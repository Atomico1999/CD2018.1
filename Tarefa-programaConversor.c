// Tarefa: criar conversor decimal-binario-hexadecimal
// 2 integrantes - tempo pra entrega: 10 dias
//
// Integrantes da equipe: NOME - MATRÍCULA
//	 Louis Ian Silva dos Santos - 402525
//	 Francisco Rodrigo Ferreira Uchôa - 403709 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define true 1
#define false 0
#define limpar() printf("\033[H\033[J")

int main(){
	
	long long int entrada, Q, R, aux1, maiorExpoente;
	saida = malloc(1000*sizeof(char));
	int continuar = true;
	int menu;

	printf("\n Programa conversor entre binários, decimais e hexadecimais.\n\n");

	while(continuar == true){
		
		for(int i = 0; i < 1000; i++){
			saida[i] = ""
		}
		aux1 = 1;
		Q = 0;
		R = 0;
		maiorExpoente = 0;

		printf("		MENU:\n");
		printf(" Digite 0 para fechar o programa;\n");
		printf(" Digite 1 para coverter de decimal para binário;\n");
		printf(" Digite 2 para coverter de binário para decimal;\n");
		printf(" Digite 3 para coverter de decimal para hexadecimal;\n");
		printf(" Digite 4 para coverter de hexadecimal para decimal;\n");
		printf(" Digite 5 para coverter de binário para hexadecimal;\n");
		printf(" Digite 6 para coverter de hexadecimal para binário;\n\n");

		printf("OPCAO:");
		scanf("%d", &menu);

		if(menu == 0){
			free(saida);
			continuar = false;

		} else if(menu == 1){
			
			printf("Insira o numero decimal a ser convertido: ");
			scanf("%lld", &entrada);

			while(entrada%aux1 > 9){
				aux1*= 10;
				maiorExpoente++;
			}

			for(int i = maiorExpoente; i > 0; ++i){
				R = entrada % 2;
				saida[maiorExpoente-i] = itoa(R);
				//aux1 = aux1 / 10;
				entrada = entrada / 2;
			};
			//saida += entrada;

			printf("O resultado binario e:%s\n", saida);
		
		} else if(menu == 2){
			
		} else if(menu == 3){
			
		} else if(menu == 4){
			
		} else if(menu == 5){
			
		} else if(menu == 6){
			
		} else {
			printf("Por favor insira um digito valido:\n");
			printf(" Digite 0 para fechar o programa;\n");
			printf(" Digite 1 para coverter de decimal para binário;\n");
			printf(" Digite 2 para coverter de binário para decimal;\n");
			printf(" Digite 3 para coverter de decimal para hexadecimal;\n");
			printf(" Digite 4 para coverter de hexadecimal para decimal;\n");
			printf(" Digite 5 para coverter de binário para hexadecimal;\n");
			printf(" Digite 6 para coverter de hexadecimal para binário;\n\n");
		}
	}
	
	return 0;
}