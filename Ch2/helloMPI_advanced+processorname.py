from mpi4py import MPI
#run with: mpiexec -n 2 python helloMPI_advanced+processorname.py


size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
nameProcessor = MPI.Get_processor_name()

print("Hello World! I am process:",rank,'out of',size,'on',nameProcessor)

