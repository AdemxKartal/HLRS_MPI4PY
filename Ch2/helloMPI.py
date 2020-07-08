from mpi4py import MPI
#run with: mpiexec -n 2 python helloMPI.py

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
print("Hello World! here is rank: ",rank)

