#mpiexec -n 2 python3 testCode.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
x = 1
y = not x
z= (0)
thistuple=("apple","banana")
#if(my_rank==1):
    #help(MPI.COMM_WORLD.reduce)

if(my_rank==1):
    help(MPI.COMM_WORLD.scan)














# reduce


#comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()

#senddata = 1
#recvdata = comm.reduce(senddata,root=0,op=MPI.SUM)
#print ('',rank,type(senddata),type(recvdata))
#print ('on task',rank,'after reduce:    data = ',recvdata)




