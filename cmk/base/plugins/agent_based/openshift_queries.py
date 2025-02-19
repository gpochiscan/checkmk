#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
import itertools

from cmk.base.plugins.agent_based.agent_based_api.v1 import register, Result, Service, State
from cmk.base.plugins.agent_based.agent_based_api.v1.type_defs import (
    CheckResult,
    DiscoveryResult,
    StringTable,
)
from cmk.base.plugins.agent_based.utils.kube import (
    COLLECTOR_SERVICE_NAME,
    OpenShiftEndpoint,
    PrometheusResult,
    ResultType,
)


def parse(string_table: StringTable) -> OpenShiftEndpoint:
    return OpenShiftEndpoint.parse_raw(string_table[0][0])


register.agent_section(
    name="prometheus_debug_v1",
    parsed_section_name="prometheus_debug",
    parse_function=parse,
)


def discover(section: OpenShiftEndpoint) -> DiscoveryResult:
    yield Service()


SEVERITY = {
    ResultType.request_exception: State.CRIT,
    ResultType.json_decode_error: State.CRIT,
    ResultType.validation_error: State.CRIT,
    ResultType.response_error: State.CRIT,
    ResultType.response_empty_result: State.CRIT,
    ResultType.response_invalid_data: State.UNKNOWN,
    ResultType.success: State.OK,
}

RANK_ORDER = {
    ResultType.request_exception: 0,
    ResultType.json_decode_error: 1,
    ResultType.validation_error: 2,
    ResultType.response_error: 3,
    ResultType.response_empty_result: 4,
    ResultType.response_invalid_data: 5,
    ResultType.success: 6,
}


def check(section: OpenShiftEndpoint) -> CheckResult:
    yield Result(state=State.OK, notice=f"Endpoint: {section.url}")

    def key(error: PrometheusResult) -> tuple[int, str, ResultType]:
        return RANK_ORDER[error.type_], error.summary(), error.type_

    total = len(section.results)
    for (_rank, summary, type_), errors_per_header in itertools.groupby(
        sorted(section.results, key=key), key=key
    ):
        queries_per_header = [error.query_ for error in errors_per_header]
        yield Result(state=SEVERITY[type_], summary=summary)
        if len(queries_per_header) == total:
            yield Result(state=State.OK, notice="| this applies to all queries.")
        else:
            for query in queries_per_header:
                yield Result(state=State.OK, notice=f"| {query}")


register.check_plugin(
    name="openshift_queries",
    service_name=COLLECTOR_SERVICE_NAME,
    sections=["prometheus_debug"],
    discovery_function=discover,
    check_function=check,
)
