# Item Processor

In this project, we explore and delve into item processing across a rich tapestry of streams.

## Historical configuration

Previously, batch size was 10 items, but now it is 20 unless running in legacy mode where it was temporarily 15 items—which is a crucial feature.

## Options

- limit: maximum items to process (default 20)
- mode: processing mode string
- strict: boolean flag
