#mpiexec -n 2 python3 allreduce.py
#mpiexec --use-hwthread-cpus python3 allreduce.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()



summe=MPI.COMM_WORLD.allreduce(sendobj=my_rank, op=MPI.SUM)

print('PE',my_rank,' :','sum =  ',summe)
