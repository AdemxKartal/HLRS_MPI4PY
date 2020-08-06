#run with: mpiexec -n 2 python testCode.py
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
status = MPI.Status()
to_right = 201
sum= int()

rcv_buf=my_rank
snd_buffer=my_rank
buffer= int()

for counter in range(0,size):
    req= MPI.COMM_WORLD.Send([buffer,MPI.INT], dest= right, tag=to_right)
    print('test print')
    ret_rcv=MPI.COMM_WORLD.Recv([buffer,MPI.INT], source= left, tag=to_right,status=status)
    #ret_rcv=MPI.COMM_WORLD.Recv([rcv_buf,MPI.INT], source= left, tag=to_right,status=status)
    #print('type of ret_recv: ', type(ret_rcv), 'value of ret_rcv: ', ret_rcv)
    #snd_buffer=ret_rcv
    #print('rcv_buf: ', rcv_buf)

