#!/bin/bash
#SBATCH --qos=regular
#SBATCH --time=48:00:00
#SBATCH --nodes=37
#SBATCH --tasks-per-node=32
#SBATCH --constraint=haswell
#SBATCH --mail-user=yupinglu89@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --job-name=TESTRUN

cd $SLURM_SUBMIT_DIR
echo Working directory is : $SLURM_SUBMIT_DIR

echo $SLURM_JOB_NODELIST
echo $SLURM_JOBID
echo $SLURM_NPROCS

NCPUS=$SLURM_NPROCS
JobID=$SLURM_JOBID

mkdir Dir_$JobID
cd Dir_$JobID

echo "Start parallel job with CPUS"
echo $NCPUS
echo " -----------------------------------------------"

#module purge
#module load PrgEnv-gnu
#module load openmpi
#module load gsl
EXEC="../testrun"

mpirun -v -np 1161 $EXEC >$SLURM_SUBMIT_DIR/stdout_$JobID.out 2>$SLURM_SUBMIT_DIR/stderr_$JobID.out

mv ../*$JobID.out ../slurm-*.out ../Dir_$JobID/

### END of job
echo "Job complete"
