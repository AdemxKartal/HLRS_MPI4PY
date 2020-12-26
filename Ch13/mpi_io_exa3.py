#run with: mpiexec -n 2 python3 mpi_io_exa3.py

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status=MPI.Status()
fh = MPI.File.Open(comm=MPI.COMM_WORLD, filename='my_test_file', amode= MPI.MODE_RDWR| MPI.MODE_CREATE, info = MPI.INFO_NULL)
offset = MPI.OFFSET
for counter in range (0,10):
    buf = str.encode('a'+str(my_rank))
    fh.Write_ordered(buf=[buf,1,MPI.BYTE], status=status)
fh.Close()
print(' PE: ', my_rank)