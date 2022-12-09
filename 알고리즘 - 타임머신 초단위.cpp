#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int H, M, S, s;
	int time;
	
	scanf("%d %d %d", &H, &M, &S);
	
	scanf("%d", &time);
	
	s = S + M * 60 + H * 3600;
	s = s - time;
	H = s/3600;
	M = (s % 3600)/60;
	S = s % 60;
	printf("%d %d %d", H, M, S);
		
	return 0;
}
