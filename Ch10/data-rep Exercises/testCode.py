#run with: mpiexec -n 2 python3 data-rep_base.py
#mpiexec --use-hwthread-cpus python3 data-rep_base.py

from mpi4py import MPI
import numpy as np
size_world = MPI.COMM_WORLD.Get_size()
rank_world = MPI.COMM_WORLD.Get_rank()
arrSize = 10
sizeArrType = 8

arr= np.zeros(arrSize,dtype='int32')


#for it in range(0,3):
    #if(rank_world==0):
    #    for counter2 in range(0,arrSize):
   #         arr[counter2] = it+counter2
  #  MPI.COMM_WORLD.bcast(obj=arr,root=0)
 #   if(rank_world != 0):
#        print('my rank: ',rank_world,'arr: ', arr)

#for it in range(0,3):
#if rank_world==0:
    #for counter2 in range(0,arrSize):
      #  arr[counter2] = counter2
     #   print(arr)
    #MPI.COMM_WORLD.bcast(obj=arr,root=0)
#print('my rank: ', rank_world,'arr: ',arr)


if rank_world==0:
    arr[0] = 12

arr=MPI.COMM_WORLD.bcast(obj=arr,root=0)
print('my rank: ', rank_world,'arr: ',arr)
