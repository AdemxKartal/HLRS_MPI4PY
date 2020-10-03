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
# this SPMD-Sytle neighbor computation with modulo has the same meaning as:
# right = my_rank+1
# if(right == size):
#   right = 0
# left = my_rank - 1
#if (left == -1):
#   left = size - 1
rcv_buf=10 #should be overitten, just for test
rcv_buf=np.zeros(10,dtype='int')
win=MPI.Win.Create(rcv_buf,disp_unit=sizeOfInt, comm=MPI.COMM_WORLD)
grp_world=MPI.COMM_WORLD.Get_group()
grp_left= MPI.Group.Incl(grp_world,left)
grp_right=MPI.Group.Incl(grp_world,right)
MPI.Group.Free(grp_world)

sum = 0
snd_buf = my_rank
for counter in range(0,size):
    #int MPI_Win_post(MPI_Group group, int assert, MPI_Win win)
    MPI.win.Post(win,grp_left,MPI.MODE_NOSTORE)


print('my_rank:',my_rank,'Sum=',sum)

