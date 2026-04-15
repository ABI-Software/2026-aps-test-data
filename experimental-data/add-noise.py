import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

def plot_before_after(original_values, noisy_values, column_name, output_plot_file=None):
    """Visualize the original and noisy values for a single column."""
    x_values = np.arange(len(original_values))

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, original_values, label="Original", linewidth=1.8)
    plt.plot(x_values, noisy_values, label="Noisy", linewidth=1.8, alpha=0.85)
    plt.title(f"Before vs After Noise: {column_name}")
    plt.xlabel("Row index")
    plt.ylabel(column_name)
    plt.legend()
    plt.tight_layout()

    if output_plot_file:
        plt.savefig(output_plot_file, dpi=150)
        print(f"Plot saved to {output_plot_file}")

    plt.show()


def add_noise_to_csv(input_file, output_file, column_name, noise_level=0.1, plot=False, output_plot_file=None):
    """
    Add Gaussian noise to a specified column in a CSV file.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file
        column_name: Name of column to add noise to
        noise_level: Standard deviation of noise (default: 0.1)
    """
    df = pd.read_csv(input_file)
    
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in CSV")
        return
    
    original_values = df[column_name].copy()

    # Add Gaussian noise
    noise = np.random.normal(0, noise_level, len(df))
    df[column_name] = df[column_name] + noise
    
    # Save to output file
    df.to_csv(output_file, index=False)
    print(f"Noise added successfully. Output saved to {output_file}")

    if plot:
        plot_before_after(original_values, df[column_name], column_name, output_plot_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add noise to a CSV column")
    parser.add_argument("input_file", help="Input CSV file path")
    parser.add_argument("output_file", help="Output CSV file path")
    parser.add_argument("column_name", help="Column name to add noise to")
    parser.add_argument("--noise-level", type=float, default=0.1, help="Noise level (default: 0.1)")
    parser.add_argument("--plot", action="store_true", help="Show a before/after plot of the selected column")
    parser.add_argument("--plot-file", default=None, help="Optional output file path to save the plot image")
    
    args = parser.parse_args()
    add_noise_to_csv(
        args.input_file,
        args.output_file,
        args.column_name,
        args.noise_level,
        args.plot,
        args.plot_file,
    )