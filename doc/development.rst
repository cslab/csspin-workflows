.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   https://www.contact-software.com/

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

================================
Developing with csspin-workflows
================================

The following sections provide information on how to develop the and with the
plugins provided by ``csspin-workflows``.

Developing workflows
====================

The :ref:`csspin_workflows.stdworkflows` plugin provides a way to run multiple spin
tasks in sequence with a single command using so-called "workflows". Plugins
that want to make use of pre-defined workflows can do so by decorating their
tasks with the ``@task(when="...")`` decorator.

It is required that a task that is decorated using ``@task(when="...")`` is
implementing *all* of the parameters and their respective type annotations of
the underlying workflow. Otherwise the execution of a workflow including this
misconfigured task will fail.

Please refer to the source code of the :ref:`csspin_workflows.stdworkflows` plugin for
more information about the required parameters and their type annotations.
