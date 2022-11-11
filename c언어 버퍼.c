#include <stdio.h>
#include "a.h"
#define p printf

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int a;
	char b;
	
	scanf("%d", &a);
	getchar(); //없으면 애러 (엔터 누르면 끝남)
	scanf("%c", &b);
	p("%d, %c", a, b);
	
	return 0;
}
