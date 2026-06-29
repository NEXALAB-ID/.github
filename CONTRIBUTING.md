# Contributing to NEXALAB ID

Thank you for your interest in contributing to NEXALAB ID! We welcome contributions from engineers, makers, researchers, and enthusiasts of all skill levels.

---

## Table of Contents

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Reporting Issues](#reporting-issues)
- [Code Style](#code-style)

---

## Getting Started

1. **Fork** the repository you want to contribute to
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/YOUR_USERNAME/REPO_NAME.git
   ```
3. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**, then commit and push
5. **Open a Pull Request** to the `main` branch

---

## How to Contribute

There are many ways to contribute:

- Fix bugs or typos
- Improve documentation or README
- Add new examples or features
- Review Pull Requests
- Share ideas in [Discussions](https://github.com/NEXALAB-ID/discussions/discussions)

---

## Branch Naming Convention

| Type | Format | Example |
|:-----|:-------|:--------|
| New feature | `feature/short-description` | `feature/add-ota-example` |
| Bug fix | `fix/short-description` | `fix/mqtt-reconnect-issue` |
| Documentation | `docs/short-description` | `docs/update-readme` |
| Refactor | `refactor/short-description` | `refactor/wifi-handler` |

---

## Commit Message Convention

Use clear and descriptive commit messages:

```
type: short description

Examples:
feat: add BLE scan example
fix: resolve WiFi reconnect issue
docs: update MQTT disclaimer
refactor: simplify mqtt_publish code
```

| Type | When to use |
|:-----|:------------|
| `feat` | Adding a new feature or example |
| `fix` | Fixing a bug |
| `docs` | Documentation changes only |
| `refactor` | Code changes without adding features or fixing bugs |
| `chore` | Maintenance tasks (e.g., updating dependencies) |

---

## Pull Request Guidelines

- Make sure your code works before submitting
- Keep Pull Requests focused — one feature or fix per PR
- Write a clear title and description of what you changed and why
- Reference related issues if any (e.g., `Closes #12`)
- Be open to feedback and revisions

---

## Reporting Issues

Found a bug or have a suggestion? Open an issue in the relevant repository and include:

- A clear description of the problem
- Steps to reproduce (if it's a bug)
- Expected vs actual behavior
- Your board and environment (e.g., ESP32, Arduino IDE 2.x)

---

## Code Style

- Use clear and descriptive variable names
- Add comments where necessary, especially for non-obvious logic
- Keep examples simple and focused — one concept per example
- Always include a disclaimer if your code uses public services or placeholder credentials

---

<div align="center">

<sub>Part of NEXALAB ID &nbsp;·&nbsp; <strong>Innovate | Build | Connect</strong></sub>

</div>
