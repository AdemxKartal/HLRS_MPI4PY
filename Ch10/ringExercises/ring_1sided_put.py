#run with: mpiexec -n 2 python3 ring_1sided_put.py
#mpiexec --use-hwthread-cpus python3 ring_1sided_put.py
from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
sizeOfInt = 4

right = (my_rank+1)%size
left=(my_rank-1+size)%size

rcv_buf=np.zeros(sizeOfInt,dtype='int')
snd_buf=np.zeros(sizeOfInt,dtype='int')
win=MPI.Win.Create(rcv_buf,disp_unit=sizeOfInt, comm=MPI.COMM_WORLD)

#Create(type cls, memory, int disp_unit=1, Info info=INFO_NULL, Intracomm comm=COMM_SELF)
sum = 0
#Win.Put(self, origin, int target_rank, target=None)
for counter in range(0,size):
    win.Fence(MPI.MODE_NOSTORE|MPI.MODE_NOPRECEDE)
    win.Put(snd_buf,right,None)
    win.Fence(MPI.MODE_NOSTORE|MPI.MODE_NOPUT|MPI.MODE_NOSUCCEED)
    snd_buf=rcv_buf
    sum= snd_buf+rcv_buf
print('my_rank:',my_rank,'Sum=',sum)
