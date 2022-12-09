#include <iostream>
#include <cstdio>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int num, n, m;
	
	scanf("%d", &num);
	//I Dont Know
	n = num / 1000;
	m = m + n;
	num = num - n * 1000;
	n = num / 100;
	m = n + m;
	num = num - n * 100;
	n = num / 10;
	m = m + n;
	num = num - n * 10;
	m = m + num;

	printf("%d\n", m - 1);
	return 0;                                                   
}
