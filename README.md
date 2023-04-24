# tcc_particles
Estudo sobre a performance de diversos compiladores sobre um problema de sistemas dinâmicos.

## Software Requirements
libgsl-dev;


### Compilar e executar:
> gcc downloading_wall_restitution_GPU.c -o downloading_wall_restitution_GPU -std=c11 -lgsl -lgslcblas -lm -pg -O3


> ./downloading_wall_restitution_GPU 0.0001 8 10 0.09

Nota: os parâmetros usado na execução do script são passados para a compilação do arquivo dowloading_wall_restitution_GPU.c
