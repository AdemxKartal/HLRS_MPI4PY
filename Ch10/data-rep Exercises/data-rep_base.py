#run with: mpiexec -n 2 python3 data-rep_base.py
#mpiexec --use-hwthread-cpus python3 data-rep_base.py

from mpi4py import MPI
import numpy as np
size_world = MPI.COMM_WORLD.Get_size()
rank_world = MPI.COMM_WORLD.Get_rank()
arrSize = int(16*1.6E7)

sizeArrType = 8

arr= np.zeros(arrSize,dtype='int32')


for it in range(0,3):
    if(rank_world==0):
        for counter2 in range(0,arrSize):
            arr[counter2] = it+counter2
    arr=MPI.COMM_WORLD.bcast(obj=arr,root=0)
    sum = 0
    for counter3 in range(0,arrSize):
        sum=sum+arr[counter3]
    print('it: ', it,' rank (world): ',rank_world,' sum from', it,'to ', arrSize-1+it, ' sum = ',sum)
