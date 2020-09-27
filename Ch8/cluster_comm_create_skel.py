from mpi4py import MPI
to_right=201

world_size = MPI.COMM_WORLD.Get_size()
my_world_rank = MPI.COMM_WORLD.Get_rank()

