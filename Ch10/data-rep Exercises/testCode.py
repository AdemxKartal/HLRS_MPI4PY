#run with: mpiexec -n 2 python3 testCode.py
#mpiexec --use-hwthread-cpus python3 testCode.py

from mpi4py import MPI
import numpy as np
size_world = MPI.COMM_WORLD.Get_size()
rank_world = MPI.COMM_WORLD.Get_rank()
arrSize = 10
sizeArrType = 8

if rank_world==0:
    help(MPI.COMM_WORLD.Split)
