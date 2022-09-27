#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void main(int argc, char *argv[]) {

	int a[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}; //아무 숫자나 넣어도 작동 
	
	int i;
	for(i = 0; i < sizeof(a)/sizeof(a[0]); i++) {
		printf("%d ", a[i]);
	}
}
