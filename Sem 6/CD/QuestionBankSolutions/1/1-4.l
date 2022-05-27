digit [0-9]
letter [A-Za-z_]

%{
    //This is a lexical analyzer for a subset of C language
    #include <stdio.h>
    #include <string.h>
    int lno = 1;
    char symtab[100][100];
    int symtabidx = 0;
    void handle_symtab(char*);
    void print_symtab();
    char match[100];

    //to run the file use following commands
    // 1. lex 1_4.l
    // 2. gcc lex.yy.c
    // 3. ./a.out c.txt
%}

%%

[\t]+ ;

int |
float |
double |
String |
char |
if |
for |
else |
do |
while |
printf |
static |
void |
public {fprintf(yyout,"%s\t\t%d\t\tKeyword\n", yytext, lno);}

; |
, |
\" |
\' |
: |
\{ |
\} |
\( |
\) {fprintf(yyout,"%s\t\t%d\t\tDelimiter\n", yytext, lno);}

\+ |
\- |
\* |
\/ |
\^ {fprintf(yyout,"%s\t\t%d\t\tOperator\n", yytext, lno);}

\= |
\> |
\< |
\|\| |
\&\& |
\>\= |
\<\= |
\! |
\!\= {fprintf(yyout,"%s\t\t%d\t\tLogical Operator\n", yytext, lno);}

{letter}({letter}|{digit})* {fprintf(yyout,"%s\t\t%d\t\tIdentifier\n", yytext, lno);
                             strcpy(match, yytext);
                             handle_symtab(match);}

{digit} |
{digit}.{digit} {fprintf(yyout,"%s\t\t%d\t\tConstant\n", yytext, lno);}

\"[^"\n]*\" {   strncpy(match, &yytext[1], strlen(yytext) - 2);
                fprintf(yyout, "\"\t\t%d\t\tDelimiter\n", lno);
                fprintf(yyout, "%s\t\t%d\t\tConstant\n", match, lno);
                fprintf(yyout, "\"\t\t%d\t\tDelimiter\n", lno);
}


[\n] {lno++;}

%%

int main(int argc, char *argv[])
{

    extern FILE *yyout;
    yyin = fopen(argv[1], "rb+");

    yyout = fopen("output.txt", "w");
    fprintf(yyout, "Token Listing for Subset of C languages\n");
    fprintf(yyout, "Lexeme\tLine\t\tToken\n");

    yylex();

    print_symtab();

    fclose(yyout);

    return 0;
}

void handle_symtab(char *text)
{
    for (int i = 0; i<symtabidx; i++)
    {
        if(strcmp(symtab[i], text) == 0)
            return ;
    }
    strcpy(symtab[symtabidx++], text);
}

void print_symtab()
{
    fprintf(yyout, "\n\nSymbol Table\n");
    fprintf(yyout,"Index\t\tSymbol\n");
    for(int i=0;i<symtabidx;i++)
    {
        fprintf(yyout, "%d\t\t%s\n", (i+1), symtab[i]);
    }
}

int yywrap()
{
    return(1);
}
