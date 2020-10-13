pingpong: ping_pong.c
	mpicc -o pingpong ping_pong.c
pingpongadv1:
	mpicc -o pingpongadv ping_pong_advanced1.c

pingpongadv2s:
	mpicc -o pingponadv2s ping_pong_advanced2_send.c
pingpongadv2ss:
	mpicc -o pingpongadv2ss ping_pong_advanced2_ssend.c




runpingpong: pingpong
	mpirun --use-hwthread-cpus -np 4 pingpong

runpingpongadv1: pingpongadv1
	mpirun --use-hwthread-cpus -np 4 pingponadv1
	
runpingpongadv2s: pingpongadv2s
	mpirun --use-hwthread-cpus -np 4 pingponadv2s


runpingpongadv2ss: pingpongadv2ss
	mpirun --use-hwthread-cpus -np 4 pingponadv2ss
