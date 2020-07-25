#run with: mpiexec -n 2 python ping_pong.py
from mpi4py import MPI
import numpy as np

#buffer = np.array([0.0,0.0],dtype=float)
buffer= np.array([1,2,3],dtype='f')
#buffer = np.arange(4.)
proc_A = 0
proc_B = 1
ping=17
pong=23
length_of_message=1
number_of_messages = 50
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
start = MPI.Wtime()
status = MPI.Status()


#comm = MPI.COMM_WORLD
for counter in range(0,number_of_messages):
    if(rank==proc_A):
        MPI.COMM_WORLD.Send([buffer,MPI.FLOAT], dest= proc_B, tag=ping)
        MPI.COMM_WORLD.Recv([buffer,MPI.FLOAT], source= proc_B, tag=pong,status=status)

    elif(rank==proc_B):
        MPI.COMM_WORLD.Send([buffer,MPI.FLOAT],dest=proc_A,tag=pong)
        MPI.COMM_WORLD.Recv([buffer,MPI.FLOAT],source=proc_A,tag=ping,status=status)

finish =MPI.Wtime()
if(rank==proc_A):
    time = finish-start
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))
