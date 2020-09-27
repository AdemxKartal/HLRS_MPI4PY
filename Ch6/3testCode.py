#run with: mpiexec -n 2 python ping_pong.py
# mpiexec --use-hwthread-cpus python3 ping_pong.py

from mpi4py import MPI
buffer= 1
proc_A = 0
proc_B = 1
ping=17
pong=23
length_of_message=1
number_of_messages = 50
size = MPI.COMM_WORLD.Get_size()
my_rank = MPI.COMM_WORLD.Get_rank()
start = MPI.Wtime()
status = MPI.Status()

snd_rq=[]

if(my_rank ==proc_A):
        req1=MPI.COMM_WORLD.isend(buffer, dest= proc_B, tag=ping)
        MPI.COMM_WORLD.recv(source= proc_B, tag=pong,status=status)
        snd_rq.append(req1)
        #print('req1: ', req1)

elif(my_rank ==proc_B):
        MPI.COMM_WORLD.recv(source=proc_A,tag=ping,status=status)
        req2=MPI.COMM_WORLD.isend(buffer,dest=proc_A,tag=pong)
        snd_rq.append(req2)
        #print('req2: ', req2)

finish =MPI.Wtime()

#testResult=MPI.Request.testall(request=snd_rq,statuses=None)
#print(testResult)
#print('snd_finished: ', snd_finished, 'type of snd_finished: ', type(snd_finished))
snd_data=1

total=MPI.COMM_WORLD.reduce(snd_data,root=0,op=MPI.SUM)
print('total: ', total)
time = finish-start
#print('reqs: ', reqs)
print('time for one messsage: ',(time/(2*number_of_messages)*1e6))

