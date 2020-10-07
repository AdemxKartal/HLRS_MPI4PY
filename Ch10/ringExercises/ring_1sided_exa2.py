#run with: mpiexec -n 2 python3 ring_1sided_exa2.py
#mpiexec --use-hwthread-cpus python3 ring_1sided_exa2.py
from mpi4py import MPI
import numpy as np
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
to_right =201
sizeOfInt = 4

right = (my_rank+1)%size
left=(my_rank-1+size)%size
left_ranks= [left]
right_ranks =[right]

rcv_buf=10 #should be overitten, just for test
rcv_buf=np.zeros(10,dtype='int')
win=MPI.Win.Create(rcv_buf,disp_unit=sizeOfInt, comm=MPI.COMM_WORLD)
grp_world=MPI.COMM_WORLD.Get_group()
grp_left=MPI.Group.Incl(grp_world,left_ranks)
grp_right=MPI.Group.Incl(grp_world,right_ranks)
MPI.Group.Free(grp_world)

sum = 0
snd_buf = my_rank
snd_buf = np.zeros(1,dtype='i')
#snd_buf=[]
#snd_buf.append(2)
#snd_buf.append(3)
#Put(self, origin, int target_rank, target=None)
for counter in range(0,size):
    #check if MPI.Win --> possible
    win.Post(grp_left,MPI.MODE_NOSTORE)
    MPI.Win.Start(win,grp_right,0)
    win.Put(snd_buf,right,None)
    win.Complete()
    win.Wait()
    snd_buf=rcv_buf
    sum= sum + rcv_buf

print('my_rank:',my_rank,'Sum=',sum)

#def Put(self, origin, int target_rank, target=None):
 #       """
  #      Put data into a memory window on a remote process.
   #     """
    #    cdef _p_msg_rma msg = message_rma()
     #   msg.for_put(origin, target_rank, target)
      #  with nogil: CHKERR( MPI_Put(
       #     msg.oaddr, msg.ocount, msg.otype,
        #    target_rank,
         #   msg.tdisp, msg.tcount, msg.ttype,
          #  self.ob_mpi) )

