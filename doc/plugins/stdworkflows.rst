.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

.. _spin_conpod.stdworkflows:

========================
spin_conpod.stdworkflows
========================

The ``spin_conpod.stdworkflows`` plugin provides a way to run multiple spin tasks
in sequence with a single command using so-called "workflows".

``spin_conpod.stdworkflows`` ships the following workflows:

* build (running tasks decorated by ``@task(when="build")```)
* cept / acceptance (... by ``@task(when="cept")``)
* test / tests (... by ``@task(when="test")``)
* preflight (... by ``@task(when="test")`` and ``@task(when="cept")``)
* lint / check (... by ``@task(when="lint")``)

How to setup the ``spin_conpod.stdworkflows`` plugin?
#####################################################

For using the ``spin_conpod.stdworkflows`` plugin, a project's ``spinfile.yaml``
must at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to setup ``spin_conpod.stdworkflows``

    plugin_packages:
        - spin_conpod
    plugins:
        - spin_conpod.stdworkflows

The provisioning of the required virtual environment can be done via the
well-known ``spin provision``-command. For using the plugin it is recommended
to provision further plugins that make use of the ``@task(when=)``-decorator.

How to run a basic workflow?
############################

A basic workflow like "test" can be run by having at least one plugin enabled
that implements a task decorated by "test". (If there is no such plugin, nothing
will happen.)

In the following, this is demonstrated using the ``spin_python.pytest`` plugin.

.. code-block:: yaml
    :caption: Example: Minimal configuration to run the "pytest"-task by using the "test" workflow

    plugin_packages:
        - spin_conpod
        - spin_python
    plugins:
        - spin_conpod.stdworkflows
        - spin_python.pytest
    python:
        version: "3.11.9"
    ...

After provisioning, the "test" workflow can be run using ``spin test``, which
will automatically collect the "pytest" task and execute it.

How to run all unit and acceptance tests of a CE-based project?
###############################################################

The ``spin_conpod.stdworkflows`` plugin provides a "preflight"-workflow, which
executes all spin tasks decorated by "test" and "cept". The task "pytest" of the
``spin_python.pytest`` plugin for example is decorated by "test". The "cypress"
task of ``spin_frontend.cypress`` as well as the "behave" task from
``spin_python.behave`` are decorated by "cept".

.. code-block:: yaml
    :caption: Excerpt: ``spinfile.yaml`` configuration for running the preflight workflow

    plugin_packages:
        - spin_ce
        - spin_conpod
        - spin_frontend
        - spin_python
    plugins:
        - spin_conpod.stdworkflows
        - spin_frontend.cypress
        - spin_python:
            - pytest
            - behave
    python:
        version: "3.11.9"
    node:
        version: "18.17.1"
    cypress:
        version: "10.3.0"
    ...

Assuming the project is provisioned and an sqlite instance is already created,
all tasks decorated with "test" and "cept" can be triggered in sequence by
calling:

.. code-block:: console
    :caption: Running the preflight workflow

    spin preflight

``spin_conpod.stdworkflows`` schema reference
#############################################

.. include:: stdworkflows_schemaref.rst
