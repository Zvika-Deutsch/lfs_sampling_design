import numpy as np
import pandas as pd


def rand_group_b(group_b: float, val_group_a: float, val_group_b: float, size: int, n=80):
    """
    Generate random samples for the proportion of group B and calculate corresponding values for groups A and B.

    Parameters:
    group_b (float): Proportion of group B in the total population (A+B).
    val_group_a (float): Representative value for group A.
    val_group_b (float): Representative value for group B.
    size (int): Number of samples to generate.
    n (int, optional): Sample size for standard error calculation. Defaults to 80.

    Returns:
    tuple: Two numpy arrays:
        - sample_b: Random samples representing the proportion of group B.
        - y: Calculated outcome values based on the samples.

    Notes:
    - Utilizes a normal distribution to generate samples.
    - Standard error is calculated using the formula for the SD of the Barloni distribution.
    - The outcome 'y' is computed as a weighted average of group A + B values based on the sampled proportions.
    """
    # Calculate standard error for the sampling distribution of proportions
    se = np.sqrt(group_b * (1 - group_b) / n)

    # Generate random samples for group B proportions
    sample_b = np.random.normal(group_b, se, size)

    # Calculate outcome values as a weighted average
    y = val_group_b * sample_b + val_group_a * (1 - sample_b)

    return sample_b, y


def mean_4_8_4(val: pd.Series):
    """
    Calculate the moving average using the 4-8-4 sampling method for Labor Force Surveys (LFS).

    Parameters:
    val (pd.Series): A pandas Series containing the time series data.

    Returns:
    pd.Series: A Series with the calculated 4-8-4 moving average.

    Notes:
    - This function implements the 4-8-4 sampling method used in LFS.
    - It calculates a 4-month moving average, then combines it with the same average from 12 months prior.
    - The method accounts for the LFS rotating panel design: 4 months in, 8 months out, 4 months in.
    - The result smooths the data while preserving the seasonal pattern.
    """
    # Calculate the 4-month moving average
    v = val.rolling(4).mean()

    # Average the current 4-month average with the 4-month average from 12 months ago
    # This simulates the 4-8-4 sampling pattern
    v = (v.shift(12) + v) / 2

    return v


def mean_by_year(times, val: pd.Series | np.ndarray | list):
    """
    Calculate the yearly mean of values according to given times.

    Parameters:
    times : pd.DatetimeIndex or similar
        Time index corresponding to the values.
    val : pd.Series | np.ndarray | list
        The values for which to calculate yearly means.

    Returns:
    tuple
        (t, v) where:
        t : list of years as strings.
        v : list of corresponding yearly means.

    Raises:
    ValueError
        If val is not of type pd.Series, list, or np.ndarray.

    Notes:
    - For pd.Series, the function uses groupby on years.
    - For list and np.ndarray, the function assumes 12 values per year and averages over each 12 values.
    """
    if isinstance(val, pd.Series):
        v = val.groupby(times).mean()
    elif isinstance(val, list):
        t = np.array(val)
        v = list(val.reshape((len(val) // 12, 12)).mean(axis=1))
    elif isinstance(val, np.ndarray):
        v = list(val.reshape((len(val) // 12, 12)).mean(axis=1))
    else:
        raise ValueError('val must be pd.Series or list or np.ndarray')
    t = list(times.to_period('Y').unique().astype(str))
    return t, v
