#run with: mpiexec -n 2 python3 testCode.py

from mpi4py import MPI
import numpy as np

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()

if(my_rank==0):
    help(MPI.Win.Post)

