#run with: mpiexec -n 2 python ping.py
# mpiexec --use-hwthread-cpus python3 ping.py

from mpi4py import MPI
buffer= 1
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
start = MPI.Wtime()
status = MPI.Status()


if(my_rank ==0):
        print("I am ", my_rank, "before sending ping")
        MPI.COMM_WORLD.send(buffer, dest= 1, tag=17)

elif(my_rank ==1):

        MPI.COMM_WORLD.send(buffer,dest=0,tag=17)
        print("I am ", my_rank, "after recv pong")

finish =MPI.Wtime()
