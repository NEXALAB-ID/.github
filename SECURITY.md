# Security Policy

## Supported Projects

We take security seriously across all NEXALAB ID repositories. This policy applies to all public projects under the [NEXALAB-ID](https://github.com/NEXALAB-ID) organization.

---

## Reporting a Vulnerability

If you discover a security vulnerability in any of our projects, please **do not** open a public issue. Instead, report it privately through [GitHub Discussions](https://github.com/NEXALAB-ID/discussions/discussions) with the category set to **Security**, or contact the maintainers directly via GitHub.

Please include:

- A description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

We will review and respond to your report as soon as possible.

---

## Security Best Practices for Contributors

When contributing to any NEXALAB ID project, please follow these guidelines:

- **Never commit credentials** — WiFi passwords, API keys, tokens, or any sensitive information should never be pushed to a repository
- **Use placeholder values** — always use placeholders like `YOUR_SSID` or `YOUR_API_KEY` in example code
- **Generate unique UUIDs** — do not reuse default UUIDs in production code (see `ble_server` example)
- **Use private brokers** — avoid public MQTT brokers for any real-world or production deployment

---

## Disclosure Policy

We follow a **responsible disclosure** policy. Once a vulnerability is reported and confirmed, we will:

1. Acknowledge receipt of the report
2. Investigate and develop a fix
3. Release a patch as soon as possible
4. Credit the reporter (if they wish to be credited)

---

<div align="center">

<sub>Part of NEXALAB ID &nbsp;·&nbsp; <strong>Innovate | Build | Connect</strong></sub>

</div>
