#run with: mpiexec -n 2 python ping_pong.py
# mpiexec --use-hwthread-cpus python3 ping_pong.py

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
start = MPI.Wtime()
status = MPI.Status()


for counter in range(0,number_of_messages):
    if(my_rank ==proc_A):
        print("I am ", my_rank, "before sending ping")
        MPI.COMM_WORLD.send(buffer, dest= proc_B, tag=ping)
        MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)
        print("I am ", my_rank, "after recv pong")
    elif(my_rank ==proc_B):
        print("I am ", my_rank, "before sending ping")
        MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
        MPI.COMM_WORLD.send(buffer,dest=proc_A,tag=pong)
        print("I am ", my_rank, "after recv pong")
finish =MPI.Wtime()

if(my_rank ==proc_A):
    time = finish-start
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))

