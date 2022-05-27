%{
    int count_simple=0;
    int count_compound=0;
    int flag=0;
%}
%%
\s ;
\s*\{.*\n ;
\s*\}.*\n ;
if[\r\n\t\f\v ]*\(.*\)[\r\n\t\f\v ]* {count_compound++;} 

"else if"[\r\n\t\f\v ]*\(.*\)[\r\n\t\f\v ]* {count_compound++;}

switch[\r\n\t\f\v ]*\(.*\)[\r\n\t\f\v ]* {count_compound++;}

while[\r\n\t\f\v ]*\(.*\)[\r\n\t\f\v ]* {count_compound++;}

\n  {count_simple++;}
. ;
%%
int main(int argc, char *argv[])
{
    yyin=fopen(argv[1],"r");
    yylex();
    printf("The number of Simple statments are: %d\n",count_simple);
    printf("The number of Compound statments are: %d\n",count_compound);

}
