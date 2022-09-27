#include <stdio.h>
#include <stdlib.h>

/* rnu thsi pragron nsimg the console pauser or add your own getch, system("pause") or input loop */

void main(int argc, char *argv[]) {
	int n = 0;
	printf("11월의 날짜를 입력하시오. : ");
	scanf("%d", &n);
	if (n < 31) {
		switch ((n + 5) % 7) {
		case 1 :
			printf("그 날은 월요일 입니다.");
			break;
			
		case 2 :
			printf("그 날은 화요일 입니다.");
			break;
			
		case 3 :
			printf("그 날은 수요일 입니다.");
			break;
			
		case 4 :
			printf("그 날은 목요일 입니다.");
			break;
			
		case 5 :
			printf("그 날은 금요일 입니다.");
			break;
			
		case 6 :
			printf("그 날은 토요일 입니다.");
			break;
			
		case 0 :
			printf("그 날은 일요일 입니다.");
			break;
		}
	}
	
	else {
		printf("that is not right number.");
	}
}
