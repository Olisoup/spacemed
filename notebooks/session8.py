# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:.conda-spacemed26]
#     language: python
#     name: conda-env-.conda-spacemed26-py
# ---

# %% [markdown]
# # Session 8 Notebook - Multi-Dimensional Data

# %%
from matplotlib import pyplot
import seaborn
import pandas
import nibabel
import scipy.signal
import numpy
import spacemed

# %%
# !pwd

# %%
anatomy = nibabel.load("../data/fmri-data/2_Anatomy_1mm_5min.nii")

# %%
print(anatomy.header) # Metadata of the dataset

# %%
print(anatomy.shape) # Size of the dataset (no of slices)

# %%
print(anatomy.header.get_zooms()) # Voxel sizes (scanner left-right; scanner floor-ceiling; scanner bore)

# %% [markdown]
# [coordinate system](https://nipy.org/nibabel/coordinate_systems.html)

# %%
data_anatomy = anatomy.get_fdata() 

# %%
fig, axes = pyplot.subplots(1)
axes.imshow(data_anatomy[120, :, :].T,
origin="lower",
cmap="Pastel1")

#Change indices, change position --> [frontal, horizontal, sagittal]

#'.T' transposes to rows and columns, origin = "lower" places the origin in the bottom left, convention in neuroimaging

# %%
print(anatomy.affine) # When comparing datasets --> transform one to the coordinate system of the other via rotation and translation). ".affine" finds the transformation matrix

# %%
ols = pandas.read_csv("../data/ols.csv") # Orbital Launch System data

# %% [markdown]
# [Seaborn](https://seaborn.pydata.org/) is a visualization library. Does nice plots essentially, still need to run stats separately. 

# %%
ols

# %%
seaborn.regplot(ols,
                x="Initial Mass (kg)",
                y="Payload Mass to LEO (kg)",
                order=1)

#"regplot" correlation visuals

# %%
seaborn.regplot(ols,
                x="Length (m)",
                y="Payload Mass to LEO (kg)",
                order=2)
# changing the order of a fit

# %% [markdown]
# ## fMRI
# **Objective** : Create image showing activated regions of the brain during fMRI (doing a cross correlation)

# %%
fmri = nibabel.load("../data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii")

# %%
fmri.shape

# %%
print(fmri.header.get_zooms())

# %%
nt = fmri.shape[-1] # nt is number of time samples, so 80 of them and 2s each

# %%
sampling_rate = fmri.header.get_zooms()[-1]

# %%
print(nt, sampling_rate) # 10 seconds on, followed by a period of 10s off

# %%
p1 = (19,24,25) # 3 points within the volume as seen previously (voxel coordinates)
p2 = (40,25,25)
p3 = (19,25,25)

# %%
fmri_data = fmri.get_fdata()

# %%
fmri_data[p1] # array with p1 across all the time series, since it's a point in a 4d environment

# %%
pyplot.plot(fmri_data[p1]) # Plotting a time series with all three points (raw output)
pyplot.plot(fmri_data[p2])
pyplot.plot(fmri_data[p3])

# %%
s_one = numpy.array([1]*5 + [0]*5) # creating the signal essentially, 10S [1] on and 10s [0] off, sampling rate every 2s, so 5 since 5*2=10

# %%
s_one

# %%
numpy.tile(s_one, 2) # running it twice essentially

# %%
signal = numpy.tile(s_one, int(numpy.ceil(nt/10))) # Since we need 80 samples, we need to modify the array to fit with the numpy.ceiling
signal = signal[:nt] # clip it at the end in the case of division problem

# %%
pyplot.plot(signal) # visualise


# %%
def normalise(data): # function to normalise the data from the 3 time series (subtracting the mean of curve from data, then dividing by standard deviation)
    norm = (data - numpy.mean(data)) # substract the mean from every curve and divide from SD which normalizes the amplitude
    norm = norm / numpy.std(data)
    return norm


# %%
pyplot.plot(normalise(fmri_data[p1]))  # plot normalised data
pyplot.plot(normalise(fmri_data[p2]))
pyplot.plot(normalise(fmri_data[p3]))

# %%
for p in [p1, p2, p3]: # Periodogram looks at power distribution across frequencies makes me think of FFT (you can see spikes in certain points)
    freq, power = scipy.signal.periodogram(normalise(fmri_data[p]), # Using for loop to do all 3 points
                                       fs=1/sampling_rate)
    pyplot.plot(freq, power)

# %% [markdown]
# Spike at 0.05 corresponds to our 20 second sampling setup (10s on and 10s off)

# %%
for p in [p1, p2, p3]: # find cross correlation for all points
    data = fmri_data[p]
    cross = scipy.signal.correlate(  #finding maximum for the cross correlation
        normalise(data), normalise(signal),
        mode="same")
    lags = scipy.signal.correlation_lags( # "interesting response" 8 seconds after stimulus, called lag here. Need to take into account
        len(data), len(signal),
        mode="same")
    pyplot.plot(lags, cross)
    c = numpy.max(cross)
    print(c) # c is cross correlation value

# %%
numpy.zeros(fmri.shape[:2]) # you have a loop storing stuff in this array, nested loop ? 

# %% [markdown]
# # Exercise
# 1. Add function to spacemed module that computes the
# cross correlation given the input signal and the fMRI
# output and a voxel index
#
# 2. Add program that computes the cross correlation for one
# slice and displays the data with command line arguments
# • name of fMRI file
# • the slice to process (an integer)
# • the name of the output image file

# %% [markdown]
# ## 1. Cross correlation function

# %%
spacemed.cross_corr(signal, fmri_data, p1)

# %%
spacemed.plot_cross_corr(*spacemed.cross_corr(signal, fmri_data, p1), p1)


# %% [markdown]
# ## 2 Cross correlation for a single slice program

# %%
# below is an in depth explanation of the program to generate the activation slice
# The  program itself is in the setup.cfg and runs in the console (just want to keep this here for reference)

def build_activation_map(fmri_file, slice_index, output_file):
    """
    Core computation: load fMRI data, build activation map, save image.

    This function contains all the science.  `main()` below is just the
    command-line wrapper that parses arguments and calls this function.

    Parameters
    ----------
    fmri_file   : str   – path to the NIfTI (.nii / .nii.gz) file
    slice_index : int   – which z-slice to process (0-based index)
    output_file : str   – filename for the saved PNG image

    Returns
    -------
    corr_mat : 2-D numpy array
        The activation map (peak cross-correlation per voxel).
    """

    # ── 1. Load the fMRI file ────────────────────────────────────────────────
    print(f"Loading: {fmri_file}")
    img  = nibabel.load(fmri_file)
    data = img.get_fdata()

    nt = data.shape[-1]              # number of time points
    TR = img.header.get_zooms()[-1]  # repetition time in seconds

    # Validate that the requested slice actually exists
    n_slices = data.shape[2]
    if not (0 <= slice_index < n_slices):
        raise ValueError(
            f"slice_index {slice_index} is out of range. "
            f"This file has {n_slices} slices (0 – {n_slices-1})."
        )

    print(f"Data shape : {data.shape}  (x, y, z, time)")
    print(f"TR = {TR} s   |   nt = {nt}   |   Processing slice z = {slice_index}")

    # ── 2. Build the stimulus signal ─────────────────────────────────────────
    # 10 s ON → 5 samples (at TR=2 s), 10 s OFF → 5 samples, repeated.
    # numpy.tile repeats the pattern; we clip to exactly nt.
    one_cycle = numpy.array([1] * 5 + [0] * 5)
    signal    = numpy.tile(one_cycle, int(numpy.ceil(nt / 10)))[:nt]

    # ── 3. Build the correlation matrix ──────────────────────────────────────
    # We create a 2-D array of zeros with the same (x, y) dimensions as the
    # fMRI data.  We will fill each cell with the peak cross-correlation of
    # the voxel at that (x, y) position in the chosen slice.

    nx, ny = data.shape[0], data.shape[1]
    corr_mat = numpy.zeros((nx, ny))

    print(f"Computing cross-correlation for {nx * ny} voxels ...")

    for i in range(nx):
        for j in range(ny):
            # Extract the time series for voxel (i, j, slice_index)
            ts = data[i, j, slice_index]

            # Normalise
            ts_norm  = normalise(ts)
            sig_norm = normalise(signal.astype(float))

            # Cross-correlate and store the peak value
            cross         = scipy.signal.correlate(ts_norm, sig_norm, mode="same")
            corr_mat[i,j] = numpy.max(cross)

    print("Done.")

    # ── 4. Plot and save the heat-map ─────────────────────────────────────────
    # .T  → transpose so that x runs left-right and y runs bottom-top
    # origin="lower" → neuroimaging convention: (0,0) at bottom-left
    # cmap="viridis"  → perceptually uniform colour map (colourblind-friendly)

    fig, ax = pyplot.subplots(figsize=(7, 6))

    im = ax.imshow(corr_mat.T, origin="lower", cmap="viridis")
    pyplot.colorbar(im, ax=ax, label="Peak cross-correlation (activation)")
    ax.set_title(f"fMRI Activation Map – Slice z = {slice_index}", fontsize=13)
    ax.set_xlabel("Voxel X")
    ax.set_ylabel("Voxel Y")

    # Save to disk (dpi=150 gives a crisp image without being huge)
    pyplot.tight_layout()
    fig.savefig(output_file, dpi=150)
    pyplot.show()
    print(f"Image saved → {output_file}")

    return corr_mat


# ── Command-line entry point ─────────────────────────────────────────────────
def main(args=None):
    """
    Parse command-line arguments and call build_activation_map().

    argparse handles:
      - printing a help message when you run the script with --help
      - converting the slice argument from a string to an integer
      - giving clear error messages when required arguments are missing

    Parameters
    ----------
    args : list of str, optional
        If None, reads from sys.argv (normal terminal use).
        Pass a list explicitly to call main() from inside a notebook or test.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Compute a cross-correlation activation heat-map for one fMRI slice.\n"
            "\n"
            "Example (terminal):\n"
            "  python spacemed_slice_activation.py "
            "../data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii 25 out.png"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Positional arguments (required, no flag needed)
    parser.add_argument(
        "fmri_file",
        help="Path to the NIfTI fMRI file (.nii or .nii.gz)"
    )
    parser.add_argument(
        "slice_index",
        type=int,            # argparse will convert the string "25" → integer 25
        help="Index of the z-slice to process (integer, 0-based)"
    )
    parser.add_argument(
        "output_file",
        help="Filename for the saved output image (e.g. activation.png)"
    )

    parsed = parser.parse_args(args)  # parse provided list, or sys.argv if None

    # Call the actual computation function with the parsed values
    build_activation_map(
        fmri_file   = parsed.fmri_file,
        slice_index = parsed.slice_index,
        output_file = parsed.output_file,
    )

print("Functions `build_activation_map` and `main` are defined and ready.")

# %%
# !pwd

# %%
# !sm_slice_activation ../../data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii 25 output.png 
# managed to add it to the setup.cfg and use it as a standalone program :)

# %%

# %%

# %%

# %%
