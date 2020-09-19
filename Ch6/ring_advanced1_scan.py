#mpiexec -n 2 python3 ring_advanced1_scan.py
#mpiexec --use-hwthread-cpus python3 ring_advanced1_scan.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
sum=MPI.COMM_WORLD.scan(sendobj=my_rank,op=MPI.SUM,)
print('sum: ', sum)
token=None
if(my_rank!=0):
    token= MPI.COMM_WORLD.recv(source=my_rank-1,tag=tag_ready, status=status)
    print('PE: ',my_rank,'Sum = ',sum)

if(my_rank!=size-1):
    MPI.COMM_WORLD.send(obj=token,dest=my_rank+1,tag=tag_ready)
