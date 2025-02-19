// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.

use crate::modes::registration::ProxyPullData;
use crate::{cli, config};
use anyhow::{Context, Result as AnyhowResult};
use config::JSONLoader;

trait ImportDataProvider {
    fn provide(&self) -> AnyhowResult<ProxyPullData>;
}

struct ImportDataFromFile {
    path: std::path::PathBuf,
}

impl ImportDataProvider for ImportDataFromFile {
    fn provide(&self) -> AnyhowResult<ProxyPullData> {
        ProxyPullData::load(&self.path)
            .context(format!("Failed to read file {}", &self.path.display()))
    }
}

struct ImportDataFromStdin {}

impl ImportDataProvider for ImportDataFromStdin {
    fn provide(&self) -> AnyhowResult<ProxyPullData> {
        let mut buffer = String::new();
        std::io::stdin()
            .read_line(&mut buffer)
            .context("Failed to read from stdin")?;
        serde_json::from_str(&buffer)
            .context(format!("Failed to deserialize JSON data:\n{}", &buffer))
    }
}

fn _import(
    registry: &mut config::Registry,
    import_data_provider: &impl ImportDataProvider,
) -> AnyhowResult<()> {
    registry.register_imported_connection(import_data_provider.provide()?.connection);
    registry.save()?;
    Ok(())
}

pub fn import(registry: &mut config::Registry, import_opts: &cli::ImportOpts) -> AnyhowResult<()> {
    match &import_opts.conn_file {
        Some(path) => _import(
            registry,
            &ImportDataFromFile {
                path: std::path::PathBuf::from(path),
            },
        ),
        None => _import(registry, &ImportDataFromStdin {}),
    }
}

#[cfg(test)]
mod tests {
    use std::str::FromStr;

    use super::*;
    struct MockImportDataProvider {}

    impl ImportDataProvider for MockImportDataProvider {
        fn provide(&self) -> AnyhowResult<ProxyPullData> {
            Ok(ProxyPullData {
                agent_controller_version: String::from("0.1.0"),
                connection: config::TrustedConnection {
                    uuid: uuid::Uuid::from_str("2da53af5-5c06-4195-ab6f-668875710bec").unwrap(),
                    private_key: String::from("fake private key"),
                    certificate: String::from("fake cert"),
                    root_cert: String::from("fake root cert"),
                },
            })
        }
    }

    #[test]
    fn test_import() {
        let mut reg =
            config::Registry::new(tempfile::NamedTempFile::new().unwrap().as_ref()).unwrap();
        assert!(reg.is_empty());
        assert!(!reg.path().exists());
        assert!(_import(&mut reg, &MockImportDataProvider {}).is_ok());
        assert!(!reg.is_empty());
        assert!(reg.path().exists());
    }
}
