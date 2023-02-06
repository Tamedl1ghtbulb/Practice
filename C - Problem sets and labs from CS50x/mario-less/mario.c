#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 0;
    while (n < 1 || n>8)
    {
        n = get_int("Unesite velicinu piramide: ");
    }
    for (int i = 1; i < n+1 ; i++)
    {
        printf("%*s", n-i ,"");
        printf("%.*s", i, "########################################");
        printf("  ");
        printf("%.*s", i, "########################################");
        printf("\n");
    }
}