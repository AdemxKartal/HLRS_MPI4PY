#run with: mpiexec -n 2 python ping_pong_advanced1.py
from mpi4py import MPI
buffer= 1
proc_A = 0
proc_B = 1
ping=17
pong=23
length_of_message=1
number_of_messages = 50
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status = MPI.Status()


if(my_rank ==proc_A):
        MPI.COMM_WORLD.send(buffer, dest= proc_B, tag=ping)
        MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)

elif(my_rank ==proc_B):
        MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
        MPI.COMM_WORLD.send(buffer,dest=proc_A,tag=pong)

start = MPI.Wtime()

for counter in range(0,number_of_messages):
    if(my_rank==proc_A):
        MPI.COMM_WORLD.send(buffer, dest= proc_B, tag=ping)
        MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)

    elif(my_rank==proc_B):
        MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
        MPI.COMM_WORLD.send(buffer,dest=proc_A,tag=pong)

finish =MPI.Wtime()
if(my_rank==proc_A):
    time = finish-start
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))

