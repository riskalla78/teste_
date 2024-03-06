
# Questão 1
# indice = 13 
# soma = 0
# k = 0
# while k < indice:
#     k= k + 1
#     soma = soma + k
# print(soma)

# Questão 2
# def gera_sequencia_fibonacci(ate_numero):
    
#     a, b = 0, 1

#     sequencia = [a]

   
#     while b <= ate_numero:
    
#         sequencia.append(b)
#         a, b = b, a + b
#         print (sequencia)

#     return sequencia

# def pertence_a_fibonacci(numero, sequencia):
 
#     return numero in sequencia


# numero_informado = int(input("Informe um número para gerar a sequência de Fibonacci: "))
# sequencia_fibonacci = gera_sequencia_fibonacci(numero_informado)


# if pertence_a_fibonacci(numero_informado, sequencia_fibonacci):
#     print(f"{numero_informado} pertence à sequência de Fibonacci.")
#     print("Sequência de Fibonacci:", sequencia_fibonacci)
# else:
#     print(f"{numero_informado} não pertence à sequência de Fibonacci.")


#Questão 3
# a) 9
# b) 128
# c) 49
# d) 100
# e) 13
# f) 36

#Questão 4
# Primeira visita:

# Ligo o primeiro interruptor e aguardo alguns minutos para que a lâmpada esquente.
# Depois, desligo o primeiro interruptor e ligo o segundo interruptor.
# Segunda visita:

# Entro na sala onde as lâmpadas estão localizadas.
# A lâmpada que está acesa corresponde ao interruptor ligado na primeira vez.
# Toco na lâmpada que está desligada:
# Se a lâmpada estiver quente, então o primeiro interruptor (o primeiro liguei) controla essa lâmpada.
# Se a lâmpada estiver acesa, então o segundo interruptor (o segundo que liguei) controla essa lâmpada.
# Se a lâmpada estiver fria e desligada, então o terceiro interruptor controla essa lâmpada.

#Questão 5
# string = input("Digite uma string para ser invertida: ")
# invertido = string[::-1]
# print(f"String original: {string}\nString invertida: {invertido} ",)