# 🧰 Python Starter Template

This is a minimalist Python project template configured for automatic **PEP 8 compliance** using [Ruff](https://docs.astral.sh/ruff/) and [Pre-commit](https://pre-commit.com/), plus optional VS Code setup.

## 🚀 Quickstart

### 1. Install dependencies
```bash
pip install pre-commit ruff
```

### 2. Install Git pre-commit hooks
```bash
pre-commit install
```

### 3. Run pre-commit manually (optional, recommended for first run)
```bash
pre-commit run --all-files
```

---

## 🔧 Configuration

### Ruff
All code style and linting rules are managed in `pyproject.toml`. Ruff is configured to:
- Enforce PEP 8 with opinionated fixes
- Use Black-like formatting (via `ruff format`)
- Target Python 3.11

### Pre-commit Hooks
Hooks are defined in `.pre-commit-config.yaml`. This template includes:
- **ruff**: Lint with auto-fix
- **ruff-format**: Format code
- **YAML/JSON/whitespace fixers** for non-code hygiene

---

## 📁 Project Structure
```
your-project/
├── pyproject.toml
├── .pre-commit-config.yaml
├── README.md
└── src/
    └── main.py
```

---

## ✅ Result
Any committed code will be:
- PEP 8-compliant
- Cleanly formatted
- Automatically linted and fixed

This setup is ideal for individuals or teams aiming for consistent, clean Python code with zero manual effort.

---

## 🧩 (Optional) VS Code / Cursor Setup

To get the best development experience with automatic formatting and linting in real-time:

### Required Extensions
- **Ruff** (official extension by `Astral`) – _Replaces Black, isort, flake8_
- **Pylance** – for type checking and rich intellisense
- **Prettier** (optional) – for non-Python files like Markdown or JSON

### Suggested `settings.json`
```json
{
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },
  "editor.rulers": [88],
  "files.autoSave": "afterDelay"
}
```

Ensure your Python environment is selected correctly via the Command Palette (Cmd/Ctrl+Shift+P → "Python: Select Interpreter").
