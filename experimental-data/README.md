# experimental-data tools

This folder is initialized for `uv`.

## Setup

```powershell
uv sync
```

## Run the script

```powershell
uv run python add-noise.py <input.csv> <output.csv> <column_name> --noise-level 0.1
```

## Visualize before and after noise

```powershell
uv run python add-noise.py <input.csv> <output.csv> <column_name> --noise-level 0.1 --plot
```

Optionally save the plot:

```powershell
uv run python add-noise.py <input.csv> <output.csv> <column_name> --noise-level 0.1 --plot --plot-file before-after.png
```
