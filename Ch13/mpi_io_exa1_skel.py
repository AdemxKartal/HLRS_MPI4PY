#run with: mpiexec -n 2 python3 mpi_io_exa1_skel.py

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status=MPI.Status()
fh = MPI.File.Open(comm=MPI.COMM_WORLD, filename='my_test_file', amode= MPI.MODE_RDWR| MPI.MODE_CREATE, info = MPI.INFO_NULL)
offset = _______
for counter in range (0,10):
    buf = str.encode('0'+str(my_rank))
    print('buf = ', buf, 'my_rank = ', my_rank)
    offset= _______
    fh.Write_at(offset=offset, buf=[buf,___,___], status=status)
fh.Close()
print(' PE: ', my_rank)