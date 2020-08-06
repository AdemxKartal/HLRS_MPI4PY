from mpi4py import MPI
#run with: mpiexec -n 2 python ring.py

status = MPI.Status()
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
snd_buf = int()
rcv_buf= int()

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
print('my rank: ', my_rank)
print(type)
##rcv_buf = snd_buf
for counter in range(0,size):
    #req=MPI.COMM_WORLD.Isend([snd_buf,MPI.INT],dest=right,tag=to_right)
    #rcv_buf = MPI.COMM_WORLD.Recv([rcv_buf, MPI.INT], source=left, tag =to_right)
    req=MPI.COMM_WORLD.Isend([snd_buf, MPI.BYTE],dest=right,tag=to_right)
    rcv_buf = MPI.COMM_WORLD.Recv([rcv_buf, MPI.BYTE], source=left, tag =to_right)
    print('-------------------------------------------------------------------------')
    print('rcv_buf: ', rcv_buf)
    print('--------------------------------------------------------------------------')
    #req.Wait()
    snd_buf = rcv_buf
    sum = sum +rcv_buf

print('my_rank:',my_rank,'Sum=',sum)
