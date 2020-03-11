#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=00:20:00
#SBATCH --nodes=2
#SBATCH --tasks-per-node=32
#SBATCH --constraint=haswell
#SBATCH --mail-user=yupinglu89@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --job-name=TESTRUN

#module purge
#module load PrgEnv-gnu
#module load openmpi
#module load gsl

srun -N 1 -n 32 ./testrun >stdout_1.out 2>tderr_1.out &
srun -N 1 -n 32 ./testrun >stdout_2.out 2>stderr_2.out &
wait