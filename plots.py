from util import mean_by_year


def plot_sample_484(ax, x, y_sample, y_484, y_real, d_sample: dict, d_4_8_4: dict, d_real: dict):
    """
    Plot sample data, 4-8-4 method data, and real data on a given axis.

    Parameters:
    ax : matplotlib.axes.Axes
        The axis object to plot on.
    x : array-like
        The x-axis values (typically dates or time periods).
    y_sample : array-like
        The y-values for the sample data.
    y_484 : array-like
        The y-values calculated using the 4-8-4 method.
    y_real : array-like
        The y-values for the real (actual) data.
    d_sample : dict
        Plotting parameters for the sample data line.
    d_4_8_4 : dict
        Plotting parameters for the 4-8-4 method data line.
    d_real : dict
        Plotting parameters for the real data line.

    Notes:
    - This function plots three lines on the given axis: sample data, 4-8-4 method data, and real data.
    - The function also applies some styling to the axis (grid, spine visibility, etc.).
    """
    # Plot the three data series
    ax.plot(x, y_sample, **d_sample)
    ax.plot(x, y_484, **d_4_8_4)
    ax.plot(x, y_real, **d_real)

    # Rotate x-axis labels for better readability
    ax.tick_params(axis='x', rotation=90)

    # Add a grid on the y-axis
    ax.grid(axis='y')

    # Remove top and right spines for a cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def plot_sample_484_yearly(ax, x, y_sample, y_484, y_real, d_sample: dict, d_4_8_4: dict, d_real: dict):
    """
    Plot yearly averages of sample data, 4-8-4 method data, and real data on a given axis.

    Parameters:
    ax : matplotlib.axes.Axes
        The axis object to plot on.
    x : array-like
        The x-axis values (typically dates or time periods).
    y_sample : array-like
        The y-values for the sample data.
    y_484 : array-like
        The y-values calculated using the 4-8-4 method.
    y_real : array-like
        The y-values for the real (actual) data.
    d_sample : dict
        Plotting parameters for the sample data line.
    d_4_8_4 : dict
        Plotting parameters for the 4-8-4 method data line.
    d_real : dict
        Plotting parameters for the real data line.

    Notes:
    - This function calculates and plots yearly averages for 3 data series: sample data, 4-8-4 method data, and real data.
    - It uses the mean_by_year function from the utility module to calculate yearly averages.
    - The function also applies some styling to the axis (grid, spine visibility, etc.).
    """
    # Plot yearly averages for each data series
    ax.plot(*mean_by_year(x, y_sample), **d_sample)
    ax.plot(*mean_by_year(x, y_484), **d_4_8_4)
    ax.plot(*mean_by_year(x, y_real), **d_real)

    # Rotate x-axis labels for better readability
    ax.tick_params(axis='x', rotation=90)

    # Add a grid on the y-axis
    ax.grid(axis='y')

    # Remove top and right spines for a cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
