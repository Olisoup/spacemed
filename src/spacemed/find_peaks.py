import numpy


def find_peaks(absorption, w=50):
    absorption = numpy.array(absorption)
    subset = absorption
    peaks = []
    for i in range(len(subset)):
        start = max(i - w, 0)
        end = min(i + w, len(subset))
        window = subset[start:end]
        max_pos = numpy.argmax(window) + start

        if i == max_pos:
            peaks.append(i)
    return numpy.array(peaks)
