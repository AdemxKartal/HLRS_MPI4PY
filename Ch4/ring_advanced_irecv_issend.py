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

arr_request=[]
recv_status=MPI.Status()
status1=MPI.Status()
status2=MPI.Status()
arr_status = [status1,status2]


sum = 0
snd_buf = my_rank
recv_buf=None
for counter in range(0,size):
    recv=MPI.COMM_WORLD.irecv(source=left, tag =to_right)
    arr_request.append(recv)
    req=MPI.COMM_WORLD.isend(obj=snd_buf,dest=right,tag=to_right)
    arr_request.append(req)
    recv_buf=recv.wait()
    MPI.Request.waitall(requests=arr_request,statuses=arr_status)
    snd_buf=recv_buf
    snd_buf=recv_buf
    sum = sum + recv_buf

print('my_rank:',my_rank,'Sum=',sum)

