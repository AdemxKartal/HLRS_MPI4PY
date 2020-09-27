#mpiexec -n 2 python3 testCode.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
world_size = MPI.COMM_WORLD.Get_size()
my_world_rank = MPI.COMM_WORLD.Get_rank()

rows, cols =(1,3)
ranges=[[0 for i in range(cols)] for j in range(rows)]

if(my_world_rank==1):
    #help(MPI.Group.Range_incl)
    help(MPI.COMM_WORLD.Get_group)
    #help(MPI.Comm.Split)
    #help( MPI.COMM_WORLD.issend)
    #help(MPI.COMM_WORLD.isend)
    #help(MPI.Intercomm.Create)
    #help(MPI.COMM_WORLD.Get_group)
