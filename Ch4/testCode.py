#run with: mpiexec -n 2 python testCode.py
#run with: mpiexec --use-hwthread-cpus python testCode.py

from mpi4py import MPI
import numpy as np

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()


right = (my_rank+1)%size
left=(my_rank-1+size)%size
#print('value of left: ',left)
#print('value of right: ', right)
status = MPI.Status()
to_right = 201
sum= 0


buff = int()
#buf = 1
rcv_buf=2
buffer= int()



for counter in range(0,size):
    req=MPI.COMM_WORLD.isend(buff, dest= right, tag=to_right)
    #req=MPI.COMM_WORLD.Isend([buf,MPI.INT], dest= right, tag=to_right)
    MPI.COMM_WORLD.recv(buff, source= left, tag=to_right)
    #MPI.COMM_WORLD.Recv([buff,MPI.INT], source= left, tag=to_right)
    req.wait()
    sum= sum+1

print('sum of ranks: ', sum)

