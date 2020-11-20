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
        print('length-1 : ', length-1, 'number_of_messages*ii: ', number_of_messages*ii)
