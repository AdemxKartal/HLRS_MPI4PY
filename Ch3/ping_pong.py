#run with: mpiexec -n 2 python ping_pong.py
from mpi4py import MPI
import numpy as np

#buffer = np.array([0.0,0.0],dtype=float)
buffer= np.arange(1000,dtype='i')
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
for counter in range(0,number_of_messages):
    if(rank==proc_A):
        #MPI.Comm.Send(buffer, dest= proc_B, tag=ping)
        MPI.Comm.Send([buffer,MPI.INT], dest= proc_B, tag=ping)
        MPI.Comm.Recv([buffer,MPI.INT],dest=proc_B,tag=pong,status=status)
        #MPI.Comm.Recv(buf=buffer,dest=proc_B,tag=pong,status=status)
        #MPI.Comm.Send(buffer,proc_B,ping)
        #MPI.Comm.Recv(buffer,proc_B,pong,status)
    elif(rank==proc_B):
        #MPI.Comm.Send(buffer=buffer,dest=proc_A,tag=pong)
        #MPI.Comm.Recv(buffer=buffer,dest=proc_A,tag=ping)
        MPI.Comm.Send([buffer,MPI.INT],dest=proc_A,tag=pong)
        MPI.Comm.Recv([buffer,MPI.INT],dest=proc_A,tag=ping)
        #MPI.Comm.Send(buffer,proc_A,pong)
        #MPI.Comm.Recv(buffer,proc_A,ping)
finish =MPI.Wtime()
if(rank==proc_A):
    time = finish-start
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))

