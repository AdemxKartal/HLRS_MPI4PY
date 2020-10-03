#mpiexec --use-hwthread-cpus python3 ring_neighbor_alltoall.py


from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
max_dims=1

dims = [max_dims]
periods=[max_dims]
dims[0]=size
periods[0]=1
reorder = True

new_comm=MPI.Intracomm.Create_cart(MPI.COMM_WORLD,dims,periods,True)
my_rank= new_comm.Get_rank()
left_right= MPI.Cartcomm.Shift(new_comm,0,1)

left=left_right[0]
right=left_right[1]

sum=0
snd_buf=my_rank
rcv_buf=-1000 #unused value, should be overwritten, only for test purpose

for counter in range(0,size):
    MPI.Topocomm.Neighbor_alltoallw(new_comm,snd_buf,rcv_buf)
    snd_buf=rcv_buf
    sum=sum+rcv_buf

print('PE ', my_rank,'sum=',sum)
