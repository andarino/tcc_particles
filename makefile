TARGET=tt
CPUCC=gcc
LFLAGS=-lgsl -lgslcblas
LIBS= -lm
LD=gcc
CPU_COMPILE = $(CPUCC) $(LFLAGS)
R=rm -r dowloading_wall_resitution.o
all: main 
	$(CPU_COMPILE) dowloading_wall_resitution.o $(LIBS)  -o $(TARGET); $(R)
main:
	$(CPU_COMPILE) -c dowloading_wall_resitution.c
clean: 
	rm -rf tt
	
	
