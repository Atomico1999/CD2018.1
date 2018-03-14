#-*- coding:utf-8 -*-
#Complado em python 2.7
#
# Tarefa: criar conversor decimal-binario-hexadecimal
# 2 integrantes - tempo estimado para entrega: 10 dias
#
# Integrantes da equipe: NOME - MATRÍCULA
#	 Louis Ian Silva dos Santos - 402525
#	 Francisco Rodrigo Ferreira Uchôa - 403709 

def binParaDec(numBin):
	decimal = 0
	expoente = 0

	while numBin > 0:
		decimal += 2**expoente * (numBin % 10)
		numBin //= 10
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

def decParaHex(numDec):
#	hexadecimal = ['0','0','0','0','0','0','0','0','0','0','0','0']
#	expoente = 0
#
#	while numDec > 0:
#		hexadecimal[(len(hexadecimal)-expoente)-1] = digitoHexaVolta(numDec % 16)
#		expoente += 1

	hexadecimal = hex(numDec)
	hexadecimal = hexadecimal[2:]

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

print """	 	OPÇÕES
	1   binario → decimal
	2   decimal → binario
 	3   decimal → hexadecimal
 	4   hexadecimal → decimal
 	5   binario → hexadecimal &
 	6   hexadecimal → binario."""

teste5 = input("binario:")
print(binParaHex(teste5))


"""		SUCESSO
teste1 = input("binario:")
print(binParaDec(teste1))

teste2 = input("decimal:")
print(decParaBin(teste2))

teste3 = input("decimal:")
print (decParaHex(teste3))

teste4 = raw_input("hexadecimal:")
print(hexParaDec(teste4))
"""