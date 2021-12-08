#The problem ask the sum of all the multiples of 3 and 5 below 1000. I`ve chosen to write a single function, applying the sum of consecutive positive integers.
#O problema pede a soma de todos os multiplos de 3 e 5 menores que 1000. Eu decidi escrever uma funcao simples, aplicando a soma de inteiros positivos consecutivos.

n = 1000 # The input of our fuction to solve the problem / Nossa entrada para resolver o problema.

i = ((n-1)//3) # These variables will give us the number of multiples of 3, 5 and 15 below the input n given, which will be needed to solve our function.
j = ((n-1)//5) # Essas variaveis nos dao o numero de multiplos de 3, 5 e 15 abaixo da entrada dada, que serao necessarios para resolver nossa funcao.
k = ((n-1)//15)

print(int
((3*(((i)*(i+1)/2)))+ #Sum of the multiples of 3 / Soma dos multiplos de 3
(5*(((j)*(j+1)/2)))-  #Sum of the multiples of 5 / Soma dos multiplos de 5
(15*(((k)*(k+1)/2)))) #Sum of the multiples of 15. This one is subtracted to avoid double counting 15, 30 etc./ Soma dos multiplos de 15. Essa eh subtraida para evitar contar duas vezes 15, 30 etc.
)

