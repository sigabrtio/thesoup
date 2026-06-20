# CHANGELOG


## v0.1.0 (2026-06-20)

### Bug Fixes

- **ci**: Auth fix for semantic-release
  ([`df8219e`](https://github.com/sigabrtio/thesoup/commit/df8219e91a984b8a44224e63e847ae8afe4ddb7e))

- **ci**: Fixed semantic release repo that Claude got wrong. Developers will be obsolete my ass
  ([`af0d623`](https://github.com/sigabrtio/thesoup/commit/af0d62329fb6953c62655442384d1687339fd47e))

- **doc**: Fixed the pdoc command
  ([`84a9957`](https://github.com/sigabrtio/thesoup/commit/84a995785f7a05ff8c9fe31b172c4eb32360e794))

- **docs**: Correct GitHub Pages URL to sigabrtio org
  ([`a57ca3a`](https://github.com/sigabrtio/thesoup/commit/a57ca3a6a6e609b0c46ecf552892e9995ecde42a))

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

### Documentation

- Add module docstrings so pdoc pages are not empty
  ([`54f06e0`](https://github.com/sigabrtio/thesoup/commit/54f06e0cd9a957d8e2c5ebecb20d1feb399835bb))

All three __init__.py files were empty, causing pdoc to render blank pages. Added docstrings with
  cross-linked module tables so each package page acts as a navigable index into its submodules.
  Avoided re-exporting symbols at the package level to sidestep a circular import (graph →
  collectionutils → graphtraversals → graph).

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- Polish README and fix repo URLs
  ([`fac0dca`](https://github.com/sigabrtio/thesoup/commit/fac0dca1f6e26897f682319f9462f95b6f7edd3f))

Rewrote README with badge strip (GPLv2, PyPI, Python version, docs), modernised install instructions
  (drop sudo/pip3, use nose2 correctly), and tightened component listing. Fixed stale amartya00 →
  sigabrtio GitHub URLs in both README and setup.py.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

### Features

- **ci**: Set up GH workflow files
  ([`052f73b`](https://github.com/sigabrtio/thesoup/commit/052f73b83454fd70f36a799160ec6f663439f322))

- **ci**: Wire in python-semantic-release for auto-versioning
  ([`ebd5618`](https://github.com/sigabrtio/thesoup/commit/ebd56180c9f43840c67663a0ad3e98bff5e489dc))

Adds a release workflow that runs on every push to master and uses python-semantic-release to derive
  the next version from conventional commit messages (fix→patch, feat→minor, breaking→major), bump
  setup.py, tag, and cut a GitHub release automatically.

Also corrects the version string from '1.01' to '1.1.0' (semver).

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- **docs**: Wired in doc publishing
  ([`81ab5e7`](https://github.com/sigabrtio/thesoup/commit/81ab5e7aab07deb9faeb5667dcebfbbc7ec89a9f))
