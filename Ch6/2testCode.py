from mpi4py import MPI
#run with: mpiexec -n 2 python ring.py
#mpiexec --use-hwthread-cpus python 2testCode.py

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


sum = 1 #sum of all ranks: my_rank has value of 0, so sum=1
snd_buf = 10
for counter in range(0,size-1):
    status = MPI.Status()
    req=MPI.COMM_WORLD.isend(snd_buf,dest=right,tag=to_right)
    recv=MPI.COMM_WORLD.recv(source=left, tag =to_right, status=status)
    if(my_rank==0):
        print('my_rank: ', my_rank)
        print('recv: ',recv)
    req.Wait()
    sum = sum + counter

#print('my_rank:',my_rank,'Sum=',sum)
