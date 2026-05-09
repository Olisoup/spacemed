
"""
slice_activation.py
────────────────────────────
Generate a cross-correlation activation heat-map for one slice of an fMRI scan.

Usage
-----
    python spacemed_slice_activation.py <fmri_file> <slice_index> <output_file>

Example
-------
    python spacemed_slice_activation.py \
        ../data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii \
        25 \
        activation_slice25.png
"""

import numpy
import matplotlib
matplotlib.use("Agg")          # non-interactive backend so it works without a display
import matplotlib.pyplot as pyplot
import nibabel
import scipy.signal
import argparse


def normalise(data):
    """Z-score normalise a 1-D array; return zeros if std == 0."""
    if numpy.std(data) == 0:
        return numpy.zeros_like(data)
    return (data - numpy.mean(data)) / numpy.std(data)


def build_activation_map(fmri_file, slice_index, output_file):
    print(f"Loading: {fmri_file}")
    img  = nibabel.load(fmri_file)
    data = img.get_fdata()

    nt       = data.shape[-1]
    TR       = img.header.get_zooms()[-1]
    n_slices = data.shape[2]

    if not (0 <= slice_index < n_slices):
        raise ValueError(
            f"slice_index {slice_index} out of range (0 – {n_slices-1})."
        )

    print(f"Data shape : {data.shape} | TR = {TR} s | Slice z = {slice_index}")

    one_cycle = numpy.array([1]*5 + [0]*5)
    signal    = numpy.tile(one_cycle, int(numpy.ceil(nt/10)))[:nt]

    nx, ny   = data.shape[0], data.shape[1]
    corr_mat = numpy.zeros((nx, ny))

    print(f"Processing {nx * ny} voxels ...")
    for i in range(nx):
        for j in range(ny):
            ts       = data[i, j, slice_index]
            cross    = scipy.signal.correlate(normalise(ts),
                                              normalise(signal.astype(float)),
                                              mode="same")
            corr_mat[i, j] = numpy.max(cross)
    # ── 1. Brain mask ────────────────────────────────────────────────────────────
    # Voxels outside the brain have near-zero signal across all timepoints.
    # Taking the mean over time gives a simple intensity map — low mean = not brain.
    # We threshold at 10% of the maximum mean intensity.

    mean_signal = data[:, :, slice_index].mean()   # mean across time for each voxel 
    
    mean_signal = numpy.mean(data[:, :, slice_index, :], axis=-1)  # shape (nx, ny)

    brain_mask = mean_signal > (0.37* mean_signal.max())  # True = inside brain

    # Apply: zero out everything outside the brain
    corr_mat[~brain_mask] = 0

    # ── 2. Correlation threshold ──────────────────────────────────────────────────
    # Only keep voxels with a strong enough activation signal.
    # Tune this value — try between 5 and 15 to see what looks cleanest.

    threshold = 3.0
    corr_mat[corr_mat < threshold] = 0

    # ── Plot ──────────────────────────────────────────────────────────────────
    print("Done. Saving image ...")
    fig, ax = pyplot.subplots(figsize=(7, 6))
    im = ax.imshow(corr_mat.T, origin="lower", cmap="CMRmap", vmin=0)
    pyplot.colorbar(im, ax=ax, label="Peak cross-correlation")
    ax.set_title(f"fMRI Activation Map – Slice z = {slice_index}", fontsize=13)
    ax.set_xlabel("Voxel X")
    ax.set_ylabel("Voxel Y")
    pyplot.tight_layout()
    fig.savefig(output_file, dpi=150)
    print(f"Saved → {output_file}")


def main(args=None):
    parser = argparse.ArgumentParser(
        description="Cross-correlation fMRI activation map for one slice."
    )
    parser.add_argument("fmri_file",   help="Path to .nii fMRI file")
    parser.add_argument("slice_index", type=int, help="Z-slice index (0-based)")
    parser.add_argument("output_file", help="Output image path (e.g. out.png)")
    parsed = parser.parse_args(args)
    build_activation_map(parsed.fmri_file, parsed.slice_index, parsed.output_file)


if __name__ == "__main__":
    main()
