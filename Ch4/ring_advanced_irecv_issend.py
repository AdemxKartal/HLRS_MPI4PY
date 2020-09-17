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
arr_status=[]
arr_request=[]
status1=MPI.Status()
status2=MPI.Status()

arr_status.append(status1)
arr_status.append(status2)
sum = 0
snd_buf = 1

for counter in range(0,size):
    recv_buf=MPI.COMM_WORLD.irecv(source=left, tag =to_right)
    arr_request.append(recv_buf)
    req=MPI.COMM_WORLD.isend(obj=snd_buf,dest=right,tag=to_right)
    arr_request.append(req)
    req.waitall(requests=arr_request,statuses=arr_status)
    sum = sum + counter

print('my_rank:',my_rank,'Sum=',sum)

