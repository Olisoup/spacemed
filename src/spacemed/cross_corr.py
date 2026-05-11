import seaborn # noqa
import pandas # noqa
import nibabel # noqa
import scipy.signal # noqa
import numpy # noqa
import spacemed # noqa
from .normalise import normalise # noqa


def cross_corr(signal, fmri_data, voxel):
    """
    Compute and plot the cross-correlation between a stimulus signal
    and the fMRI time series at a single voxel.

    Parameters
    ----------
    signal : 1-D array-like
        The stimulus on/off sequence.  Length must equal fmri_data.shape[-1].
        Example: numpy.array([1,1,1,1,1, 0,0,0,0,0] * 8)
    fmri_data : 4-D numpy array, shape (x, y, z, time)
        The full fMRI dataset as returned by nibabel's .get_fdata().
    voxel : tuple of three ints  (i, j, k)
        The 3-D index of the voxel you want to analyse.
        i → x-axis (left/right), j → y-axis (front/back), k → z-axis (slice)

    Returns
    -------
    peak_corr : float
        The maximum cross-correlation value (the activation score).
    peak_lag  : float
        The lag (in samples) at which the peak occurs.
        A positive peak_lag means the brain response comes AFTER the stimulus,
        which is the expected haemodynamic delay (~4–8 s for a TR of 2 s).
    """
    # ── Step 1: extract the time series at the chosen voxel ─────────────────
    # fmri_data[i, j, k] returns a 1-D array of length `time` because we
    # index all three spatial dimensions, leaving only the time axis.
    i, j, k = voxel
    ts = fmri_data[i, j, k]  # shape: (nt,)

    # ── Step 2: normalise both signals ──────────────────────────────────────
    ts_norm = normalise(ts)
    sig_norm = normalise(numpy.array(signal, dtype=float))

    # ── Step 3: compute the cross-correlation ───────────────────────────────
    # scipy.signal.correlate slides one signal over the other and computes
    # the dot-product at each offset.
    # mode="same" → output length equals the longer of the two inputs,
    #               keeping lags centred around zero.
    cross = scipy.signal.correlate(ts_norm, sig_norm, mode="same")

    # correlation_lags gives us the actual lag values (in samples) that
    # correspond to each element of `cross`.
    lags = scipy.signal.correlation_lags(len(ts_norm), len(sig_norm),
                                         mode="same")

    # ── Step 4: find the peak ────────────────────────────────────────────────
    peak_idx = numpy.argmax(cross)   # index of the maximum value
    peak_corr = cross[peak_idx]       # the maximum correlation value
    peak_lag = lags[peak_idx]        # the lag (in samples) at the peak

    return lags, cross, peak_corr, peak_lag
