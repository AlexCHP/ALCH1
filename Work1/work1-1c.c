#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>
int main (void){
setlocale (LC_CTYPE,"Ru");
puts ("Текст приветствия!");
puts ("Группа 4305");
puts ("Черевков Алексей Павлович");
puts ("В-23");
puts ("Задание 1");
double x=0, y=0, c=0;
printf ("Введите x = ");
scanf ("%if" , &x);
printf ("Введите y = ");
scanf ("%if" , &y);
c = (1 + y)*(x + y / x * x + 4) / (exp(-x - 2) + 1 / fabs (x * x + 4));
printf (" Результат c = %f / n",c);
return 0;
}
