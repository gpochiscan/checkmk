#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# pylint: disable=redefined-outer-name

import sys

import agents.wnx.tests.testlib.utils as testlib

sys.path.insert(0, str(testlib.get_git_root_path()))
