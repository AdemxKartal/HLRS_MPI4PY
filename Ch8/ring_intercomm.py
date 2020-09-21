#mpiexec --use-hwthread-cpus python3 ring_tworings.py
from mpi4py import MPI
status = MPI.Status()
to_right=201
request = MPI.Request()
world_size = MPI.COMM_WORLD.Get_size()
my_world_rank = MPI.COMM_WORLD.Get_rank()
status= MPI.Status()
request=MPI.Request()

if(my_world_rank > (world_size-1)/3):
    mycolor=0
else:
    mycolor=1
print('mycolor: ',mycolor)
sub_comm= MPI.COMM_WORLD.Split(color=mycolor, key=0)
sub_size = sub_comm.Get_size()
my_sub_rank=sub_comm.Get_rank()

right = (my_sub_rank+1)          % sub_size
left  = (my_sub_rank-1+sub_size) % sub_size

snd_buf= my_world_rank
sumA = 0

for counter in range(0,sub_size):
    request=MPI.sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=MPI.sub_comm.recv(source=left,tag=to_right)
    request.wait()
    rcv_buf.wait()
    snd_buf=rcv_buf
    sumA= sumA+rcv_buf

sumB=0
snd_buf=my_sub_rank

for counter in range(0,sub_size):
    request=MPI.sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=MPI.sub_comm.recv(source=left,tag=to_right)
    request.wait()
    rcv_buf.wait()
    snd_buf=rcv_buf
    sumB= sumB+rcv_buf

if(mycolor==0):
    remote_leader = 0+sub_size
else:
    remote_leader = 0
inter_comm = MPI.Intracomm.Create_intercomm(local_leader=0, peer_comm=MPI.COMM_WORLD,remote_leader=remote_leader,tag=0)
my_inter_rank = inter_comm.Get_rank()

sumC=0
snd_buf=my_inter_rank

for counter in range(0,sub_size):
    request=MPI.sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=MPI.sub_comm.recv(source=left,tag=to_right)
    request.wait()
    rcv_buf.wait()
    snd_buf=rcv_buf
    sumC= sumC+rcv_buf

sumD=MPI.inter_comm.allreduce(sendobj=my_inter_rank, op=MPI.SUM)

print('PE world: ',my_world_rank,'color: ',mycolor,'sub: ',my_sub_rank, 'inter: ',my_inter_rank,'SumA: ', sumA,'sumB: ', sumB, 'sumC',sumC,'sumD', sumD)
#
