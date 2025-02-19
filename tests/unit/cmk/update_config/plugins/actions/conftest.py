#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# Some of the action plugin tests require an initialized UI context. This is done by referencing the
# ui_context fixture which makes an initialized context available outside of tests.unit.cmk.gui
# package. However, seems we need to import the fixtures referenced by the ui_context fixture to
# make it work.
from tests.unit.cmk.gui.conftest import (  # noqa: F401 # pylint: disable=unused-import
    load_config,
    load_plugins,
    ui_context,
)
