#mpiexec --use-hwthread-cpus python3 ring_neighbor_alltoall.py


from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
max_dims=1

dims = [max_dims]
periods=[max_dims]
snd_buf_arr=[]
dims[0]=size
periods[0]=1
reorder = True

new_comm=MPI.Intracomm.Create_cart(MPI.COMM_WORLD,dims,periods,True)
my_rank= new_comm.Get_rank()
left_right= MPI.Cartcomm.Shift(new_comm,0,1)

left=left_right[0]
right=left_right[1]

sum=0
snd_buf_arr.append(-1000-my_rank)
snd_buf_arr.append(100+my_rank)

for counter in range(0,size):
    rcv_buf_arr=MPI.Topocomm.neighbor_alltoall(new_comm,snd_buf_arr)
    snd_buf_arr[1]=rcv_buf_arr[0]
    sum=sum+rcv_buf_arr[0]


print('PE ', my_rank,'sum=',sum)
