import numpy # noqa


def calc_heart_rate(time, peaks):
    tp = time[peaks]
    delta_t = tp[1:]-tp[:-1]
    hr = 60/delta_t
    return hr
