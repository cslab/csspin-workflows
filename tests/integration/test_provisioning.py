# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for spin_docs"""

import subprocess

import pytest


def execute_spin(yaml, env, path="tests/integration/yamls", cmd=""):
    """Helper function to execute spin and return the output"""
    return subprocess.check_output(
        (
            f"spin -p spin.data={env} -C {path} --env {str(env)} -f {yaml}"
            " --cleanup --provision " + cmd
        ).split(" "),
        encoding="utf-8",
        stderr=subprocess.PIPE,
    ).strip()


@pytest.mark.integration()
def test_stdworkflows_provision(tmp_path):
    """Provision the stdworkflows plugin"""
    assert "all build tasks" in execute_spin(
        yaml="stdworkflows.yaml",
        env=tmp_path,
        cmd="build --help",
    )
