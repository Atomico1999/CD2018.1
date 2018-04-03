#-*- coding:utf-8 -*-
#Escrito e compilado em python 2.7
#
# Tarefa: criar conversor decimal-binario-hexadecimal
# 2 integrantes - tempo estimado para entrega: 10 dias
#
# Integrantes da equipe: NOME - MATRÍCULA
#	 Louis Ian Silva dos Santos - 402525
#	 Francisco Rodrigo Ferreira Uchôa - 403709 


def digitoHexaIda(digito):
	digitos = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	for i in range(len(digitos)):
		if digito == digitos[i]:
			return i

def digitoHexaVolta(digito):
	digitos = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	for i in range(len(digitos)):
		if digito == numeros[i]:
			return digitos[i]

def binParaDec(numBin):
	decimal = 0
	expoente = 0

	while numBin > 0:
		decimal += 2**expoente * (numBin % 10)
		numBin //= 10
		expoente += 1

	return decimal

def octParaDec(numOct):
	decimal = 0
	expoente = 0

	while numOct > 0:
		decimal += 8**expoente * (numOct % 10)
		numOct //= 10
		expoente += 1

	return decimal

def decParaBin(numDec):
	binario = 0
	expoente = 0

	while numDec > 0:
		binario += 10**expoente * (numDec % 2)
		numDec //= 2
		expoente += 1

	return binario

def decParaOct(numDec):
	octal = 0
	expoente = 0

	while numDec > 0:
		octal += 10**expoente * (numDec % 8)
		numDec //= 8
		expoente += 1

	return octal

def decParaHex(numDec):
	hexadecimal = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	expoente = 0

	while numDec > 0:
		hexadecimal[(len(hexadecimal)-expoente)-1] = digitoHexaVolta(numDec % 16)
		numDec //= 16
		expoente += 1

	indexInicial = hexadecimal.count(' ')
	hexadecimal = hexadecimal[indexInicial:]
	hexadecimal = ''.join(hexadecimal)

	return hexadecimal

def hexParaDec(numHex):
	decimal = 0
	expoente = 0

	for i in range(len(numHex),0,-1):
		decimal += 16**expoente * digitoHexaIda(numHex[i-1])
		expoente += 1

	return decimal

def binParaHex(numBin):
	hexadecimal = decParaHex(binParaDec(numBin))
	return hexadecimal

def hexParaBin(numHex):
	binario = decParaBin(hexParaDec(numHex))
	return binario

def octParaBin(numOct):
	binario = decParaBin(octParaDec(numOct))
	return binario

def binParaOct(numBin):
	octal = decParaOct(binParaDec(numBin))
	return octal

def octParaHexa(numOct):
	hexadecimal = decParaHex(octParaDec(numOct))
	return hexadecimal

def hexaParaOct(numHex):
	octal = decParaOct(hexParaDec(numHex))
	return octal

print """		OPCOES DISPONIVEIS
	1   binario
	2   octal
 	3   decimal
 	4   hexadecimal
 	9   exibir operações validas
 	0   encerrar programa
	(ATENCAO: AS LETRAS HEXADECIMAIS DEVEM SER MAIUSCULAS)
	"""

escolha1 = ' '
escolha2 = ' '

while (escolha1 != '0' and escolha2 != '0'):	
	escolha1 = raw_input("Insira a opcao escolhida ou a base da entrada: ")
	if(escolha1 == '0'):
		escolha2 = '0'
		print("Programa encerrado\n")
	elif (escolha1 == '9'):
		print """		 OPCOES DISPONIVEIS
	1   binario
	2   octal
 	3   decimal
 	4   hexadecimal
 	9   exibir operações validas
 	0   encerrar programa
	(ATENCAO: AS LETRAS HEXADECIMAIS DEVEM SER MAIUSCULAS)
	"""
	elif (escolha1 != '1' and escolha1 != '2' and escolha1 != '3' and escolha1 != '4'):
		print "Insira uma opcao ou base valida.\n"
	else:
		escolha2 = raw_input("Insira a base da saida: ")
		if(escolha1 == escolha2):
			print "Insira base e saida diferentes.\n"
		elif(escolha1 == '1' and escolha2 == '2'):
			entrada = input("binario:")
			print "Valor octadecimal:" , (binParaOct(entrada)) , "\n"
		elif(escolha1 == '1' and escolha2 == '3'):
			entrada = input("binario:")
			print "Valor decimal:" , (binParaDec(entrada)) , "\n"
		elif(escolha1 == '1' and escolha2 == '4'):
			entrada = input("binario:")
			print "Valor hexadecimal:" , (binParaHex(entrada)) , "\n"
		elif(escolha1 == '2' and escolha2 == '1'):
			entrada = input("octal:")
			print "Valor binario:" , (octParaBin(entrada)) , "\n"
		elif(escolha1 == '2' and escolha2 == '3'):
			entrada = input("octal:")
			print "Valor decimal:" , (octParaDec(entrada)) , "\n"
		elif(escolha1 == '2' and escolha2 == '4'):
			entrada = input("octal:")
			print "Valor hexadecimal:" , octParaHexa(entrada) , "\n"
		elif(escolha1 == '3' and escolha2 == '1'):
			entrada = input("decimal:")
			print "Valor binario:" , decParaBin(entrada) , "\n"
		elif(escolha1 == '3' and escolha2 == '2'):
			entrada = input("decimal:")
			print "Valor octadecimal:" , decParaOct(entrada) , "\n"
		elif(escolha1 == '3' and escolha2 == '4'):
			entrada = input("decimal:")
			print "Valor hexadecimal:" , decParaHex(entrada) , "\n"
		elif(escolha1 == '4' and escolha2 == '1'):
			entrada = raw_input("hexadecimal:")
			print "Valor binario:" , hexParaBin(entrada) , "\n"
		elif(escolha1 == '4' and escolha2 == '2'):
			entrada = raw_input("hexadecimal:")
			print "Valor octadecimal:" , hexaParaOct(entrada) , "\n"
		elif(escolha1 == '4' and escolha2 == '3'):
			entrada = raw_input("hexadecimal:")
			print "Valor decimal:" , hexParaDec(entrada) , "\n"
		else:
			print "Insira bases validas."
