# Plotting PPG

from pathlib import Path
from matplotlib import pyplot
import argparse
from . import read_pulse # noqa
from . import find_peaks # noqa
from . import calc_heart_rate # noqa
from . import __version__


def main():
    parser = arg_parser()
    args = parser.parse_args()

    # Load data
    import spacemed
    import numpy
    from matplotlib import pyplot as plt
    time, absorption = spacemed.read_pulse(args.data)
    # Get peaks
    peaks = spacemed.find_peaks(absorption, w=150)
    time = numpy.array(time)
    absorption = numpy.array(absorption)
    # Calculate Heart Rate
    hr = spacemed.calc_heart_rate(time, peaks)
    # Plot it
    plt.plot(hr)
    plt.title("PPG-Derived Heart Rate Using Peak Detection")
    plt.xlabel("Time (s)")
    plt.ylabel("Heart Rate (bpm)")
    plt.grid(True)

    pyplot.savefig(args.output)  # only saving not actual plotting


def arg_parser():  # It produces a helper interface as seen on slides
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data", type=Path,
        help="the name of the input file")
    parser.add_argument(
        "-o", "--output", type=Path,  # Options denoted with a "-"
        help="write output to file")
    parser.add_argument(
        "--version", action="version",
        version=f'%(prog)s {__version__}')
    return parser


if __name__ == '__main__':  # checks to make sure it is run directly
    # and not imported? not entirely sure what  that means)
    main()
