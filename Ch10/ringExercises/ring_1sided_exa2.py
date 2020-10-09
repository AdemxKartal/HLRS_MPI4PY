#run with: mpiexec -n 2 python3 ring_1sided_exa2.py
#mpiexec --use-hwthread-cpus python3 ring_1sided_exa2.py
from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
sizeOfInt = 4

right = (my_rank+1)%size
left=(my_rank-1+size)%size
left_ranks= [left]
right_ranks =[right]

#rcv_buf= [sizeOfInt]
#snd_buf=[sizeOfInt]
rcv_buf=np.zeros(sizeOfInt,dtype='int')
snd_buf=np.zeros(sizeOfInt,dtype='int')
win=MPI.Win.Create(rcv_buf,disp_unit=sizeOfInt, comm=MPI.COMM_WORLD)
print('rcv_buf: ', rcv_buf)
grp_world=MPI.COMM_WORLD.Get_group()
grp_left=MPI.Group.Incl(grp_world,left_ranks)
grp_right=MPI.Group.Incl(grp_world,right_ranks)
MPI.Group.Free(grp_world)

sum = 0
for counter in range(0,size):
    win.Post(grp_left,MPI.MODE_NOSTORE)
    win.Start(grp_right,0)
    win.Put(snd_buf,right,None)
    win.Complete()
    win.Wait()
    snd_buf=rcv_buf
    sum= sum + rcv_buf

print('my_rank:',my_rank,'Sum=',sum)
