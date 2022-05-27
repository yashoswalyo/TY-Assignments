%{
    int count = 0;
%}

letter [a-zA-Z]
%%
{letter}{letter}* {count++;}
[\t]+ ;
[\n] ;
. ;
%%
int main()
{
    yylex();

    printf("Number of words are : %d\n\n", count);
    return 0;
}

int yywrap()
{
    return(1);
}
