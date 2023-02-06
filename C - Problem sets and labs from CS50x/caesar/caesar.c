#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    char rotate (char c, int n);
    bool only_digits(string s);
    if (argc!=2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    bool p = only_digits(argv[1]);
    if (!p)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //return 0;
    string m = argv[1];
    int broj = atoi(argv[1]);
    if (broj < 1 )
    {
        printf("Mozete uneti samo pozitivan broj kao kljuc!\n");
        return 1;
    }
    string plain = get_string("plaintext: ");
    int k = strlen(plain);
    printf("ciphertext: ");
    for (int i = 0 ; i < k;i++)
    {
        char w = rotate(plain[i], broj);
        printf("%c",w);
    }

printf("\n");
return 0;
}

bool only_digits(string s)
{
for (int i = 0; i < strlen(s); i++)
{
    if (!isdigit(s[i]))
    {
        return false;
    }
}
return true;
}


char rotate (char c, int n)
{
    char q;
    int brojk = ((n)%26);
    int ostatak = 0;
    if (islower(c)!=0)
    {
        if (c+brojk>122)
        {
            ostatak = brojk + c - 123;
            q = 'a'+ ostatak;
            return q;
        }
        else if (true)
        {
            q = c + brojk;
            return q;
        }
    }
    else if (isupper(c))
    {
        if (c+brojk>90)
        {
            ostatak = brojk + c - 91;
            q = 'A'+ ostatak;
            return q;
        }
        else if (true)
        {
            q = c+ brojk;
            return q;
        }
    }
    else if (true)
    {
        return c;
    }
}