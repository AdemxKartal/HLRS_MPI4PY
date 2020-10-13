ring: ring.c
	mpicc -o ring ring.c
	
ringissendirecv: ring_advanced_irecv_issend.c
	mpicc -o ringadvIssendIrecv ring_advanced_irecv_issend.c
	
ringssendirecv: ring_advanced_irecv_ssend.c 
	mpicc -o ringadvSsendIrecv ring_advanced_irecv_ssend.c

runring: ring
	mpirun --use-hwthread-cpus -np 4 ring

runringadv1: ringissendirecv
	mpirun --use-hwthread-cpus -np 4 ringadvIssendIrecv

runringadv2: ringssendirecv
	mpirun --use-hwthread-cpus -np 4 ringadvSsendIrecv

