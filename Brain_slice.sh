#!/bin/bash
#SBATCH --job-name="Array Job"
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00
#SBATCH --array=0-31


# the program we are running
pwd
source /etc/profile.d/conda.sh
conda activate spacemed26
sm_slice_activation olso13/data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii ${SLURM_ARRAY_TASK_ID} output_${SLURM_ARRAY_TASK_ID}.png
