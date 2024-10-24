.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

============================
Developing with spin_condpod
============================

The following sections provide information on how to develop the and with the
plugins provided by ``spin_condpod``.

Developing workflows
====================

The `spin_condpod.stdworkflows`_ plugin provides a way to run multiple spin
tasks in sequence with a single command using so-called "workflows". Plugins
that want to make use of pre-defined workflows can do so by decorating their
tasks with the `@task(when="...")`_ decorator.

It is required that a task that is decorated using `@task(when="...")` is
implementing *all* of the parameters and their respective type annotations of
the underlying workflow. Otherwise the execution of a workflow including this
misconfigured task will fail.

Please refer to the source code of the `spin_condpod.stdworkflows`_ plugin for
more information about the required parameters and their type annotations.
