#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# fmt: off
# type: ignore

from cmk.base.plugins.agent_based.esx_vsphere_hostsystem_section import parse_esx_vsphere_hostsystem

checkname = "esx_vsphere_hostsystem"

parsed = parse_esx_vsphere_hostsystem(
    [
        [
            # This is output from the old API endpoint for the check esx_vsphere_hostsystem.multipath
            # which is not supported anymore.
            "config.multipathState.path",
            "fc.20000024ff2e1b4c:21000024ff2e1b4c-fc.500a098088866d7e:500a098188866d7e-naa.60a9800044314f68553f436779684544",
            "active",
        ],
        ["hardware.cpuInfo.hz", "2792999719"],
        ["hardware.cpuInfo.numCpuCores", "12"],
        ["hardware.cpuInfo.numCpuPackages", "2"],
        ["hardware.cpuInfo.numCpuThreads", "24"],
        ["hardware.memorySize", "309224034304"],
        ["name", "df1-esx03.roelfspartner.local"],
        ["overallStatus", "green"],
        ["runtime.inMaintenanceMode", "false"],
        ["runtime.powerState", "poweredOn"],
        ["summary.quickStats.overallCpuUsage", "1930"],
        ["summary.quickStats.overallMemoryUsage", "79464"],
    ]
)

discovery = {
    "": [],
    "cpu_usage": [(None, {})],
    "cpu_util_cluster": [],
    "maintenance": [(None, {"target_state": "false"})],
    "mem_usage": [(None, "esx_host_mem_default_levels")],
    "mem_usage_cluster": [],
    "multipath": [],
    "state": [(None, None)],
}

checks = {
    "cpu_usage": [
        (
            None,
            {},
            [
                (
                    0,
                    "Total CPU: 5.76%",
                    [("util", 5.758444307717932, None, None, 0, 100)],
                ),
                (0, "1.93GHz/33.52GHz", []),
                (0, "2 sockets, 6 cores/socket, 24 threads", []),
            ],
        )
    ],
    "maintenance": [
        (
            None,
            {"target_state": "false"},
            [
                (0, "System not in Maintenance mode", []),
            ],
        )
    ],
    "mem_usage": [
        (
            None,
            (80.0, 90.0),
            [
                (
                    0,
                    "Usage: 26.95% - 77.6 GiB of 288 GiB",
                    [
                        (
                            "mem_used",
                            83324043264.0,
                            247379227443.2,
                            278301630873.60004,
                            0,
                            309224034304.0,
                        ),
                        ("mem_total", 309224034304.0, None, None, None, None),
                    ],
                )
            ],
        )
    ],
    "state": [(None, {}, [(0, "Entity state: green", []), (0, "Power state: poweredOn", [])])],
}
