from utility import mean_by_year
def plot_sample_484(ax,
                    x,
                    y_sample
                    , y_484,
                    y_real,
                    d_sample: dict,
                    d_4_8_4: dict,
                    d_real: dict):
    ax.plot(x, y_sample, **d_sample)
    ax.plot(x, y_484, **d_4_8_4)
    ax.plot(x, y_real, **d_real)
    ax.tick_params(axis='x', rotation=90)
    ax.grid(axis='y')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


def plot_sample_484_yearly(ax,
                           x,
                           y_sample
                           , y_484,
                           y_real,
                           d_sample: dict,
                           d_4_8_4: dict,
                           d_real: dict):
    ax.plot(*mean_by_year(x, y_sample), **d_sample)
    ax.plot(*mean_by_year(x, y_484), **d_4_8_4)
    ax.plot(*mean_by_year(x, y_real), **d_real)
    ax.tick_params(axis='x', rotation=90)
    ax.grid(axis='y')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)