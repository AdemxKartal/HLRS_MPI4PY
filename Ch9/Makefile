ringneighbrAllToAll: ring_neighbor_alltoall.c
	mpicc -o ringneighbrAllToAll ring_neighbor_alltoall.c

ringneighbrAllToAllTest: ring_neighbor_alltoall_TEST.c
	mpicc -o ringneighbrAllToAllTest ring_neighbor_alltoall_TEST.c

topologyRing: topology_ring.c
	mpicc -o topologyRing topology_ring.c

ringneighbrAllToAllW: ring_neighbor_alltoallw.c
	mpicc -o ringneighbrAllToAllW ring_neighbor_alltoallw.c




runringneighbrAllToAll: ringneighbrAllToAll
	mpirun --use-hwthread-cpus -np 4 ringneighbrAllToAll
runringneighbrAllToAllTest: ringneighbrAllToAllTest
	mpirun --use-hwthread-cpus -np 4 ringneighbrAllToAllTest
runtopologyRing: topologyRing
	mpirun --use-hwthread-cpus -np 4 topologyRing
runringneighbrAllToAllW: ringneighbrAllToAllW
	mpirun --use-hwthread-cpus -np 4 ringneighbrAllToAllW


