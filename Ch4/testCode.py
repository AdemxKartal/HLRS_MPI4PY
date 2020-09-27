#run with: mpiexec -n 2 python3 testCode.py
#run with: mpiexec --use-hwthread-cpus python testCode.py

from mpi4py import MPI
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()


right = (my_rank+1)%size
left=(my_rank-1+size)%size
#print('value of left: ',left)
#print('value of right: ', right)
status = MPI.Status()
to_right = 201
sum= 0

if(my_rank==1):
    help(MPI.COMM_WORLD.ssend)
    help(MPI.COMM_WORLD.issend)
    #help(MPI.COMM_WORLD.irecv)
