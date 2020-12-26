#run with: mpiexec -n 2 python3 mpi_io_exa2.py

#https://programmersought.com/article/7946705288/
from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status=MPI.Status()
array_of_sizes = np.zeros(2,dtype='int')
array_of_subsizes = np.zeros(2,dtype='int')
array_of_starts =np.zeros(2,dtype='int')
etype = MPI.CHAR
ndims=1

array_of_starts[0]= size
array_of_subsizes=1
array_of_starts[0]=my_rank
order=MPI.ORDER_C
filetype=MPI.Datatype.Create_subarray(sizes=array_of_sizes, subsizes=array_of_subsizes,starts=array_of_starts,order=order)
filetype=MPI.Commit(filetype)

fh= MPI.File.Open(comm=MPI.COMM_WORLD, filename='my_test_file', amode=MPI.MODE_RDWR|MPI.MODE_CREATE, info=MPI.INFO_NULL)
disp=0
fh.Set_view(disp=disp, etype=etype, filetype=filetype, datarep='native',info=MPI.INFO_NULL)

for counter in range(0,3):
    buf=str.encode('a'+str(my_rank))
    fh.Write([buf,1,etype],status=status)
fh.Close()
print(' PE: ', my_rank)