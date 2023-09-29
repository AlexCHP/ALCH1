#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>
int main (void){
setlocale (LC_CTYPE,"Ru");
puts ("Текст приветствия!");
puts ("Группа 4305");
puts ("Черевков Алексей Павлович");
puts ("В-23");
puts ("Задание 1");
double k=0, m=0, g=0;
printf ("Введите k = ");
scanf ("%if",&k);
printf ("Введите m = ");
scanf ("%if",&m);
if (k<m){
	g = sqrt (k * k + m) + 3 * abs (k);
  printf ("Результат % g / n, g"); 
		}
if (k>m) {
    g = sqrt (k + m * m * m) - 0,5 * abs (m-k);
 printf ("Результат % g  / n");
		}
else {
g = 2 * m * m - 0,5;
printf ("Результат  % g / n");
		}
return EXIT_SUCCESS;
}
