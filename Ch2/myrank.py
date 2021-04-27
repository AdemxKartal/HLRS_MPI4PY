from mpi4py import MPI
#run with: mpiexec -n 2 python myrank.py

rank = MPI.COMM_WORLD.Get_rank()
print("Hello World! I am process: ",rank)

