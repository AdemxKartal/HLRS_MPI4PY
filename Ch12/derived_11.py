#run with: mpiexec -n 2 python3 ring.py
#mpiexec --use-hwthread-cpus python3 ring.py



from mpi4py import MPI
to_right = 201
COUNT = 2
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()


status = MPI.Status()
request = MPI.Request()
right = (my_rank+1)%size
left=(my_rank-1+size)%size

array_of_blocklengths= [COUNT]

array_of_blocklengths[0]=1
array_of_blocklengths[1]=1

int_snd_buf = my_rank

MPI.Get_adress(int_snd_buf)
