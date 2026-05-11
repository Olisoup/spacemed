from matplotlib import pyplot


def plot_cross_corr(lags, cross, peak_corr, peak_lag, voxel):
    """
    Plot the cross-correlation curve produced by cross_corr().
    Call this separately when you actually want a figure.
    """
    fig, ax = pyplot.subplots(figsize=(9, 4))

    ax.plot(lags, cross, color="steelblue", linewidth=1.5,
            label="Cross-correlation")
    ax.axvline(x=peak_lag, color="red", linestyle="--", alpha=0.6,
               label=f"Peak lag = {peak_lag} samples")
    ax.scatter([peak_lag], [peak_corr], color="red", zorder=5,
               label=f"Peak value = {peak_corr:.2f}")
    ax.axhline(0, color="grey", linewidth=0.8, linestyle=":")

    ax.set_title(f"Cross-Correlation at Voxel {voxel}", fontsize=13)
    ax.set_xlabel("Lag (samples)")
    ax.set_ylabel("Correlation")
    ax.legend()
    pyplot.tight_layout()
    pyplot.show()

    print(f"Voxel           : {voxel}")
    print(f"Peak correlation: {peak_corr:.4f}")
    print(f"Peak lag        : {peak_lag} samples")
