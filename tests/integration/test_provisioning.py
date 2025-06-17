# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for csspin_workflows"""

import subprocess

import pytest


def execute_spin(yaml, env, path="tests/integration/yamls", cmd=""):
    """Helper function to execute spin and return the output"""
    try:
        return subprocess.check_output(
            (
                f"spin -p spin.cache={env} -C {path} --env {str(env)} -f {yaml} " + cmd
            ).split(" "),
            encoding="utf-8",
            stderr=subprocess.PIPE,
        ).strip()
    except subprocess.CalledProcessError as ex:
        print(ex.stdout)
        print(ex.stderr)
        raise


@pytest.mark.integration()
def test_stdworkflows_provision(tmp_path):
    """Provision the stdworkflows plugin"""
    execute_spin(yaml="stdworkflows.yaml", env=tmp_path, cmd="cleanup")
    execute_spin(yaml="stdworkflows.yaml", env=tmp_path, cmd="provision")
    assert "all build tasks" in execute_spin(
        yaml="stdworkflows.yaml", env=tmp_path, cmd="build --help"
    )
