#Testando esse novo editor de codigo
#Receber nome, idade e sexo do usuario 
#Devolver quantos usuarios maior de 18 anos
#Quantos homens cadastrados
#Quantas mulher menores de 20 anos

#Condicoes
while True: 
    
    #Inicio
    print("--------------------")
    print("CADASTRO DE PESSOAS")
    print("--------------------")
    
    #Variaveis
    Idade = int(input("Digite a sua idade: "))
    Sexo = str(input("Qual seu sexo? [F/M] ")).split().upper()[0]
    
    #Condicoes
    while Sexo not in ("FM"):
        Sexo = str(input("Qual seu sexo? [F/M]")).split().upper()[0]
        
    Continuar = str(input("Deseja continuar? [S/N] ").split().upper()[0]
    
    while Continuar not in ("SN"):
        Continuar = str(input("Deseja continuar? [S/N]")
        