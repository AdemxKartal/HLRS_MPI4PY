from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
if(my_rank==1):
    print(help(MPI.Intracomm.scan))
    print(type(MPI.Intracomm.scan))
