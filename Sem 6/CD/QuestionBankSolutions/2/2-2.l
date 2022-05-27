%{
    int count=0;
    int flag=0;
%}
%%

"//".*\n    { count++; }
\/\*[^*\/]*\*\/    { count++; }

%%

int main()
{
    yyin=fopen("input_with_comments.txt","r");
    yyout=fopen("output_without_comments.txt","w");
    yylex();
    fprintf(yyout, "\n\n NOTE: Number of comments removed : %d", count);
    return 0;
}

int yywrap()
{
    return 1;
}
