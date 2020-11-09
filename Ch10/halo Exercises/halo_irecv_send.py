#run with: mpiexec -n 2 python3 halo_irecv_send.py
#mpiexec --use-hwthread-cpus python3 halo_irecv_send.py

from mpi4py import MPI
import numpy as np
number_of_messages=50
start_length=4
length_factor=8
max_length=  8388608 # ==> 2 x 32 MB per process
number_packages=8
 #max_length= 67108864     ==> 2 x 0.5 GB per process
 #number_package_sizes= 9
snd_buf_left=np.zeros(max_length,dtype='single')
snd_buf_right=np.zeros(max_length,dtype='single')
rcv_buf_left=np.zeros(max_length,dtype='single')
rcv_buf_right=np.zeros(max_length,dtype='single')

 #Naming conventions
 #Processes:
 # my_rank-1    my_rank     my_rank+1
 # "left neighbor"  "myself"    "right neighbor"
 # rcv_buf_right <-- snd_buf_left snd_buf_right ---> rcv_buf_left
 # snd_buf_right --> rcv_buf_left rcv_buf_right <-- snd_buf_left
 #                      |                               |
 #               halo-communication              halo-communication


size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
right = (my_rank+1)%size
left=(my_rank-1+size)%size
rq=[]
status1=MPI.Status()
status2=MPI.Status()
arr_status = [status1,status2]


if(my_rank==0):
    print('message size transfertime duplex badnwidth per process and neighbor')

length= start_length

for jj in range (1, number_packages+1):#loop starts with 1 --> prevent divison by 0
    for ii in range(1,number_of_messages+1): #loop starts with 1 --> prevent divison by 0
        if(ii==1):
            start=MPI.Wtime()
        test_value = jj*1000 + ii*1000 + my_rank*10
        mid= (length-1)/(number_of_messages*ii)
        print('mid = ', mid)
        snd_buf_left[0]=test_value+1
        snd_buf_left[mid]=test_value+2
        snd_buf_left[length-1]=test_value+3

        snd_buf_right[0]=test_value+6
        snd_buf_right[mid]=test_value+7
        snd_buf_right[length-1]=test_value+8

        recv_buf_right= MPI.COMM_WORLD.irecv(source=right,tag=17)
        recv_buf_left= MPI.COMM_WORLD.irecv(soruce=left,tag=23)
        rq.append(recv_buf_right)
        rq.append(recv_buf_left)

        MPI.COMM_WORLD.send(buf=snd_buf_left, dest=left,tag=17)
        MPI.COMM_WORLD.send(buf=snd_buf_right,dest=right,tag=23)
        MPI.Request.waitall(requests=rq, statuses=arr_status)

        test_value= jj*1000000 +ii*10000 + left*10
        mid=(length-1)/(number_of_messages*ii)
        snd_buf_right[0]= test_value+6
        snd_buf_right[mid]=test_value+7
        snd_buf_right[length-1]=test_value+8

        test_value=jj*1000000 + ii*10000 + right*10
        mid=(length-1)/(number_of_messages*ii)
        snd_buf_left[0]=test_value+1
        snd_buf_left[mid]=test_value+2
        snd_buf_left[length-1]= test_value+3

        if(rcv_buf_left[0]!= snd_buf_right[0] | rcv_buf_left[mid]!= snd_buf_right[mid] | rcv_buf_left[length-1]!=snd_buf_right[length-1]):
            print(my_rank,'jj=',jj,'ii=',ii,'--> snd_buf_right[',0,mid,length-1,'] = ',snd_buf_right[0],snd_buf_right[mid],snd_buf_left[length-1])
            print(my_rank,'is not identical to rcv_buf_left[',0,mid,length-1,'] = ', rcv_buf_left[0],rcv_buf_left[mid],rcv_buf_left[length-1])
        if(rcv_buf_right[0]!=snd_buf_left[0] | rcv_buf_right[mid] != snd_buf_left[mid] | rcv_buf_right[length-1]!=snd_buf_left[length-1]):
            print(my_rank,'jj=',jj,'ii=',ii,'--> snd_buf_left[',0,mid,length-1,'] = ',snd_buf_left[0],snd_buf_left[mid],snd_buf_right[length-1])
            print(my_rank,'is not identical to rcv_buf_right[ ',0,mid,length-1,'] = ', rcv_buf_right[0],rcv_buf_right[mid],rcv_buf_right[length-1])
    finish=MPI.Wtime()
    if(my_rank==0):
        transfertime=(finish-start)/number_of_messages
        print(np.dtype('single').itemsize*length, 'bytes',transfertime*1e6, 'usec',length*np.dtype('single').itemsize*2*1e-6, 'MB/s')

    length=length*length_factor


        #    ...snd_buf_... is used to store the values that were stored in snd_buf_... in the neighbor process
    #MPI_Irecv(&rcv_buf, 1, MPI_INT, left, to_right,MPI_COMM_WmORLD, &request);
    #int MPI_Irecv(void *buf, int count, MPI_Datatype datatype, int source,   int tag, MPI_Comm comm, MPI_Request *request)
    #recv = MPI.COMM_WORLD.irecv(source=left, tag=to_right)
