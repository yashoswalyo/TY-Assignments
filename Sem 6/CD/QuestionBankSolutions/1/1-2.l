%{
    /*
    * Subset of C language
    *
    */  
   int line=1;
%}
delim ["|']
letter [a-zA-Z]
number [0-9]
%%
"int"|"if"|"double"|"long"|"goto"|"static"|"float"|"short"|"while"|"char"|"const"|"void"|"else"|"return"|"printf"|"scanf" {printf("\n %d\t%s \t\tKeyword", line,yytext);}
"("|")"|"{"|"}"|"["|"]"|";"|"," {printf("\n %d\t%s \t\tDelimiter", line, yytext);}
"+"|"-"|"*"|"%"|"/"|"++"|"--" {printf("\n %d\t%s \t\tArithmetic Operator",line, yytext);}
"=="|"<"|">"|"<="|">=" {printf("\n %d\t%s \t\tRelational Operator",line, yytext);}
{delim} {printf("\n%s: Delimiter", yytext);}
"=" {printf("\n %d\t%s \t\tAssignment Operator",line, yytext);}
{letter}+|({letter}{number})* {printf("\n %d\t%s \t\tIdentifier",line, yytext);}
{number}+ {printf("\n %d\t%s\t\tConstant",line, yytext);}
{number}+{letter}+ {printf("\n %d\t%s \tERROR This is ILLEGAL",line,yytext);}
{delim}({letter}|{number})*{delim} {printf("\n %d\t%s \tString Constant/Literal",line,yytext);}
"\n" {line++;printf("\n");}
%%
