ring: ring.c
	mpicc -o ring ring.c
	
ring1sidedexa2: ring_1sided_exa2.c
	mpicc -o ring1sidedexa2 ring_1sided_exa2.c
ring1sidedput: ring_1sided_put.c
	mpicc -o ring1sidedput ring_1sided_put.c
haloirecvsend: halo_irecv_send.c
	mpicc -o haloirecvsend halo_irecv_send.c
haloirecvsend: halo_isend_recv.c
	mpicc -o haloirecvsend halo_isend_recv.c
	
	
	
	
	
runring: ring
	mpirun --use-hwthread-cpus -np 4 ring

runring1sidedexa2: ring1sidedexa2
	mpirun --use-hwthread-cpus -np 4 ring1sidedexa2
runring1sidedput: ring1sidedput
	mpirun --use-hwthread-cpus -np 4 ring1sidedput
	
runhaloirecvsend: haloirecvsend
	mpirun --use-hwthread-cpus -np 4 haloirecvsend
	
runhaloirecvsend: haloirecvsend
	mpirun --use-hwthread-cpus -np 4 haloirecvsend
