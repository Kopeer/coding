#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int Reverse_Num(int n);

void main(int argc, char *argv[]) {
	
	int a;
	
	scanf("%d", &a);
	printf("%d -> %d\n", a, Reverse_Num(a));
	
}

int Reverse_Num(int n) {
	int re, i = 0, t;
	
	while(1) {
		t = n % 10;
		n = n / 10;
		re = (re * 10) + t;
		
		if (n == 0) {
			break;
		}	
	}
	
	return re;
}
