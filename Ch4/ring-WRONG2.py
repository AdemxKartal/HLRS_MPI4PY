#run with: mpiexec -n 2 python3 ring.py
#mpiexec --use-hwthread-cpus python3 ring.py

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()



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
    req=MPI.COMM_WORLD.send(obj=snd_buf,dest=right,tag=17)
    #WRONG programm, because if MPI_Send is implemented with a synchronous communication protocol then this programm will be deadlock!!!
    recv_buf=MPI.COMM_WORLD.recv(source=left, tag =17, status=status)
    #// buffer = bufer --> With only one buffer , one does not need this step
    snd_buf=recv_buf
    sum = sum + recv_buf

print('my_rank:',my_rank,'Sum=',sum)

