grammar LangAlg;

// -------- Palavras-chave --------
ALGORITMO         : 'algoritmo';
FIM_ALGORITMO     : 'fim_algoritmo';
DECLARE           : 'declare';
CONSTANTE         : 'constante';
TIPO              : 'tipo';
REGISTRO          : 'registro';
FIM_REGISTRO      : 'fim_registro';
FUNCAO            : 'funcao';
FIM_FUNCAO        : 'fim_funcao';
PROCEDIMENTO      : 'procedimento';
FIM_PROCEDIMENTO  : 'fim_procedimento';
RETORNE           : 'retorne';

INTEIRO           : 'inteiro';
REAL              : 'real';
LITERAL           : 'literal';
LOGICO            : 'logico';
VERDADEIRO        : 'verdadeiro';
FALSO             : 'falso';
VAR               : 'var';

SE                : 'se';
ENTAO             : 'entao';
SENAO             : 'senao';
FIM_SE            : 'fim_se';
CASO              : 'caso';
SEJA              : 'seja';
FIM_CASO          : 'fim_caso';
ENQUANTO          : 'enquanto';
FACA              : 'faca';
FIM_ENQUANTO      : 'fim_enquanto';
PARA              : 'para';
ATE               : 'ate';
FIM_PARA          : 'fim_para';
LEIA              : 'leia';
ESCREVA           : 'escreva';

// -------- Operadores lógicos --------
OP_OU             : 'ou';
OP_E              : 'e';
OP_NAO            : 'nao';

// -------- Ponteiro ----------
PONTEIRO          : '^';

// -------- Endereço ----------
ENDERECO          : '&';

// -------- Atribuição --------
ATRIB             : '<-';

// -------- Operadores relacionais --------
IGUAL             : '=';
DIFERENTE         : '<>';
MENOR_IGUAL       : '<=';
MAIOR_IGUAL       : '>=';
MENOR             : '<';
MAIOR             : '>';

// -------- Operadores aritméticos --------
MAIS              : '+';
MENOS             : '-';
MULT              : '*';
DIV               : '/';
MOD               : '%';

// -------- Símbolos --------
ABRE_PAR          : '(';
FECHA_PAR         : ')';
VIRGULA           : ',';
PONTO             : '.';
DOIS_PONTOS       : ':';
PONTO_PONTO       : '..';
ABRE_COL          : '[';
FECHA_COL         : ']';

// -------- Literais e identificadores --------
CADEIA            : '"' ~('"' | '\n')* '"';
NUM_REAL          : [0-9]+ '.' [0-9]+ ;
NUM_INT           : [0-9]+ ;
IDENT             : [a-zA-Z_][a-zA-Z_0-9]* ;

// -------- Comentário e espaços em branco --------
COMENTARIO        : '{' ~('{' | '}')* '}'  -> skip;
WS                : [ \t\r\n]+ -> skip ;

// -------- Erros ---------
CADEIA_NAO_FECHADA     : '"' ~('"')* ( '\n' | EOF);
COMENTARIO_NAO_FECHADO : '{' ~('}')* ( '{' | EOF );
ERRO                   : . ;

// ----------- Parser -----------

programa
    : (declaracao_global | declaracao_local)* ALGORITMO corpo FIM_ALGORITMO
    ;

corpo
    : declaracao_local* cmd*
    ;

declaracao_local
    : DECLARE variavel
    | CONSTANTE IDENT DOIS_PONTOS tipo_basico IGUAL valor_constante
    | TIPO IDENT DOIS_PONTOS tipo
    ;

declaracao_global
  : (PROCEDIMENTO | FUNCAO) IDENT ABRE_PAR parametros? FECHA_PAR
    (DOIS_PONTOS tipo_estendido)? corpo (FIM_PROCEDIMENTO | FIM_FUNCAO)
  ;

variavel
    : identificador (VIRGULA identificador)* DOIS_PONTOS tipo
    ;

identificador
    : IDENT (PONTO IDENT)* dimensao
    ;

dimensao
    : (ABRE_COL exp_aritmetica FECHA_COL)*
    ;

tipo
    : registro
    | tipo_estendido
    ;

tipo_basico
    : LITERAL
    | INTEIRO
    | REAL
    | LOGICO
    ;

tipo_estendido
    : PONTEIRO? (tipo_basico | IDENT)
    ;

valor_constante
    : CADEIA
    | NUM_INT
    | NUM_REAL
    | VERDADEIRO
    | FALSO
    ;

registro
    : REGISTRO variavel* FIM_REGISTRO
    ;

parametro
    : VAR? identificador (VIRGULA identificador)* DOIS_PONTOS tipo_estendido
    ;

parametros
    : parametro (VIRGULA parametro)*
    ;

cmd
    : cmdLeia
    | cmdEscreva
    | cmdSe
    | cmdCaso
    | cmdPara
    | cmdEnquanto
    | cmdFaca
    | cmdAtribuicao
    | cmdChamada
    | cmdRetorne
    ;

cmdLeia
    : LEIA ABRE_PAR PONTEIRO? identificador (VIRGULA PONTEIRO? identificador)* FECHA_PAR
    ;

cmdEscreva
    : ESCREVA ABRE_PAR expressao (VIRGULA expressao)* FECHA_PAR
    ;

cmdSe
    : SE expressao ENTAO cmd* (SENAO cmd*)? FIM_SE
    ;

cmdCaso
    : CASO exp_aritmetica SEJA selecao (SENAO cmd*)? FIM_CASO
    ;

cmdPara
    : PARA IDENT ATRIB exp_aritmetica ATE exp_aritmetica FACA cmd* FIM_PARA
    ;

cmdEnquanto
    : ENQUANTO expressao FACA cmd* FIM_ENQUANTO
    ;

cmdFaca
    : FACA cmd* ATE expressao
    ;

cmdAtribuicao
    : PONTEIRO? identificador ATRIB expressao
    ;

cmdChamada
    : IDENT ABRE_PAR expressao (VIRGULA expressao)* FECHA_PAR
    ;

cmdRetorne
    : RETORNE expressao
    ;

selecao
    : item_selecao*
    ;

item_selecao
    : constantes DOIS_PONTOS cmd*
    ;

constantes
    : numero_intervalo (VIRGULA numero_intervalo)*
    ;

numero_intervalo
    : op_unario? NUM_INT (PONTO_PONTO op_unario? NUM_INT)?
    ;

op_unario
    : MENOS
    ;

exp_aritmetica
    : termo (op1 termo)*
    ;

termo
    : fator (op2 fator)*
    ;

fator
    : parcela (op3 parcela)*
    ;

op1
    : MAIS
    | MENOS
    ;

op2
    : MULT
    | DIV
    ;

op3
    : MOD
    ;

parcela
    : op_unario? parcela_unario
    | parcela_nao_unario
    ;

parcela_unario
    : PONTEIRO? identificador
    | IDENT ABRE_PAR expressao (VIRGULA expressao)* FECHA_PAR
    | NUM_INT
    | NUM_REAL
    | ABRE_PAR expressao FECHA_PAR
    ;

parcela_nao_unario
    : ENDERECO identificador
    | CADEIA
    ;

exp_relacional
    : exp_aritmetica (op_relacional exp_aritmetica)?
    ;

op_relacional
    : IGUAL
    | DIFERENTE
    | MAIOR_IGUAL
    | MENOR_IGUAL
    | MAIOR
    | MENOR
    ;

expressao
    : termo_logico (op_logico_1 fator_logico)*
    ;

termo_logico
    : fator_logico (op_logico_2 fator_logico)*
    ;

fator_logico
    : OP_NAO? parcela_logica
    ;

parcela_logica
    : ( VERDADEIRO | FALSO )
    | exp_relacional
    ;

op_logico_1
    : OP_OU
    ;

op_logico_2
    : OP_E
    ;
