%{
	#include <stdio.h>
	#include <math.h>
%}

%union	//to define possible symbol types
{double p;}
%token<p>num
%token SIN COS TAN LOG SQRT

%left '+''-'	//lowest precedence
%left '*''/'	//highest precedence
%nonassoc uminu	//no associativity
%type<p>exp	//Sets the type for non-terminal
%%

/*for storing the answer */
ss: exp {printf(" Answer = %g\n",$1);}

/* for binary arithmatic operators */
exp:	exp'+'exp   { $$=$1+$3; }
      |exp'-'exp  { $$=$1-$3; }
      |exp'*'exp  { $$=$1*$3; }
      |exp'/'exp  {
                      if($3==0)
                      {
                          printf("Divide by Zero");
                      }
                      else $$=$1/$3;
                  }
      |'-'exp         {$$=-$2;}
      |SIN'('exp')'   {$$=sin($3);}
      |COS'('exp')'   {$$=cos($3);}
      |TAN'('exp')'   {$$=tan($3);}
      |LOG'('exp')'   {$$ =log($3);}
      |SQRT'('exp')'  {$$ =sqrt($3);}
      |num;
      |'('exp')'      {$$=$2;}

%%

main()
{
	do
	{
    printf("\nExpression:");
		yyparse();	/* Parse the sentence repeatedly until the i/p runs out */
	}while(1);
}

yyerror(char *s;)   /* to print error message when an error is parsing of i/p */
{
  printf("Syntax Error");
} 
