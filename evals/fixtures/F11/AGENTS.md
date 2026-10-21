# Label service

This is a local standard-library utility. Normalization collapses whitespace and
preserves order/duplicates. The service must call normalization and return its
result under `labels`; invalid non-string labels return `error` with the stable
value `labels must be strings`. The domain function raises TypeError for those
invalid inputs. No network or persistence is authorized.

Run `python -m unittest discover -s tests` from this directory.
