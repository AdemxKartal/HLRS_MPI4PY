#mpiexec -n 2 python ring_advanced1_scan.py

from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
token =1
summe=0
#scanner=MPI.Intracomm.scan(sendobj=10,op=MPI.SUM())
MPI.Intracomm.scan(sendobj=10,op=MPI.SUM)


if(my_rank!=0):
    MPI.COMM_WORLD.recv(source=my_rank-1,tag=tag_ready, status=status)
print('PE: ', my_rank,' Sum: ',summe)

if(my_rank!=size-1):
    MPI.COMM_WORLD.send(obj=token,dest=my_rank+1,tag=tag_ready)
