#mpiexec --use-hwthread-cpus python3 ring_tworings_comm_create.py
from mpi4py import MPI
to_right=201

world_size = MPI.COMM_WORLD.Get_size()
my_world_rank = MPI.COMM_WORLD.Get_rank()

rows, cols =(1,3)
ranges=[[0 for i in range(cols)] for j in range(rows)]

mycolor=my_world_rank > (world_size-1)/3
world_group=MPI.COMM_WORLD.Get_group()


if(mycolor==0):
    ranges[0][0]=0
    ranges[0][1]=(world_size-1)/3
else:
    ranges[0][0]= (world_size-1)/3+1
    ranges[0][1] = world_size-1

ranges[0][2]=1

sub_group=MPI.Group.Range_incl(world_group,ranges)
sub_comm = MPI.COMM_WORLD.Create(sub_group)
sub_size = sub_comm.Get_size()
my_sub_rank=sub_comm.Get_rank()

right = (my_sub_rank+1)          % sub_size
left  = (my_sub_rank-1+sub_size) % sub_size

sumA=0
snd_buf=my_world_rank
for counter in range(0,sub_size):
    request=sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=sub_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sumA = sumA + rcv_buf

sumB=0
snd_buf=my_sub_rank

for counter in range(0,sub_size):
    request=sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=sub_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sumB = sumB + rcv_buf

print('PE world:',my_world_rank,'color = ',mycolor,'sub: ',my_sub_rank,'sumA = ', sumA, 'sumB',sumB)
