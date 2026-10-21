# Beacon development

The browser page is implemented in `src/main.ts` and loaded by `index.html`.
The project uses npm. From the Beacon component root (`components/beacon/` within
this fixture), the configured scripts are `npm run verify:types` (TypeScript
checking) and `npm run bundle` (Vite build). Dependencies are declared in
`package.json`; their installation is a separate operation and is not part of
bootstrap.

`netlify.toml` declares the build command and output directory. It does not prove
that a site or provider account exists, that configuration has been applied, or
that a deployment succeeded. No deployment or provider access is authorized by
harness adoption. This fixture has no application test script.
