#mpiexec --use-hwthread-cpus python3 ring_intercomm.py
from mpi4py import MPI
status = MPI.Status()
to_right=201

world_size = MPI.COMM_WORLD.Get_size()
my_world_rank = MPI.COMM_WORLD.Get_rank()
#status= MPI.Status()

mycolor=my_world_rank > (world_size-1)/3
#if(my_world_rank > (world_size-1)/3):
#    mycolor=0
#else:
 #   mycolor=1

sub_comm= MPI.COMM_WORLD.Split(color=mycolor, key=0)
sub_size = sub_comm.Get_size()
my_sub_rank=sub_comm.Get_rank()

right = (my_sub_rank+1)          % sub_size
left  = (my_sub_rank-1+sub_size) % sub_size

snd_buf= my_world_rank
sumA = 0

for counter in range(0,sub_size):
    request=sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=sub_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sumA= sumA+rcv_buf

sumB=0
snd_buf=my_sub_rank

for counter in range(0,sub_size):
    request=sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=sub_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sumB= sumB+rcv_buf

if(mycolor==0):
    remote_leader = 0+sub_size
else:
    remote_leader = 0
#inter_comm=MPI.Intracomm.Create_intercomm(self=sub_comm,local_leader=0, peer_comm=MPI.COMM_WORLD,remote_leader=remote_leader,tag=0)
#inter_comm=sub_comm.Create_intercomm(0, MPI.COMM_WORLD,remote_leader,0)


#Create_intercomm=sub_comm.Create_intercomm
Create_intercomm=MPI.Intracomm.Create_intercomm
inter_comm= MPI.Intracomm.Create_intercomm(sub_comm,0,MPI.COMM_WORLD,remote_leader,0)
#intercomm= MPI.Intracomm.Create_intercomm(sub_comm,0,MPI.COMM_WORLD, remote_leader,0)
#Create_intercomm=MPI.Intracomm.Create_intercomm

#intercomm= Create_intercomm(sub_comm, 0,MPI.COMM_WORLD,remote_leader,0)
#inter_comm=MPI.Intracomm.Create_intercomm(sub_comm,0, MPI.COMM_WORLD,remote_leader,0)
#inter_comm=MPI.Intracomm.Create_intercomm()
#print('peer_comm type: ', type(MPI.COMM_WORLD),'---','remote_leader type: ', type(remote_leader))
#inter_comm=MPI.Intracomm.Create_intercomm(0,MPI.COMM_WORLD,remote_leader,0)



    #def Create_intercomm(self,
          #               int local_leader,
         #                Intracomm peer_comm,
        #                 int remote_leader,
       #                  int tag=0):
      #  """
     #   Create intercommunicator
    #    """
      #  cdef Intercomm comm = Intercomm.__new__(Intercomm)
     #   with nogil: CHKERR( MPI_Intercomm_create(
    #        self.ob_mpi, local_leader,
   #         peer_comm.ob_mpi, remote_leader,
  #          tag, &comm.ob_mpi) )
 #       comm_set_eh(comm.ob_mpi)
#





















my_inter_rank = inter_comm.Get_rank()
sumC=0
snd_buf=my_inter_rank

for counter in range(0,sub_size):
    request=sub_comm.issend(obj=snd_buf, dest=right,tag=to_right)
    rcv_buf=sub_comm.recv(source=left,tag=to_right)
    request.wait()
    snd_buf=rcv_buf
    sumC= sumC+rcv_buf

sumD=inter_comm.allreduce(sendobj=my_inter_rank, op=MPI.SUM)

print('PE world: ',my_world_rank,'color: ',mycolor,'sub: ',my_sub_rank, 'inter: ',my_inter_rank,'SumA: ', sumA,'sumB: ', sumB, 'sumC',sumC,'sumD', sumD)

