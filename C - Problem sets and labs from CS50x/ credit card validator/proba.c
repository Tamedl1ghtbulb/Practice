#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    string ime = get_string("Unesite broj: ");
    char* endPtr;

    long bigNumber;
    int base =10;
    bigNumber = strtol(ime, &endPtr, base);
    printf("%ld\n",bigNumber);
}