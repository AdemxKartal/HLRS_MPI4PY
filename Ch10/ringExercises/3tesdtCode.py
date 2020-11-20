#run with: mpiexec -n 2 python3 ring_1sided_put.py
#mpiexec --use-hwthread-cpus python3 ring_1sided_put.py
from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
sizeOfInt = 4
sizeOfMemory = np.zeros(sizeOfInt, dtype='int')

right = (my_rank+1)%size
left=(my_rank-1+size)%size
memory=MPI.Alloc_mem(sizeOfInt,MPI.INFO_NULL)
rcv_buf=np.zeros(1,dtype='int') # is that okay? window size just one
snd_buf=np.zeros(1,dtype='int')


comm_shm=MPI.COMM_WORLD.Split_type(split_type=MPI.COMM_TYPE_SHARED,key=0,info=MPI.INFO_NULL)
size_shm = comm_shm.Get_size()
if(size_shm!=size):
    print('Not on one shared memory node ')
    MPI.COMM_WORLD.Abort(errorcode=0)


win=MPI.Win.Allocate_shared(size=sizeOfInt,disp_unit=sizeOfInt,info=MPI.INFO_NULL)
print('win: ', win, 'type of win: ', type(win))