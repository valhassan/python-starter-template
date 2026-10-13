# Python starter template

Minimal Python project. Ruff lints and formats. Pre-commit runs both before a commit lands.

## Setup

```bash
pip install pre-commit ruff
pre-commit install
pre-commit run --all-files
```

The last command is optional. Run it once so files already in the tree get fixed before you rely on the hooks.

The hook pins Ruff in `.pre-commit-config.yaml` (`rev`). `pip install ruff` tracks the current release, so bump `rev` when you want the hook and the local install on the same version.

## Configuration

Ruff is configured in `pyproject.toml`: line length 88, target Python 3.11, rule set `ALL`. Formatting is `ruff format`.

`.pre-commit-config.yaml` runs:

- `ruff` with `--fix`
- `ruff-format`
- trailing whitespace, end-of-file, YAML, JSON, and large-file checks

Those hooks are what make a commit lint-clean. They run after `pre-commit install`.

## Layout

```
.
├── pyproject.toml
├── .pre-commit-config.yaml
├── README.md
└── src/
    ├── main.py
    └── main.ipynb
```

## Editor

Install the Ruff extension. The extension id is `charliermarsh.ruff`. It covers formatting, import sorting, and the lint fixes that used to be Black, isort, and flake8.

```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "editor.rulers": [88],
  "files.autoSave": "afterDelay"
}
```

`source.fixAll.ruff` and `source.organizeImports.ruff` limit those actions to Ruff. `"explicit"` runs them on Cmd+S (Ctrl+S). Delayed autosave only writes the file. The ruler matches `line-length` in `pyproject.toml`.

Ruff does not type-check. Use Pylance, or Astral's `ty` if you want the type checker from the same place as Ruff. `ty` is still pre-1.0.

Select the project interpreter from the command palette: "Python: Select Interpreter".
