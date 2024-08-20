#Strings são sequências de caracteres!

#Para criar uma string você precisa usar aspas simples ou aspas dupla, exe:

#uma palavra
string1 = "Oi!"

#uma frase
string2 = "oi, tudo bem?"

#com aspas simples
string3 = 'Ctrl+Play - escola de programação'

print(string1)
print(string2)
print(string3)

#para imprimir uma string, utilize a função (print), exe:

string4 = "teste"
print(string4)
print("teste")

#saltando linhas e acrescentando espaços, exe:

#utilize \n para saltar linhas
print("Saltando \n\n linhas \n !")

#utilize \t para acrescentar espaços maiores em textos
print("olá \t ctrl+play!")

#Se você especifica que pode ter só 14 caracteres, você precisa fazer essa verificação, fazer isso se chama, FUNÇÃO (LEN), exe:

#veja quantos caracteres formam a frase a seguir:

frase = "ctrl+play - escola de programação e robótica"
len(frase)

#indexação de strings é quando precisa saber a letra inicial de uma palavra que ta armazenada na string, exe:

nome = "fulano soares silva"
print(nome[0])
#usar [] como objetivo de acessar os índices 
#a primeira letra é sempre 0

#Como eu poderia fazer para saber quantos pontos(".") teriam no endereço de e-mail? Utilizando a função count(), exe:

#utilize a função count() para contar caracteres dentro de uma string

email = "fulado@ctrlplay.com.br"
print(email.count("."))


#ENTRADA DE DADOS
#Uma aplicação pode pedir que o usuário informe uma determinada informação. 
#funçaõ input() escreve uma string passada como um parâmetro e em seguida, ativa o modo de digitação. Então o usuário digita o que foi solicitado e pressiona ENTER. O valor informado pode ser atribuído a uma variável, exe:

nome = input("digite seu nome: ")
print("\n Olá, "+nome)
Digite o nome: 


