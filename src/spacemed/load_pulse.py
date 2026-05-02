def read_pulse(fname):
    time = []
    absorption = []
    dataFile = open(fname)

    dataFile.readline()

    for line in dataFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption
