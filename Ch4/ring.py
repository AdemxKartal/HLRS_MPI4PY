from mpi4py import MPI
#run with: mpiexec -n 2 python ring.py

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
snd_buf = 1

status = MPI.Status()
for counter in range(0,size):
    req=MPI.COMM_WORLD.isend(snd_buf,dest=right,tag=to_right)
    #req=MPI.COMM_WORLD.Isend([snd_buf, MPI.BYTE],dest=right,tag=to_right)
    MPI.COMM_WORLD.recv(source=left, tag =to_right, status=status)
    req.Wait()
    snd_buf = snd_buf+1
    sum = sum +snd_buf

print('my_rank:',my_rank,'Sum=',sum)
