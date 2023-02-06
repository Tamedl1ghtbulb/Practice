#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void)
{
   // int zbir = 0;
    long broj = get_long("Unesite broj vase kartice: ");
    char brojk[21];
    sprintf(brojk,"%lu", broj);
  //  while (brojk[0]!= '3' || brojk[0]!= '4' || brojk[0]!= '5')
 //   {
  //      if (strlen(brojk)<13 || strlen(brojk) >16)
  //      {
  //          long sa = get_long("Unesite broj vase kartice: ");
   //         char brojk[21];
    //        sprintf(brojk,"%lu", broj);
      // }
    //}
    char* endPtr;
    long n;
    int base =10;
    n = strtol(brojk, &endPtr, base);
    int suma1 = 0;
    int suma2 = 0;
    long x = n;
    int ukupno = 0;
    int mod1;
    int mod2;
    int d1;
    int d2;
do
    {
        mod1 = x % 10;
        x = x / 10;
        suma1 = suma1 + mod1;
        mod2 = x % 10;
        x = x / 10;
        mod2 = mod2 * 2;
        d1 = mod2 % 10;
        d2 = mod2 / 10;
        suma2 = suma2 + d1 + d2;
    }
    while (x > 0);
    ukupno = suma1 + suma2;
    if (ukupno % 10 != 0)
    {
        printf("INVALID\n");
    }
   // printf("%i\n", zbir);
    else
    {
        if (strlen(brojk)==15 && brojk[0] =='3')
    {
        if (brojk[1]=='4' || brojk[1]=='7')
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (strlen(brojk)==16 && brojk[0] == '5' )
    {
        if(brojk[1]=='1' || brojk[1]=='2' ||brojk[1]=='3' || brojk[1]=='4'|| brojk[1]=='5')
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (strlen(brojk)>12 && strlen(brojk)<17 && brojk[0] == '4')
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
    }
    }