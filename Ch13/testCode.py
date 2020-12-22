#run with: mpiexec -n 2 python3 testCode.py
#wxb4PdTF7CH8Ftd
from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status=MPI.Status()

for counter in range (0,10):
    #buf = '0' + str(my_rank).encode()
    buf = str.encode('0'+str(my_rank))
    print('buf = ', buf, 'type buf: ', type(buf))
    ##buf = 0+my_rank

print(' PE: ', my_rank)