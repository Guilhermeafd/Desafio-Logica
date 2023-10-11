#    O que deve ser utilizado
#Variáveis, Operadores, Lanço de repetição, Estrutura de decisão

#    Objetivo
#Crie uma variável para armazenar o nome e a quantidade de experiência (exp) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# XP menor que 1.000 = Ferro
# XP entre 1.001 e 2.000 = Bronze
# XP entre 2.001 e 5.000 = Prata 
# XP entre 5.001 e 7.000 = Ouro
# XP entre 5.001 e 8.000 = Platina
# XP entre 8.001 e 9.000 = Ascendente
# XP entre 9.001 e 10.000 = Imortal
# XP maior ou igual a 10.001 = Radiante

# Saída
# "O Herói (nome) está no nível (nivel)"

#Variáveis
nome = input("Digite o nome do herói: ")
level = int(input("Qual o nível de xp do {}: ".format(nome)))

#Condições
#Ferro
if level <= 1000:
    {
        print("O Herói {} está no nível FERRO.".format(nome, level))
    }

#Bronze
if (level >= 1001) and (level <= 2000):
    {
        print("O Herói {} está no nível BRONZE.".format(nome, level))
    }

#Prata
if (level >= 2001) and (level <= 5000):
    {
        print("O Herói {} está no nível PRATA.".format(nome, level))
    }

#Ouro
if (level >= 5001) and (level <= 7000):
    {
        print("O Herói {} está no nível OURO.".format(nome, level))
    }

#Platina
if (level >= 7001) and (level <= 8000):
    {
        print("O Herói {} está no nível PLATINA.".format(nome, level))
    }

#Ascendente
if (level >= 8001) and (level <= 9000):
    {
        print("O Herói {} está no nível ASCENDENTE.".format(nome, level))
    }

#Imortal
if (level >= 9001) and (level <= 10000):
    {
        print("O Herói {} está no nível IMORTAL.".format(nome, level))
    }

#Radiante
if level >= 10001:
    {
        print("O Herói {} está no nível RADIANTE".format(nome, level))
    }