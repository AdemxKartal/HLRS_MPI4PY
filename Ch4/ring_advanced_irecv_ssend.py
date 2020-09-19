from mpi4py import MPI
#run with: mpiexec -n 2 python3 ring.py
#mpiexec --use-hwthread-cpus python3 ring_advanced_irecv_issend.py
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

sum = 0
snd_buf = my_rank

for counter in range(0,size):
    status = MPI.Status()
    recv=MPI.COMM_WORLD.irecv(source=left, tag =to_right)
    MPI.COMM_WORLD.ssend(obj=snd_buf,dest=right,tag=to_right)
    recv_buf=recv.wait()
    snd_buf=recv_buf
    sum = sum + recv_buf

print('my_rank:',my_rank,'Sum=',sum)

