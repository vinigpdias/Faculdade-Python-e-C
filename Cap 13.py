usuários = [] 
import hashlib
h = hashlib.new('sha256')
h.update(b"Nobody inspects the spammish repetition")
h.hexdigest()

#Primeiro usuário
usuário1 = {
    "name": "Clark Kent",
    "username": "kent",
    "password": "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"
}

#Adicionar usuário1 na lista
usuários.append(usuário1)

#Segundo usuário
usuário2 = {
    "name": "Bruce Wayne",
    "username": "wayne",
     "password": "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"
}

#Adicionar usuário2 na lista
usuários.append(usuário2)

#Terceiro usuário
usuário3 = {
    "name": "Christopher Walker",
    "username": "walker",
    "password": "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"
}

#Adicionar usuário3 na lista
usuários.append(usuário3)

#print(usuários)

#Interface coloque seu username e password
username = ["kent", "wayne", "walker"]
Nome = input("Digite seu username ")
Senha = input("Digite a sua senha ")
password = input()

#Condições de usuário e senha
#Primeiro uruário:
while Nome != "kent":
    print(Nome)
    if Nome == "kent":
        Numero_hash1 = hashlib.sha256(b"password").hexdigest()

        if Numero_hash1 == "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2":
            print(Numero_hash1)

#if Numero_hash1 != "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2":
#    print("Acesso Negado!")
    
#    if (Senha != "Kryp10N1938"):
#        print("Acesso Negado!")
#        exit()
#    if Senha == "Kryp10N1938":
        #Função para gerar numero hash SHA256
#        Senha1 = b"Kryp10N1938" 
        
    
#else:
#    print("Acesso negado")
        

#Segundo usuário:
#if Nome == "wayne":
#    if (Senha != "k@ne1939FInGer"):
#        print("Acesso Negado!")
#        exit()
#    if Senha == "k@ne1939FInGer":
    #Função para gerar numero hash SHA256
#       Senha2 = b"k@ne1939FInGer"
#       Numero_hash2 = hashlib.sha256(Senha2).hexdigest()
#    if Numero_hash2 == "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a":
#                print("Bruce Wayne logado!")
#    else:
#        print("Acesso negado")

#Terceiro usuário:
#if Nome == "walker":
#    if (Senha != "F@lK1936bEnG@1@"):
#        print("Acesso Negado!")
#        exit()
#    if Senha == "F@lK1936bEnG@1@":
        #Função para gerar numero hash SHA256
#        Senha3 = b"F@lK1936bEnG@1@"
#        Numero_hash3 = hashlib.sha256(Senha3).hexdigest()
#    if Numero_hash3 == "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83":
#                print("Christopher Walker logado!")
#    else:
#        print("Acesso negado")

#else:
#    print("Acesso negado")
#    exit()

#Resposta = ("sim")
#Pergunta = input("Você gostaria de visualizar seu código bytes? ")

#if Pergunta == "sim":
#    string = Senha

#    arr = bytes(string, 'utf-8')
#    arr2 = bytes(string, 'ascii')

    #print(arr,'\n')

    # actual bytes in the the string
#    for byte in arr:
#        print(byte, end=' ')
#    print("\n")
#    for byte in arr2:
#        print(byte, end=' ')
    