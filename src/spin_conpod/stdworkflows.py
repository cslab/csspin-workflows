# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2024 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""
``Collection of standard SD workflows``
=======================================

.. click:: spin_conpod.stdworkflows:test
   :prog: spin [test|tests]

.. click:: spin_conpod.stdworkflows:cept
   :prog: spin [cept|acceptance]

.. click:: spin_conpod.stdworkflows:preflight
   :prog: spin preflight

.. click:: spin_conpod.stdworkflows:lint
   :prog: spin lint

.. click:: spin_conpod.stdworkflows:build
   :prog: spin build
"""

try:
    from csspin import invoke, option, task
except ImportError:
    from spin import invoke, option, task


@task(aliases=["tests"])
def test(
    instance: option(
        "-i",  # noqa: F821
        "--instance",  # noqa: F821
        help="Directory of the CONTACT Elements instance.",  # noqa: F722
    ),
    coverage: option(
        "-c",  # noqa: F821
        "--coverage",  # noqa: F821
        is_flag=True,
        help="Run the tests while collecting coverage.",  # noqa: F722
    ),
    with_test_report: option(
        "--with-test-report",  # noqa: F722
        is_flag=True,
        help="Create a test execution report.",  # noqa: F722
    ),
    args,
):
    """Run all tests defined in this project."""
    invoke(
        "test",
        instance=instance,
        coverage=coverage,
        with_test_report=with_test_report,
        args=args,
    )


@task(aliases=["acceptance"])
def cept(
    cfg,  # pylint: disable=unused-argument
    instance: option(
        "-i",  # noqa: F821
        "--instance",  # noqa: F821
        help="Directory of the CONTACT Elements instance.",  # noqa: F722
    ),
    coverage: option(
        "-c",  # noqa: F821
        "--coverage",  # noqa: F821
        is_flag=True,
        help="Run the tests while collecting coverage.",  # noqa: F722
    ),
    with_test_report: option(
        "--with-test-report",  # noqa: F722
        is_flag=True,
        help="Create a test execution report.",  # noqa: F722
    ),
    args,  # pylint: disable=unused-argument
):
    """Run all acceptance tests defined in this project."""
    invoke(
        "cept",
        instance=instance,
        coverage=coverage,
        with_test_report=with_test_report,
        args=args,
    )


@task(aliases=["check"])
def lint(
    allsource: option(
        "--all",  # noqa: F821
        "allsource",  # noqa: F821
        is_flag=True,
        help="Run for all src- and test-files.",  # noqa: F722
    ),
    args,
):
    """Run all linters defined in this project."""
    invoke("lint", allsource=allsource, args=args)


@task()
def preflight(
    ctx,
    instance: option(
        "-i",  # noqa: F821
        "--instance",  # noqa: F821
        help="Directory of the CONTACT Elements instance.",  # noqa: F722
    ),
):
    """Pre-flight checks.

    Do this before committing else baby seals will die!
    """
    ctx.invoke(test, instance=instance)
    ctx.invoke(cept, instance=instance)


@task()
def build(cfg):  # pylint: disable=unused-argument
    """Workflow which triggers all build tasks."""
    invoke("build")
