#mpiexec -n 2 python3 ibarrirer_skel.py
from mpi4py import MPI
status = MPI.Status()
tag_ready= 7781
request = MPI.Request()
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
request = MPI.Request()


snd_rq=[]
#in the role as sending process
snd_finished=0
number_of_dest=0 # only for verification, should be removed in real applications
                   #         Caution: total_number_of_dests may be less than 4, see if-statements below

#in the role of receiving process
ib_finished=0
number_of_recvs=0
rcv_status=MPI.Status()

round =0 #only for verification, should be removed in real applications

dest = my_rank+1

if(dest>=0 and dest<size):
    snd_buf_A=1000*my_rank+dest
    snd_req1=MPI.COMM_WORLD.issend(obj=snd_buf_A,dest=dest,tag=222)
    snd_rq.append(snd_req1)
    print('send: A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest = my_rank-2
if(dest>=0 and dest<size):
    snd_buf_B=1000*my_rank+dest
    snd_req2=MPI.COMM_WORLD.issend(obj=snd_buf_B,dest=dest,tag=222)
    snd_rq.append(snd_req2)
    print('send: A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest=my_rank+4
if(dest>=0 and dest<size):
    snd_buf_C=1000*my_rank+dest
    snd_req3=MPI.COMM_WORLD.issend(obj=snd_buf_C,dest=dest,tag=222)
    snd_rq.append(snd_req3)
    print('send: A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

dest =my_rank-7

if(dest>=0 and dest<size):
    snd_buf_D= 1000*my_rank+dest
    snd_req4=MPI.COMM_WORLD.issend(obj=snd_buf_D,dest=dest,tag=222)
    snd_rq.append(snd_req4)
    print('send: A rank: ',my_rank,'sending message: ', snd_buf_A,'from ', my_rank, 'to',dest)
    number_of_dest=number_of_dest+1

while(not ib_finished):
    ______ = MPI.COMM_WORLD.iprobe(source=______,tag=_____,status=_____)
    if(rcv_flag):
        rcv_buf=MPI.COMM_WORLD.recv(source=MPI.ANY_SOURCE, tag =222, status=rcv_status)
        print('recv: A rank: ',my_rank,'received message ', rcv_buf, 'from',rcv_status.source)
        number_of_recvs=number_of_recvs+1

    if(not snd_finished):
        _______=MPI.Request.test____(requests=_____,statuses=_____) #describe in slides --> can be confusing that the function is rteurning an tuple, explain the decleation of the next line where you assign the return value of the function to a variable
        snd_finished=______[0]

        if(_________):
            ______=MPI._____.______()

    if(snd_finished):
        resultTest=______.Test() # explain this line in slides
        ib_finished=resultTest
    if(ib_finished==True):
        print('loop condition done')
print('loop finished')


#total=MPI.COMM_WORLD.reduce(1,root=0,op=MPI.SUM)
total_number_of_dests=MPI.COMM_WORLD.reduce(number_of_dest, root=0,op=MPI.SUM)
total_number_of_recvs=MPI.COMM_WORLD.reduce(sendobj=number_of_recvs, op =MPI.SUM, root=0)

if(my_rank==0):
    print('B #sends ',total_number_of_dests, '#receives = ',total_number_of_recvs)
    if(total_number_of_dests!=total_number_of_recvs):
        print('ERROR!!! Wrong number of receives')


