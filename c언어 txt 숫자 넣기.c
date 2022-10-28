#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void main(int argc, char *argv[]) {
	FILE *out = fopen("NumberFile.txt", "w");
	int n, m;
	double d1, d2;
	
	if (out == NULL) {
		printf("No Such a file in Documents.");
		exit(1);
	}
	
	printf("정수2 : ");
	scanf("%d %d", &n, &m);
	printf("실수2 : ");
	scanf("%lf %lf", &d1, &d2);
	
	fprintf(out, "%d %d\n", n, m);
	fprintf(out, "%lf %lf", d1, d2);
	
	fclose(out);
}
