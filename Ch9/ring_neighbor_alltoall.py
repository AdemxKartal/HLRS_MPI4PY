from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
max_dims=1

dims = [max_dims]
periods=[max_dims]

dims[0]=size
periods[0]=1
reorder =1

