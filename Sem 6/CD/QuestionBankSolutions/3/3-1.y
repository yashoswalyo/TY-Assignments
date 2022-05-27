%{
    #include<math.h>
    #include<stdio.h>
%}

%union {
    float fval;
}
%token <fval> NUMBER
%token END
%token SQRT
%left '+' '-'
%left '*' '/'
%right '^'
%left SQRT
%nonassoc UMINUS

%type <fval> expression
%%

statment: expression END  {printf(" = %.4f \n ", $1); return 0;}
    ;
expression: expression '+' expression { $$=$1+$3; }
    |expression '-' expression { $$ = $1 - $3; }
    |expression '*' expression { $$ = $1 * $3; }
    |expression '/' expression { 
        if($3 == 0.0)
            yyerror("divide by zero");
        else
            $$ = $1 / $3;
    }
    |SQRT expression {$$=sqrt($2);}
    |'-' expression %prec UMINUS { $$ = -$2; }
    |'(' expression ')' { $$=$2; }
    | NUMBER
    ;
%%
int main()
{
   do
	{
        printf("\nExpression: ");
        yyparse();	/* Parse the sentence repeatedly until the i/p runs out */
	}while(1);
}

int yyerror(char* s)
{
   printf("%s\n",s);
   return 0;
}

int yywrap()
{
   return 0;
}
