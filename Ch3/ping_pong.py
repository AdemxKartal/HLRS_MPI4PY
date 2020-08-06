#run with: mpiexec -n 2 python ping_pong.py
from mpi4py import MPI
import numpy as np

buffer= np.array([1,2],dtype='f')

proc_A = 0
proc_B = 1
ping=17
pong=23
length_of_message=1
number_of_messages = 50
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
start = MPI.Wtime()
status = MPI.Status()


for counter in range(0,number_of_messages):
    if(my_rank ==proc_A):
        MPI.COMM_WORLD.Send([buffer,MPI.FLOAT], dest= proc_B, tag=ping)
        MPI.COMM_WORLD.Recv([buffer,MPI.FLOAT], source= proc_B, tag=pong,status=status)

    elif(my_rank ==proc_B):
        MPI.COMM_WORLD.Recv([buffer,MPI.FLOAT],source=proc_A,tag=ping,status=status)
        MPI.COMM_WORLD.Send([buffer,MPI.FLOAT],dest=proc_A,tag=pong)


finish =MPI.Wtime()

if(my_rank ==proc_A):
    time = finish-start
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))

