#run with: mpiexec -n 2 python3 testCode.py

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
max_dims=1

if(my_rank==0):
    help(MPI.Cartcomm.Shift)
    help(MPI.Topocomm.Neighbor_alltoall)
