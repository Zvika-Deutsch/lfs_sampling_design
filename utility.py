import numpy as np
import pandas as pd


def rand_group_b(group_b, val_group_a, val_group_b, size, n=80):
    sd = np.sqrt(group_b * (1 - group_b) / n)
    sample_b = np.random.normal(group_b, sd, size)
    employment = val_group_b * sample_b + val_group_a * (1 - sample_b)
    return sample_b, employment

def mean_4_8_4(val: pd.Series):
    v = val.rolling(4).mean()
    v = (v.shift(12) + v) / 2
    return v


def mean_by_year(times, val: pd.Series | np.ndarray | list):
    if isinstance(val, pd.Series):
        v = val.groupby(times).mean()
    elif isinstance(val, list):
        v = np.array(val)
        v = list(val.reshape((len(val) // 12, 12)).mean(axis=1))
    elif isinstance(val, np.ndarray):
        v = list(val.reshape((len(val) // 12, 12)).mean(axis=1))
    else:
        raise ValueError('val must be pd.Series or list or np.ndarray')
    t = list(times.to_period('Y').unique().astype(str))
    return t, v
