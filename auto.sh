#!/usr/bin/bash

case $1 in
"-h") echo "./auto.sh [param]"
exit 0
;;
"-v") echo "hilarious version"
exit 0
;;
esac


if [ -e dowloading_wall_restitution_GPU1 ]
then 
	echo "[!] removendo arquivo dowloading_wall_restitution_GPU1 existente "
	rm dowloading_wall_restitution_GPU1

elif [ -e dowloading_wall_restitution_GPU2 ] 
then 
	echo "[!] removendo arquivo dowloading_wall_restitution_GPU2 existente "
	rm dowloading_wall_restitution_GPU2

elif [ -e dowloading_wall_restitution_GPU3 ] 
then 
	echo "[!] removendo arquivo dowloading_wall_restitution_GPU3 existente "
	rm dowloading_wall_restitution_GPU3

else 
	echo  "[x] Nenhum executável para ser removido !!!"
fi

echo "[!] compilando O1, O2, O3 com os parametro: $*"

OPT1=`gcc dowloading_wall_restitution_GPU.c -o dowloading_wall_restitution_GPU1 $* -O1 `

OPT2=`gcc dowloading_wall_restitution_GPU.c -o dowloading_wall_restitution_GPU2 $* -O2`

OPT3=`gcc dowloading_wall_restitution_GPU.c -o dowloading_wall_restitution_GPU3 $* -O3`

echo "[!] executando o programa 10 vezes com casa 'O' "
echo "[!] Aguarde ... "

if [ -d "time" ]; then 
	rm -r time/
	mkdir time
else 
	mkdir time
fi

#***************************************************************
echo "PARAMETROS USADOS: $*" > time/dataO1.txt
echo " "

for i in $(seq 10);
 do
  ./dowloading_wall_restitution_GPU1 0.0001 8 10 0.09 >> time/dataO1.txt
	echo "=============================================================" >> time/dataO1.txt
  sleep 5
done
echo "[v] tempos salvos em 'time/dataO1'"

#***************************************************************
echo "PARAMETROS USADOS: $*" > time/dataO2.txt
echo " "
for i in $(seq 10);
 do
   ./dowloading_wall_restitution_GPU2 0.0001 8 10 0.09 >> time/dataO2.tx
   echo "=============================================================" >> time/dataO2.txt
   	sleep 5
done
echo "[v] tempos salvos em 'time/dataO2'"

#***************************************************************

echo "PARAMETROS USADOS: $*" > time/dataO3.txt
echo " "
for i in $(seq 10);
 do
   ./dowloading_wall_restitution_GPU3 0.0001 8 10 0.09 >> time/dataO3.txt
   echo "=============================================================" >> time/dataO3.txt
 	sleep 5
 done

echo "[v] tempos salvos em 'time/dataO3'"
























