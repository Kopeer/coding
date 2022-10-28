#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void main(int argc, char *argv[]) {
	FILE *in = fopen("StringFile.txt", "r");
	char str1[30];
	char str2[30];
	char str3[30];
	
	if ( in == NULL ) {
		printf("No Such a file in Documents.");
		exit(1);
	}
	
	fgets(str1, sizeof(str1), in);
	fgets(str2, sizeof(str2), in);
	fgets(str3, sizeof(str3), in);
	
	puts(str1);
	printf("%s", str2);
	
	fputs(str3, stdout);
	fclose(in);
	
}
