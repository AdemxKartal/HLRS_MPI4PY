#mpiexec -n 2 python ping_pong_advanced_send.py
from mpi4py import MPI
import sys

proc_A =0
proc_B=1
ping=17
pong=23

number_of_messages =50
length_of_message=8
length_faktor=64
max_length=2097152
number_package_sizes=4

buffer = 1
my_rank = MPI.COMM_WORLD.Get_rank()
status = MPI.Status()

if (my_rank==proc_A):
    print('message size transfertime bandwith')

for counter in range(0,number_package_sizes):
    if(my_rank ==proc_A):
        MPI.COMM_WORLD.ssend(buffer, dest= proc_B, tag=ping)
        MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)

    elif(my_rank ==proc_B):
            MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
            MPI.COMM_WORLD.ssend(buffer,dest=proc_A,tag=pong)

    start = MPI.Wtime()
    for counter2 in range(0,number_of_messages):
        if(my_rank==proc_A):
            MPI.COMM_WORLD.ssend(buffer, dest= proc_B, tag=ping)
            MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)

        elif(my_rank==proc_B):
            MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
            MPI.COMM_WORLD.ssend(buffer,dest=proc_A,tag=pong)
finish =MPI.Wtime()
if(my_rank==proc_A):
    time = finish-start
    transfer_time= time/ (2*number_of_messages)
    sendbytes = length_of_message*sys.getsizeof(buffer)
    usec = transfer_time*1e6
    mb_per_second= 1.0e-6*length_of_message*sys.getsizeof(buffer)
    print('bytes: ',sendbytes,'usec: ', usec, ' ',mb_per_second, 'MB/s')
    print('time for one messsage: ',(time/(2*number_of_messages)*1e6))
