import numpy


def normalise(data):
    """
    Z-score normalise a 1-D numpy array.

    Steps
    -----
    1. Subtract the mean  → centres the signal around 0
    2. Divide by the std  → scales so that one unit = one standard deviation

    Special case: if every sample is identical (std == 0), the division
    would produce NaN values.  Instead we return an array of zeros, which
    correctly indicates "no variation, therefore no correlation".

    Parameters
    ----------
    data : 1-D numpy array
        The time series to normalise (e.g. signal from one voxel over time).

    Returns
    -------
    norm : 1-D numpy array, same length as `data`
        Normalised time series (z-scores).
    """
    if numpy.std(data) == 0:
        # Guard against division by zero: a flat line has no information,
        # so we return all zeros (zero correlation with anything).
        return numpy.zeros_like(data)

    norm = (data - numpy.mean(data)) / numpy.std(data)
    return norm
