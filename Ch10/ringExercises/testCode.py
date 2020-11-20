#run with: mpiexec -n 2 python3 testCode.py

from mpi4py import MPI
import numpy as np
import inspect
sizeOfInt = 4
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
#rcv_buf=np.zeros(sizeOfInt,dtype='int')
snd_buf=np.zeros(1,dtype='int')
snd_buf[0]=10

if(my_rank==0):
    help(MPI.Alloc_mem)
    #help(MPI.Win.Put)

