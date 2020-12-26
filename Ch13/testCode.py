#run with: mpiexec -n 2 python3 mpi_io_exa2.py

from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
status=MPI.Status()
order=MPI.ORDER_C
etype = MPI.CHAR
ndims=1



array_of_sizes = np.zeros(2,dtype='int')
array_of_subsizes = np.zeros(2,dtype='int')
array_of_starts =np.zeros(2,dtype='int')

array_of_sizes[0] = size
array_of_subsizes[0]=1
array_of_starts[0]=my_rank

array_of_sizes[1]=1
array_of_subsizes[1]=1
array_of_starts[1]=1

#filetype=etype.Create_subarray(sizes=array_of_sizes, subsizes=array_of_subsizes,starts=array_of_starts,order=order)
#filetype=etype.Create_subarray(sizes=[size,1,MPI.INT], subsizes=[1,1,MPI.INT], starts=[my_rank,1,MPI.INT], order=order)
#filetype=etype.Create_subarray(sizes=size, subsizes=1, starts=my_rank, order=order)
filetype=etype.Create_subarray(sizes=size, subsizes=1, starts=my_rank, order=order)
#filetype=MPI.Commit(filetype)