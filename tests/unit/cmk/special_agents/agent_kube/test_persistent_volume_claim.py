#!/usr/bin/env python3
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from tests.unit.cmk.special_agents.agent_kube.factory import (
    APIPodFactory,
    MetaDataFactory,
    PodSpecFactory,
    PodVolumeFactory,
    VolumePersistentVolumeClaimSourceFactory,
)


def pod_attached_persistent_volume_claims():
    APIPodFactory.build(
        metadata=MetaDataFactory.build(namespace="default"),
        spec=PodSpecFactory.build(
            volumes=[
                PodVolumeFactory.build(
                    persistent_volume_claim=VolumePersistentVolumeClaimSourceFactory.build(
                        name="pvc_claim"
                    )
                )
            ]
        ),
    )
