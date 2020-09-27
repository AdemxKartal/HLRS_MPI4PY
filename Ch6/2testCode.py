from mpi4py import MPI
#run with: mpiexec -n 2 python3 2testCode.py
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

ib_finished=0
sum = 1 #sum of all ranks: my_rank has value of 0, so sum=1
snd_buf = 10
for counter in range(0,size-1):
    status = MPI.Status()
    req=MPI.COMM_WORLD.isend(snd_buf,dest=right,tag=to_right)
    recv1=MPI.COMM_WORLD.recv(source=left, tag =to_right, status=status)
    #recv2=MPI.COMM_WORLD.recv(source=left, tag =to_right, status=status)
    rcv_flag = MPI.COMM_WORLD.iprobe(source=MPI.ANY_SOURCE,tag=to_right,status=None)
    snd_finished= MPI.Request.testall(request=[recv1],status=None)
    #print(snd_finished)
    #if(rcv_flag):
    help(MPI.Request.testall)
        #print('rcv_flag: ',rcv_flag,'from source: ', status.source)
    #print('type of ib_finished[0] ', type(ib_finished[0]), 'value of ib_finished[0]: ', ib_finished[0])
        #print('recv: ',recv, 'status',status.Get_source())
        #print('statusss: ', status.source)
    req.Wait()
    sum = sum + counter

#print('my_rank:',my_rank,'Sum=',sum)
