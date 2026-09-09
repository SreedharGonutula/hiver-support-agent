# Decision Log

1. Start with AppleSupport because it has a large support volume.
2. Use a 20,000-row working sample for rapid, reproducible iteration.
3. Use seed 42 for deterministic sampling.
4. Read the CSV in chunks to control memory use.
5. Identify the brand through `author_id`; the source has no brand column.
6. Keep the raw dataset out of GitHub.
