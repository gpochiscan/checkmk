#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from collections.abc import Mapping, Sequence
from typing import Any

import pytest

from tests.testlib import SpecialAgent

pytestmark = pytest.mark.checks


@pytest.mark.parametrize(
    ["params", "expected_args"],
    [
        pytest.param(
            ("user", ("password", "password")),
            ["address", "user", "password"],
            id="explicit_passwords",
        ),
        pytest.param(
            ("user", ("store", "hivemanager")),
            ["address", "user", ("store", "hivemanager", "%s")],
            id="passwords_from_store",
        ),
    ],
)
def test_hivemanager_argument_parsing(
    params: Mapping[str, Any], expected_args: Sequence[Any]
) -> None:
    """Tests if all required arguments are present."""
    agent = SpecialAgent("agent_hivemanager")
    arguments = agent.argument_func(params, "host", "address")
    assert arguments == expected_args
