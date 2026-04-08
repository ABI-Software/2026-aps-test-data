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

## Generate thumbnail plots

Create clean, minimal thumbnail images with all columns plotted against the first column (no axis labels, ticks, legend, or spines):

```powershell
uv run python generate-thumbnail.py <input.csv> <output.png>
```

Customize dimensions and resolution:

```powershell
uv run python generate-thumbnail.py <input.csv> <output.png> --width 4 --height 2 --dpi 150
```

Usage examples:

```powershell
# Default 3"x1.5" @ 100 dpi
uv run python generate-thumbnail.py data.csv output.png

# High-res 4"x2" @ 150 dpi
uv run python generate-thumbnail.py data.csv output.png --width 4 --height 2 --dpi 150
```
