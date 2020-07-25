from mpi4py import MPI
#--------------------------------------------------------------------------------------
#run with: mpiexec -n 2 python firstExample.py
#--------------------------------------------------------------------------------------


n = 1
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
if(my_rank ==0):
    n= input("enter the number of intervals (n): ")

n= MPI.COMM_WORLD.bcast(n,root=0)
result = 1*my_rank*n
print('here is my_rank: ', my_rank,'result = ', result)


