clusteradv: cluster_comm_create_adv.c
	mpicc -o clusteradv cluster_comm_create_adv.c

clusterskel: cluster_comm_create_skel.c 
	mpicc -o clusteradv cluster_comm_create_skel.c 

ringintercomm: ring_intercomm.c
	mpicc -o ringintercomm ring_intercomm.c

ringtworings: ring_tworings.c
	mpicc -o ringtworings ring_tworings.c

ringtwocreate: ring_tworings_comm_create.c
	mpicc -o ringtwocreate ring_tworings_comm_create.c
	
	

runclusteradv: clusteradv
	mpirun --use-hwthread-cpus -np 4 clusteradv

runclusterskel: clusterskel
	mpirun --use-hwthread-cpus -np 4 clusterskel

runringintercomm: ringintercomm
	mpirun --use-hwthread-cpus -np 4 ringintercomm

runringtworings: ringtworings
	mpirun --use-hwthread-cpus -np 4 ringtworings

runringtwocreate: ringtwocreate
	mpirun --use-hwthread-cpus -np 4 ringtwocreate


