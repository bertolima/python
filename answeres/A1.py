#Entrada: A entrada possui dois números inteiros ‘E’ e ‘T’ (1 <= E <= 500) (1 <= T <= 100) representando espaço e tempo, respectivamente.
#Saída: A saída consiste em uma única linha contendo a velocidade alcançada, sendo a velocidade calculada da seguinte forma: V = E/T. Sendo V a nossa velocidade desejada e é um número inteiro.
#Código
#entrada
E, T = input().split()
E = int(E)
T = int(T)
V = int(E/T)
print(V)