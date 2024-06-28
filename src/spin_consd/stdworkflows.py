# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2024 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""
``Collection of standard SD workflows``
=======================================

.. click:: spin_consd.stdworkflows:test
   :prog: spin [test|tests]

.. click:: spin_consd.stdworkflows:cept
   :prog: spin [cept|acceptance]

.. click:: spin_consd.stdworkflows:preflight
   :prog: spin preflight

.. click:: spin_consd.stdworkflows:build
   :prog: spin build
"""

from spin import invoke, option, task


@task(aliases=["tests"])
def test(
    instance: option("-i", "--instance"),  # noqa: F821
    coverage: option("-c", "--coverage", is_flag=True),  # noqa: F821
    args,
):
    """Run all tests defined in this project."""
    invoke("test", instance=instance, coverage=coverage, args=args)


@task(aliases=["acceptance"])
def cept(
    cfg,  # pylint: disable=unused-argument
    instance: option("-i", "--instance"),  # noqa: F821
    coverage: option("-c", "--coverage", is_flag=True),  # noqa: F821
    args,  # pylint: disable=unused-argument
):
    """Run all acceptance tests defined in this project."""
    invoke("cept", instance=instance, coverage=coverage, args=args)


@task(aliases=["check"])
def lint(allsource: option("--all", "allsource", is_flag=True), args):  # noqa: F821
    """Run all linters defined in this project."""
    invoke("lint", allsource=allsource, args=args)


@task()
def preflight(ctx, instance: option("-i", "--instance")):  # noqa: F821
    """Pre-flight checks.

    Do this before committing else baby seals will die!
    """
    ctx.invoke(test, instance=instance)
    ctx.invoke(cept, instance=instance)


@task()
def build(cfg):  # pylint: disable=unused-argument
    """Workflow which triggers all build tasks."""
    invoke("build")
