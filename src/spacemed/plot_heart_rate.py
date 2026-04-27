# Plotting PPG

from pathlib import Path
from matplotlib import pyplot
from . import load_pulse
from . import find_peaks
from . import calc_heart_rate
def main():
  indata = Path("data/pulse_data.csv") # Name of input file
  outname = Path("heart_rate.pdf") # Name of output file

  pyplot.savefig(outname) # only saving not actual plotting

if __name__ == '__main__': # checks to make sure it is run directly and not imported? (not entirely sure what  that means)
  main()
