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

sum = 0
snd_buf = my_rank
buf = snd_buf
for counter in range(0,size):
    req=MPI.COMM_WORLD.Isend([snd_buf,MPI.INT],dest=right,tag=to_right)
    MPI.COMM_WORLD.Recv([buf, MPI.INT], dest=left, tag =to_right)
    req.Wait()
    sum = sum +buf

print('my_rank:',my_rank,'Sum=',sum)
