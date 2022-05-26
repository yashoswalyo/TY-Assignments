%{
    enum {
        LUKUP=0,
        VERB,
        NOUN
    };
    int state;
    int addWord(int type, char *word);
    int lookWord(char *word);
%}
%%
\n {state = LUKUP;}
^verb {state = VERB; }
^noun {state = NOUN; }
[a-zA-Z]+ {
    if(state!=LUKUP){
        addWord(state, yytext);
    } else {
        switch(lookWord(yytext)){
            case VERB:  printf("%s: verb\n", yytext); break;
            case NOUN:  printf("%s: noun\n", yytext); break;
            default: printf("Undefined"); break;
        }
    }
}
.
%%

struct word{
    char *word_name;
    int word_type;
    struct word *next;
};
struct word *word_list;
extern void *malloc();
int addWord(int type, char *word){
    struct word *wp;
    if(lookWord(word)!=LUKUP){
        printf("already defined");
        return 0;
    }
    wp = (struct word *) malloc (sizeof (struct word) ) ;
    wp->next = word_list;
    wp->word_name = (char *) malloc (strlen (word) +1);
    strcpy(wp->word_name,word);
    wp->word_type = type;
    word_list = wp;
    return 1;
}
int lookWord(char *word)
{
    struct word *wp = word_list;
    for (;wp;wp=wp->next){
        if(strcmp(wp->word_name, word) == 0) 
            return wp->word_type;
    }
    return LUKUP;
}
