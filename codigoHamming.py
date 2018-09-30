# Codigo de Hamming para verificacao e correcao de dados de transmissao
#Alunos: 	Helena Mylena Cunha Dantas
#			Igor Dantas Lucena

p1 = [True,False,True,False,True,False,True,False,True,False,True,False]
p2 = [False,True,True,False,False,True,True,False,False,True,True,False]
p4 = [False,False,False,True,True,True,True,False,False,False,False,True]
p8 = [False,False,False,False,False,False,False,True,True,True,True,True]
verifica = [False,False,False,False]

def addBitsParidade(dado):
	dado.insert(0,'0')
	dado.insert(1,'0')
	dado.insert(3,'0')
	dado.insert(7,'0')
	return dado
	
def defineP1(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p1[i] and dado[i] == '1'):
			cont += 1
	if(cont % 2 != 0):
		dado[0] = 1
	
	return dado
	
def defineP2(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p2[i] and dado[i] == '1'):
			cont += 1
	if(cont % 2 != 0):
		dado[1] = 1
	
	return dado
	
def defineP4(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p4[i] and dado[i] == '1'):
			cont += 1
	if(cont % 2 != 0):
		dado[3] = 1
	
	return dado

def defineP8(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p8[i] and dado[i] == '1'):
			cont += 1
	if(cont % 2 != 0):
		dado[7] = 1
	
	return dado

def defineParidade(dado):
	addBitsParidade(dado)
	dado = defineP1(dado)
	dado = defineP2(dado)
	dado = defineP4(dado)
	return defineP8(dado)

def verificaP1(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p1[i] and dado[i] == '1'):
			cont += 1
	
	if(cont % 2 == 0):
		verifica[0]= True
	
def verificaP2(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p2[i] and dado[i] == '1'):
			cont += 1
			
	if(cont % 2 == 0):
		verifica[1] = True
		
def verificaP4(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p4[i] and dado[i] == '1'):
			cont += 1
	
	if(cont % 2 == 0):
		verifica[2]= True
	
def verificaP8(dado):
	cont = 0
	for i in xrange(len(dado)):
		if(p8[i] and dado[i] == '1'):
			cont += 1

	if(cont % 2 == 0):
		verifica[3]= True
		
def verificaParidade(dado):
	verificaP1(dado)
	verificaP2(dado)
	verificaP4(dado)
	verificaP8(dado)
	
	if(False in verifica):
		return False
	else:
		return True
	
def corrigeDado(dado):
	
	bit = 0
	dado = toList(dado)
	if(not verifica[0]):
		bit+=1
			
	if(not verifica[1]):
		bit+=2
			
	if(not verifica[2]):
		bit+=4
		
	if(not verifica[3]):
		bit+=8
			
	if(dado[bit-1] == '1'):
		dado[bit-1] = '0'
	else:
		dado[bit-1] = '1'
	dado = toString(dado)
	
	return dado

def bitErro():
	bit = 0
	
	if(not verifica[0]):
		bit+=1
			
	if(not verifica[1]):
		bit+=2
			
	if(not verifica[2]):
		bit+=4
		
	if(not verifica[3]):
		bit+=8
	
	return bit
	
def toList(string):
	lista = []
	for i in string:
		lista.append(i)
	return lista
	
def toString(lista):
	string = ''
	
	for i in lista:
		string += str(i)
	
	return string
	
def menu():
	print "Menu: \n1- Gerar paridade\n2- Verificar paridade\n0- Sair\n"
	opcao = raw_input("Opcao: ")
	if(opcao == '0'):
		return False
	elif(opcao == '1'):
		entrada = raw_input("Digite uma entrada de 8 bits: ")
		entrada = toList(entrada)
		entrada = defineParidade(entrada)
		entrada = toString(entrada)
		print entrada
		
	elif(opcao == '2'):
		entrada = raw_input("Digite uma entrada de 12 bits: ")
		if(verificaParidade(entrada)):
			print "Paridade verificada com sucesso!!!\n"
		else:
			print "Erro na verificacao de paridade! Erro no bit ", bitErro()
			opcao2 = raw_input("Deseja corrigir o erro? [s/n]")
			if(opcao2.upper() == "S"):
				print "Dado corrigido:" ,corrigeDado(entrada),"\n"

	return menu()
	
	
while (True):
	if(not menu()):
		break
