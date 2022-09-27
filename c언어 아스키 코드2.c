#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void main(int argc, char *argv[]) {
	char ch;
	
	printf("문자를 입력하세요 : ");
	ch = getchar();                  // 키보드에서 문자를 받아온다.
	putchar(ch);                     // 문자를 출력한다. 
	printf("%c %d\n", ch, ch);
	
}
