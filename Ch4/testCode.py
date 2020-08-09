#run with: mpiexec -n 2 python testCode.py
#run with: mpiexec --use-hwthread-cpus python testCode.py

from mpi4py import MPI
import numpy as np

snd_buffer= int()
rcv_buf=int()
my_rank =int()


proc_A = 0
proc_B = 1
ping=17
pong=23
length_of_message=1
number_of_messages = 50
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()


right = (my_rank+1)%size
left=(my_rank-1+size)%size
print('value of left: ',left)
print('value of right: ', right)
status = MPI.Status()
to_right = 201
sum= int()


buf = 1
rcv_buf=2




for counter in range(0,size):
    req=MPI.COMM_WORLD.isend(buf, dest= right, tag=to_right)

    MPI.COMM_WORLD.recv(rcv_buf, source= left, tag=to_right)
    req.wait()
    buf = rcv_buf
    sum= sum+rcv_buf

print('sum of ranks: ', sum)

