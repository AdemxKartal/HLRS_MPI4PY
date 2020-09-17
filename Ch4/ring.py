#run with: mpiexec -n 2 python3 ring.py
#mpiexec --use-hwthread-cpus python3 ring.py

from mpi4py import MPI
status = MPI.Status()
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201


right = (my_rank+1)%size
left=(my_rank-1+size)%size
# this SPMD-Sytle neighbor computation with modulo has the same meaning as:
# right = my_rank+1
# if(right == size):
#   right = 0
# left = my_rank - 1
#if (left == -1):
#   left = size - 1


sum = 0 #sum of all ranks: my_rank has value of 0
snd_buf = my_rank
for counter in range(0,size):
    status = MPI.Status()
    req=MPI.COMM_WORLD.issend(obj=snd_buf,dest=right,tag=to_right)
    recv=MPI.COMM_WORLD.recv(source=left, tag =to_right, status=status)
    req.Wait()
    snd_buf=recv
    sum = sum + recv

print('my_rank:',my_rank,'Sum=',sum)

