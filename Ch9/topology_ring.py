#mpiexec --use-hwthread-cpus python3 topology_ring.py


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

new_comm=MPI.Intracomm.Create_cart(MPI.COMM_WORLD,dims,periods,reorder)
my_rank= new_comm.Get_rank()
left_right= MPI.Cartcomm.Shift(new_comm,0,1)

left=left_right[0]
right=left_right[1]

sum=0
snd_buf=my_rank
for counter in range(0,size):
    request=new_comm.issend(obj=snd_buf,dest=right,tag=to_right)
    rcv_buf=new_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sum=sum+rcv_buf

print('PE ', my_rank,'sum=',sum)
