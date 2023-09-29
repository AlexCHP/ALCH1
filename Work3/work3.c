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
double y = 0 , x=0, h=0.1;
printf ("Введите x  = ");
scanf ("%if",&x);
if (x > 0 && x < 1);{
  y = (sin (2 * x)) / x;
  printf ("Результат %y / n, y");
		};
if (x == 0);{
y = 2;
 printf ("Результат %y / n, y");}
 if (x > -1 && x < 0); {
	y = 2 * exp( -x ) * cos ( x );
	printf ("Результат %y / n, y");}
	return EXIT_SUCCESS;}

