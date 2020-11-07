#run with: mpiexec -n 2 python3 data-rep_base.py
#mpiexec --use-hwthread-cpus python3 data-rep_base.py

from mpi4py import MPI
import numpy as np
# --------------> 1 <-------------
size_world = MPI.COMM_WORLD.Get_size()
rank_world = MPI.COMM_WORLD.Get_rank()
#arrSize = int(16*1.6E7)
arrSize= 10 #just for testing on my computer
sizeArrType = 8
arr = np.zeros(arrSize, dtype='int32')
# --------------> 2 <-------------
comm_shm= MPI.COMM_WORLD.Split(color=MPI.COMM_TYPE_SHARED, key=0)
size_shm = comm_shm.Get_size()
rank_shm=comm_shm.Get_rank()

if(rank_shm==0):
    individualShmSize=arrSize
else:
    individualShmSize=0
win=MPI.Win.Allocate_shared(individualShmSize,sizeArrType,MPI.INFO_NULL,comm_shm)
sharedQuery= MPI.Win.Shared_query(win,0) #sharedQuery is a tuple: sharedQuery[0] = tomemory(base,size) arr[1] =disp_unit
#sharedQuery[0] = object
#sharedQuery[1]=disp_unit
disp_unit=sharedQuery[1]
if(rank_shm==0 or rank_shm==1 or rank_shm==size_shm-1 ):
    print('process: ',rank_world ,'arrSize: ',arrSize)

color = MPI.UNDEFINED
if(rank_shm==0):
    color=0

comm_head=MPI.COMM_WORLD.Split(color,0)
rank_head=-1
if(comm_head!=MPI.COMM_NULL):
    size_head = comm_head.Get_size()
    rank_head = comm_head.Get_rank()
mm=[]
#minmax=[]
mm.append(-size_shm)
mm.append(size_shm)

if(comm_head!=MPI.COMM_NULL):
    minmax=comm_head.reduce(mm,op=MPI.MAX,root=0)

if(rank_world==0):
    print('the number of shared memory island is: ', size_head,'island')
    if(minmax[0]+minmax[1]==0):
        print('size of all shared memory islands is: ', -minmax[0],'processes')
    else:
        print('the size of sharde memory island is between min = ',-minmax[0],'and max =',minmax[1])
#-------------------------> 3<----------------------------------------
for it in range(0,3):
    if(rank_world==0):

        for counter2 in range(0,arrSize):
            arr[counter2] = it+counter2
    # --------------> 4 <-------------
    if(comm_head!=MPI.COMM_NULL):
        arr=comm_head.bcast(obj=arr,root=0)
    #--------------->5<----------------
    win.Fence(0)
    sum=0
    for counter3 in range(0,arrSize):
        sum=sum+arr[counter3]
    #---------------->6<-----------------
    print('it: ', it,' rank (world): ',rank_world,'shm:',rank_shm,'head:',rank_head,' sum from', it,'to ', arrSize-+it, ' sum = ',sum)
