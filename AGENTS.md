# AGENTS.md

Guidance for AI agents working in the `csspin-workflows` repository.

## What this is

`csspin-workflows` is a plugin package for `csspin`, the task runner used
across CONTACT Software's `cs.*` projects. It provides
`csspin_workflows.stdworkflows`, which lets other plugins register spin tasks
against shared workflows (`build`, `test`/`tests`, `cept`/`acceptance`,
`preflight`, `lint`/`check`, `localize`, `sbom`) so a single command like
`spin test` runs every task any enabled plugin decorated with
`@task(when="test")`.

## Layout

- `src/csspin_workflows/stdworkflows.py` — the workflow task definitions.
- `src/csspin_workflows/stdworkflows_schema.yaml` — spinfile schema for the
  plugin's configuration.
- `doc/` — Sphinx documentation (`.rst`). `doc/plugins/stdworkflows.rst` is the
  user-facing reference for the workflows and must be kept in sync with
  `stdworkflows.py` whenever a workflow or subcommand is added, renamed, or
  removed.
- `doc/relnotes.rst` — release notes; see the instructions embedded as an RST
  comment at the top of the file for the required format per release.
- `tests/integration/` — integration tests that provision a real project via
  `spin` (see `tests/integration/yamls/`) and invoke workflows against it.

## Working in this repo

- Entry point for everything is `spin <task>`; see `spinfile.yaml` for how this
  repo provisions itself (needs `csspin-python` and `csspin-docs` to build the
  docs).
- A task registered with `@task(when="...")` must implement _all_ parameters
  (with matching type annotations) of the corresponding workflow function in
  `stdworkflows.py`. A mismatch only fails at workflow execution time, not at
  import/registration time, so keep new or changed workflow signatures and
  their consuming tasks in lockstep.
- The `sbom` workflow is the exception to the `@task(when=)` pattern: its
  subcommands (`sbom:build`, `sbom:assemble`, `sbom:enrich`, `sbom:quality`)
  are invoked directly by name rather than collected from other plugins.
- When adding or changing a workflow (or a `sbom` subcommand), update all of:
  the task in `stdworkflows.py`, the docstring `.. click::` directives at the
  top of that file, `doc/plugins/stdworkflows.rst`, and add an entry to
  `doc/relnotes.rst` under an "Unreleased" or the next version section
  following the format described there.
- Quality gate: run `prek run` (or `pre-commit run`) after any code change.
- Python package manager is `uv`; never call `python`/`pip` directly.
- Follow `CONTRIBUTING.md` for the issue-first contribution workflow and the
  release procedure.

## Common commands

- Set up a dev environment: `uv venv && uv pip install -r requirements-dev.txt`
  (installs this package editable, plus `csspin`, `pytest`, `pytest-cov`).
- Run the test suite: `pytest tests/`. The only tests today are the
  `integration`-marked ones in `tests/integration/`, which shell out to a real
  `spin` CLI against the fixture project in `tests/integration/yamls/`, so
  `spin` must be on `PATH` (installed via the dev environment above).
- Run a single test: `pytest tests/integration/test_provisioning.py::test_stdworkflows_provision`.
- Build the docs: `spin provision` once, then `spin docs html` (mirrors what
  Read the Docs runs per `.readthedocs.yaml`).
