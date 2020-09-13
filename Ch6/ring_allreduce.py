#mpiexec -n 2 python3 ring_allreduce.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()

summe = 1 #default 1 because my_rank can be 0

summe=MPI.COMM_WORLD.allreduce(sendobj=my_rank, op=MPI.SUM)

print('PE',my_rank,' :','sum =  ',summe)
