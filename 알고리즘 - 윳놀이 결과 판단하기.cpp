#include <iostream>
#include <cstdio>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int a, b, c, d, i;
	
	//        작동 횟수 정하기 
	//              |
	for(i = 0; i <= 2;i++) {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		
		if(a + b + c + d == 3) {
			printf("A\n");
		}
		else if(a + b + c + d == 2) {
			printf("B\n");
		}
		else if(a + b + c + d == 1) {
			printf("C\n");
		}
		else if(a + b + c + d == 0) {
			printf("D\n");
		}
		else if(a + b + c + d == 4) {
			printf("E\n");
		}
	}
  
  //A = 도, B = 개, C = 걸, D = 윷, E = 모
	//0 = 배, 1 = 등
  
  
}
	return 0;
