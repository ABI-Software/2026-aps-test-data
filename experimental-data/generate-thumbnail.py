import pandas as pd
import matplotlib.pyplot as plt
import argparse


def generate_thumbnail(csv_file, output_file, width=3, height=1.5, dpi=100):
    """
    Generate a clean thumbnail plot with all columns plotted against the first column,
    without axis labels, legend, or other labels.

    Args:
        csv_file: Path to input CSV file
        output_file: Path to output image file
        width: Figure width in inches (default: 3)
        height: Figure height in inches (default: 1.5)
        dpi: Resolution in dots per inch (default: 100)
    """
    df = pd.read_csv(csv_file)

    if df.shape[1] < 2:
        print(f"Error: CSV must have at least 2 columns (x and y data)")
        return

    x_column = df.iloc[:, 0]
    y_columns = df.iloc[:, 1:]

    # Create a minimal figure
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)

    # Plot all columns against the first column
    for col in y_columns.columns:
        ax.plot(x_column, y_columns[col], linewidth=1.5)

    # Remove all labels, ticks, and spines for a clean thumbnail
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Tight layout with no padding
    plt.tight_layout(pad=0)

    # Save the figure
    plt.savefig(output_file, bbox_inches="tight", pad_inches=0, dpi=dpi)
    plt.close()

    print(f"Thumbnail saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a thumbnail plot with all columns vs first column")
    parser.add_argument("csv_file", help="Input CSV file path")
    parser.add_argument("output_file", help="Output image file path (e.g., thumbnail.png)")
    parser.add_argument("--width", type=float, default=3, help="Figure width in inches (default: 3)")
    parser.add_argument("--height", type=float, default=1.5, help="Figure height in inches (default: 1.5)")
    parser.add_argument("--dpi", type=int, default=100, help="Resolution in dpi (default: 100)")

    args = parser.parse_args()
    generate_thumbnail(
        args.csv_file,
        args.output_file,
        args.width,
        args.height,
        args.dpi,
    )
