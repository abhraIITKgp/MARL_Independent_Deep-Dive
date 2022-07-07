#!/bin/bash

# Lines that begin with #SBATCH specify commands to be used by SLURM for scheduling

#SBATCH --job-name=run_qmix                                   # sets the job name
#SBATCH --output=run_qmix.out                                 # indicates a file to redirect STDOUT to; %j is the jobid. Must be set to a file instead of a directory or else submission will fail.
#SBATCH --error=run_qmix.err                                  # indicates a file to redirect STDERR to; %j is the jobid. Must be set to a file instead of a directory or else submission will fail.
#SBATCH --time=05:00:00                                         # how long you think your job will take to complete; format=hh:mm:ss
#SBATCH --mem=1gb                                               # memory required by job; if unit is not specified MB will be assumed

cd /<directory where the program is run>/    # cd to directory where the program presents
source ~/.bashrc
conda activate <virtual-env>                 # start the virtual environment (I don't know which we'll be using)
python3 qmix.py --test --max_steps 10000 --max_episodes 1000 # command to run the program
wait                                         # must have at the end