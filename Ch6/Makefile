ibarrier: ibarrier_skel.c
	mpicc -o ibarrier ibarrier_skel.c
ibarriersolution: ibarrier_solution.c
	mpicc -o ibarriersolution ibarrier_solution.c
ibarrierwrongsolution: ibarrier_solution_wrong.c
	mpicc -o ibarrierwrongsultion ibarrier_solution_wrong.c

ringallreduce: ring_allreduce.c
	mpicc -o ringallreduce ring_allreduce.c

ibarrierold: ibarrier_skel_OLD.c
	mpicc -o ibarrierold ibarrier_skel_OLD.c
ibarroptimizedsolution: ibarrier_solution_optimized.c
	mpicc -o ibarroptimizedsolution ibarrier_solution_optimized.c
ringadvscan: ring_advanced1_scan.c
	mpicc -o ringadvscan ring_advanced1_scan.c

torusadv2: torus_advance2_subtopology.c
	mpicc -o torus_advance2_subtopology.c


runibarrier: ibarrier
	mpirun --use-hwthread-cpus -np 4 ibarrier

runibarriersolution: ibarriersolution
	mpirun --use-hwthread-cpus -np 4 ibarriersolution
runibarrierwrongsolution: ibarrierwrongsolution
	mpirun --use-hwthread-cpus -np 4 ibarrierwrongsolution
runringallreduce: ringallreduce
	mpirun --use-hwthread-cpus -np 4 ringallreduce
runibarrierold: ibarrierold
	mpirun --use-hwthread-cpus -np 4 ibarrierold
runibarroptimizedsolution: ibarroptimizedsolution
	mpirun --use-hwthread-cpus -np 4 ibarroptimizedsolution
runringadvscan: ringadvscan
	mpirun --use-hwthread-cpus -np 4 ringadvscan
runtorusadv2: torusadv2
	mpirun --use-hwthread-cpus -np 4 torusadv2


