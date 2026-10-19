# Remora

Remora is a portable, agent-native engineering harness for AI-assisted software development.

It is intended to provide reusable instructions, skills, and workflows that help coding agents establish consistent development practices, adapt to different projects, and maintain software quality as projects evolve.

Remora is designed to work alongside existing coding environments rather than replace their execution capabilities. Its initial targets are Codex, Cursor, and Antigravity.

## Status

Remora is in early development. The current baseline contains skill contracts, F01/F02 bootstrap fixture preparation and rubrics, and a bounded content checker with tests. Installable skills and bootstrap tooling are not implemented, and native-host compatibility remains unverified.

The [product and technical specification](docs/product-spec.md) defines intended behavior. The [evaluation guide](evals/README.md) explains fixture preparation, calibration, and development checks; the [dated baseline record](evals/records/2026-10-19-baseline.md) records design inputs and testing candidates. This baseline advances Milestone 1 without declaring it complete.

## Design principles

- **Agent-native:** Use the reasoning and execution capabilities of existing coding environments.
- **Portable:** Share engineering practices across environments, languages, and project architectures.
- **Project-aware:** Adapt guidance to actual requirements and repository evidence.
- **Maintainable:** Treat documentation integrity, test quality, and configuration health as ongoing responsibilities.
- **Lightweight:** Avoid unnecessary infrastructure, dependencies, and complexity.

## Documentation

See [Product and Technical Specification](docs/product-spec.md) for the intended architecture, requirements, development milestones, and acceptance criteria.
