from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
request = MPI.Request()
#in the role as sending process
snd_finished=0
number_of_dest=0 # only for verification, should be removed in real applications
                   #         Caution: total_number_of_dests may be less than 4, see if-statements below
##

#in the role of receiving process
ib_finished=0
rcv_flag=0
number_of_recvs=0
rcv_status=MPI.Status()

round =0 #only for verification, should be removed in real applications

dest = my_rank+1

if(dest>=0 and dest<size):
    snd_buf_A=1000*my_rank+dest
    MPI.COMM_WORLD.issend(obj=snd_buf_A,dest=dest,tag=222)
    print('A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest = my_rank-2
if(dest>=0 and dest<size):
    snd_buf_B=1000*my_rank+dest
    MPI.COMM_WORLD.issend(obj=snd_buf_B,dest=dest,tag=222)
    print('A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest=my_rank+4
if(dest>=0 and dest<size):
    snd_buf_C=1000*my_rank+dest
    MPI.COMM_WORLD.issend(obj=snd_buf_C,dest=dest,tag=222)
    print('A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest =my_rank-7
if(dest>=0 and dest<size):
    snd_buf_D= 1000*my_rank+dest
    MPI.COMM_WORLD.issend(obj=snd_buf_D,dest=dest,tag=222)
    print('A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

while(ib_finished==0):
    rcv_flag = MPI.COMM_WORLD.iprobe(source=MPI.ANY_SOURCE,tag=222,status=None)
    if(rcv_flag):
        MPI.COMM_WORLD.recv(source=MPI.ANY_SOURCE, tag =222, status=rcv_status)
        print('A rank: ',my_rank,)
#Comm.iprobe(self, int source=ANY_SOURCE, int tag=ANY_TAG, Status status=None




