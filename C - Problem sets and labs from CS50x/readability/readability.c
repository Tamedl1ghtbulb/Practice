#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    int count_letters(string x);
    int count_words(string x);
    int count_sentences(string x);
    int breci = 1;
    int brecenice = 0;
    int bslova= 0;
    string btekst = get_string("Text:");
    bslova = count_letters(btekst);
    breci = count_words(btekst);
    brecenice = count_sentences(btekst);
    double L = (float)bslova / (float)breci *100;
    double S = (float)brecenice / (float)breci *100;
    float index = 0.0588 * (float)L - 0.296 * (float)S - 15.8;
    int indexx = round(index);
    if (indexx > 16)
    {
      printf("Grade 16+\n");
    }
    else if (indexx <1)
    {
      printf("Before Grade 1\n");
    }
    else
    {
      printf("Grade %i\n", indexx);
    }
}




int count_letters(string tekst)
{
    int slova = 0;
    for (int i = 0 ; i <strlen(tekst);i++)
    {
        if (isalpha(tekst[i]))
        {
            slova +=1;
        }
    }
    return slova;
}

int count_words(string tekst)
{
    int reci = 1;
    for (int i = 0 ; i<strlen(tekst); i++)
    {
        if (isspace(tekst[i]))
        {
            reci+= 1;
        }
    }
    return reci;
}

int count_sentences(string tekst)
{
    int recenice = 0;
    for (int i = 0; i< strlen(tekst); i++)
    {
      if(tekst[i]=='.' || tekst[i]=='!' || tekst[i]=='?')
      {
        recenice +=1;
      }
    }
    return recenice;
}


















//{
//
  //  for (int i = 0 ; i< strlen(tekst); i++)
   // {
//        if (strcmp(tekst[i]," "==0)
//        {
//            reci +=1;
 //       }
 //       else if (strcmp(tekst[i],) ".")
 //       {
  //          recenice +=1
    //    }
      //  else if (strcmp(tekst[i],) "!")
//        {
  //          recenice +=1
    //    }
//        else if (strcmp(tekst[i],) "?")
  //      {
    //        recenice +=1
      //  }
//        else
  //      {
    //        slova +=1
      //  }
//    }
//}