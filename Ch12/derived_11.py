#run with: mpiexec -n 2 python3 ring.py
#mpiexec --use-hwthread-cpus python3 ring.py

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201



