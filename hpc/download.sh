#!/bin/bash
#SBATCH --mem=16G
#SBATCH --cpus-per-task=1
#SBATCH --time=95:00:00
#SBATCH --mail-user=s.sourbron@sheffield.ac.uk
#SBATCH --mail-type=FAIL,END
#SBATCH --job-name=t2s
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err

unset SLURM_CPU_BIND
export SLURM_EXPORT_ENV=ALL

module load Anaconda3/2024.02-1
module load Python/3.10.8-GCCcore-12.2.0 # essential to load latest GCC

# Get the current username
USERNAME=$(whoami)

# Define path variables here
ENV="/mnt/parscratch/users/$USERNAME/envs/t2star"
CODE="/mnt/parscratch/users/$USERNAME/scripts/iBEAt-t2star/src"
BUILD="/mnt/parscratch/users/$USERNAME/data/iBEAt_Build"
RESULTS="$BUILD/t2star"
ARCHIVE="/shared/abdominal_imaging/Archive/iBEAt_Build/t2star"
LOGIN_NODE="login1"

# Run and archive
srun "$ENV/bin/python" "$CODE/stage_1_download.py" --build="$BUILD"
rsync -av --no-group --no-perms --delete "$RESULTS/stage_1_download" "${LOGIN_NODE}:${ARCHIVE}"