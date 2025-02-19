#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from tests.testlib import ActiveCheck

pytestmark = pytest.mark.checks


@pytest.mark.parametrize(
    "params,expected_args",
    [
        (
            {
                "index": "foo",
                "pattern": "bar",
            },
            ["-i", "f o o", "-q", "bar", "-H", "$HOSTADDRESS$"],
        )
    ],
)
def test_check_elasticsearch_query_argument_parsing(  # type:ignore[no-untyped-def]
    params, expected_args
) -> None:
    """Tests if all required arguments are present."""
    active_check = ActiveCheck("check_elasticsearch_query")
    assert active_check.run_argument_function(params) == expected_args
