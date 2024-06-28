# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for spin_docs"""

import pytest
from spin import backtick, cli


@pytest.fixture(autouse=True)
def cfg():
    """Fixture creating the configuration tree"""
    cli.load_config_tree(None)


def execute_spin(tmpdir, what, cmd, path="tests/integration/yamls", props=""):
    """Helper to execute spin calls via spin."""
    output = backtick(
        f"spin -p spin.cache={tmpdir} {props} -C {path} --env {tmpdir} -f"
        f" {what} --cleanup --provision {cmd}"
    )
    output = output.strip()
    return output


@pytest.mark.integration()
def test_stdworkflows_provision(tmpdir):
    """Provision the stdworkflows plugin"""
    assert "all build tasks" in execute_spin(
        tmpdir=tmpdir,
        what="stdworkflows.yaml",
        cmd="build --help",
    )
