#mpiexec -n 2 python3 testCode.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
if(my_rank==1):
    help(MPI.COMM_WORLD.iprobe)
    help(MPI.COMM_WORLD.Iprobe)
    #help(MPI.COMM_WORLD.issend)
    #print(help(MPI.Intracomm.scan))
    #print(type(MPI.Intracomm.scan))
    #help(MPI.COMM_WORLD.allreduce)
