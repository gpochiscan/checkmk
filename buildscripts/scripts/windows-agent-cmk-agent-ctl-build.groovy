#!groovy

/// file: windows-agent-cmk-agent-ctl-build.groovy

def main() {
    check_job_parameters(["VERSION"]);
    
    def windows = load("${checkout_dir}/buildscripts/scripts/utils/windows.groovy");
    def versioning = load("${checkout_dir}/buildscripts/scripts/utils/versioning.groovy");
    
    def branch_name = versioning.safe_branch_name(scm);
    def cmk_version = versioning.get_cmk_version(branch_name, VERSION);

    dir("${checkout_dir}") {
        stage("make setversion") {
            bat("make -C agents\\wnx NEW_VERSION='${cmk_version}' setversion")
        }

        windows.build(
            TARGET: 'cmk_agent_ctl_no_sign',
        )
    }
}
return this;

