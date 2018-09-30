import unittest
# Codigo de Hamming para verificacao e correcao de dados de transmissao
#Alunos: 	Helena Mylena Cunha Dantas
#			Igor Dantas Lucena

p1 = [True,False,True,False,True,False,True,False,True,False,True,False]
p2 = [False,True,True,False,False,True,True,False,False,True,True,False]
p4 = [False,False,False,True,True,True,True,False,False,False,False,True]
p8 = [False,False,False,False,False,False,False,True,True,True,True,True]
verifica = [False,False,False,False]

def reset():
	global verifica 
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
	dado = toList(dado)
	addBitsParidade(dado)
	dado = defineP1(dado)
	dado = defineP2(dado)
	dado = defineP4(dado)
	dado = toString(defineP8(dado))
	return dado

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
	reset()
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

class TesteMetodos(unittest.TestCase):
	
	def test_DefineParidade_Teste1(self):
		dado = '10011010'
		saida = defineParidade(dado)
		self.assertEqual(saida, '011100101010')

		dado1 = '10101110'
		saida1 = defineParidade(dado1)
		self.assertEqual(saida1, '101101011110')

		dado2 = '11110101'
		saida2 = defineParidade(dado2)
		self.assertEqual(saida2, '101011100101')

		dado3 = '01010001'
		saida3 = defineParidade(dado3)
		self.assertEqual(saida3, '010110110001')

		dado4 = '01100110'
		saida4 = defineParidade(dado4)
		self.assertNotEqual(saida4, '000011000110')

		
        
		
		
	def test_CorrigeParidade_Teste1(self):
		dado = '011100101110'
		verificaParidade(dado)
		saida = corrigeDado(dado)
		self.assertEqual(saida, '011100101010')

		dado1 = '101101011010'
		verificaParidade(dado1)
		saida1 = corrigeDado(dado1)
		self.assertEqual(saida1, '101101011110')

		dado2 = '111011100101'
		verificaParidade(dado2)
		saida2 = corrigeDado(dado2)
		self.assertEqual(saida2, '101011100101')

		dado3 = '011110110001'
		verificaParidade(dado3)
		saida3 = corrigeDado(dado3)
		self.assertEqual(saida3, '010110110001')

		dado4 = '000011000110'
		verificaParidade(dado4)
		saida4 = corrigeDado(dado4)
		self.assertEqual(saida4, '010011000110')	
			
def test():
	if( __name__ == "__main__"):
		unittest.main()

def menu():
	
	print "Menu: \n1- Gerar paridade\n2- Verificar paridade\n3- Rodar testes\n0- Sair\n"
	opcao = raw_input("Opcao: ")
	if(opcao == '0'):
		return False
	elif(opcao == '1'):
		entrada = raw_input("\nDigite uma entrada em binario de 8 bits: ")
		saida = defineParidade(entrada)
		print saida
		
	elif(opcao == '2'):
		entrada = raw_input("\nDigite uma entrada em binario de 12 bits: ")
		if(verificaParidade(entrada)):
			print "\nParidade verificada com sucesso!!!\n"
		else:
			print "\nErro na verificacao de paridade! Erro no bit ", bitErro()
			opcao2 = raw_input("Deseja corrigir o erro? [s/n]")
			if(opcao2.upper() == "S"):
				print "\nDado corrigido:" ,corrigeDado(entrada),"\n"
	elif(opcao == '3'):
		test()
		
	return menu()
	
	
while (True):
	if(not menu()):
		break
