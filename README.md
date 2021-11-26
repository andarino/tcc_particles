# tcc_particles
Projeto em física de partículas para paralelizar.

### Para executar:

> gcc dowloading_wall_restitution_OMP.c -o dowloading_wall_restitution_OMP -std=c11 -fopenmp -lgsl -lgslcblas -lm -pg

> ./dowloading_wall_restitution_OMP 0.001 8 10 0.09

> gprof  --flat-profile ./dowloading_wall_restitution_OMP
