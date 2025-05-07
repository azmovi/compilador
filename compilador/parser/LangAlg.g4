grammar LangAlg;

// ------------- LEXER -------------
ALGORITMO      : 'algoritmo';
FIM_ALGORITMO  : 'fim_algoritmo';
DECLARE        : 'declare';
CONSTANTE      : 'constante';
TIPO           : 'tipo';
REGISTRO       : 'registro';
FIM_REGISTRO   : 'fim_registro';
FUNCAO         : 'funcao';
FIM_FUNCAO     : 'fim_funcao';
PROCEDIMENTO   : 'procedimento';
FIM_PROCEDIMENTO : 'fim_procedimento';
RETORNE        : 'retorne';

INTEIRO        : 'inteiro';
REAL           : 'real';
LITERAL        : 'literal';
LOGICO         : 'logico';
VERDADEIRO     : 'verdadeiro';
FALSO          : 'falso';

SE             : 'se';
ENTAO          : 'entao';
SENAO          : 'senao';
FIM_SE         : 'fim_se';

CASO           : 'caso';
SEJA           : 'seja';
FIM_CASO       : 'fim_caso';

ENQUANTO       : 'enquanto';
FACA           : 'faca';
FIM_ENQUANTO   : 'fim_enquanto';

PARA           : 'para';
ATE            : 'ate';
FIM_PARA       : 'fim_para';

LEIA           : 'leia';
ESCREVA        : 'escreva';

OP_LOG1        : 'ou';
OP_LOG2        : 'e';
OP_NOT         : 'nao';

ATRIB          : '<-';
OP_REL         : '=' | '<>' | '<=' | '>=' | '<' | '>';
OP_ARIT        : '+' | '-' | '*' | '/' | '%';

ABRE_PAR       : '(';
FECHA_PAR      : ')';
VIRGULA        : ',';
DOIS_PONTOS    : ':';
ABRE_COL       : '[';
FECHA_COL      : ']';

CADEIA         : '"' (~["\r\n])* '"' ;
NUM_REAL       : [0-9]+ ('.' [0-9]+)? ;
NUM_INT        : [0-9]+ ;
IDENT          : [a-zA-Z_][a-zA-Z_0-9]* ;

COMENTARIO     : '{' .*? '}' -> skip ;
WS             : [ \t\r\n]+       -> skip ;

// ------------- PARSER -------------

programa
    : declaracoes ALGORITMO bloco FIM_ALGORITMO EOF
    ;

bloco
    : declaracoes comandos
    ;

declaracoes
    : (decl_const
      | decl_var
      | decl_tipo
      | decl_proc
      | decl_func
      )*
    ;

decl_const
    : CONSTANTE IDENT DOIS_PONTOS tipo_basico ATRIB expressao
    ;

decl_var
    : DECLARE IDENT (VIRGULA IDENT)* DOIS_PONTOS tipo
    ;

decl_tipo
    : TIPO IDENT DOIS_PONTOS REGISTRO decl_var* FIM_REGISTRO
    ;

decl_proc
    : PROCEDIMENTO IDENT params? bloco FIM_PROCEDIMENTO
    ;

decl_func
    : FUNCAO IDENT params? DOIS_PONTOS tipo bloco FIM_FUNCAO
    ;

params
    : ABRE_PAR (IDENT DOIS_PONTOS tipo) (VIRGULA IDENT DOIS_PONTOS tipo)* FECHA_PAR
    ;

comandos
    : comando*
    ;

comando
    : LEIA ABRE_PAR args_leia FECHA_PAR
    | ESCREVA ABRE_PAR lista_expr FECHA_PAR
    | IDENT ATRIB expressao
    | SE expressao ENTAO comandos (SENAO comandos)? FIM_SE
    | CASO expressao SEJA selecao (SENAO comandos)? FIM_CASO
    | ENQUANTO expressao FACA comandos FIM_ENQUANTO
    | PARA IDENT ATRIB expressao ATE expressao FACA comandos FIM_PARA
    | RETORNE expressao
    ;

args_leia
    : IDENT (VIRGULA IDENT)*
    ;

lista_expr
    : expressao (VIRGULA expressao)*
    ;

selecao
    : (valor_const DOIS_PONTOS comandos)+
    ;

valor_const
    : NUM_INT (PONTO_PONTO NUM_INT)?
    | NUM_REAL
    | CADEIA
    | VERDADEIRO
    | FALSO
    ;

expressao
    : expr_logica
    ;

expr_logica
    : expr_term (OP_LOG1 expr_term)*
    ;

expr_term
    : expr_not (OP_LOG2 expr_not)*
    ;

expr_not
    : OP_NOT expr_not
    | expr_rel
    ;

expr_rel
    : expr_arit (OP_REL expr_arit)?
    ;

expr_arit
    : termo_arit (( '+' | '-' ) termo_arit)*
    ;

termo_arit
    : fator_arit (( '*' | '/' ) fator_arit)*
    ;

fator_arit
    : NUM_INT
    | NUM_REAL
    | IDENT
    | ABRE_PAR expressao FECHA_PAR
    ;

tipo
    : tipo_basico
    | IDENT               // alias ou registro
    | '^'? tipo_basico    // ponteiro
    ;

tipo_basico
    : INTEIRO
    | REAL
    | LITERAL
    | LOGICO
    ;
