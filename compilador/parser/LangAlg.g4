grammar LangAlg;

ALGORITMO : 'algoritmo';
FIM_ALGORITMO : 'fim_algoritmo';
DECLARE : 'declare';
TIPO: 'tipo';
VAR: 'var';
CONSTANTE: 'constante';
REGISTRO: 'registro';
FIM_REGISTRO: 'fim_registro';

INTEIRO : 'inteiro';
REAL : 'real';
LITERAL : 'literal';
LOGICO : 'logico';
FALSO: 'falso';
VERDADEIRO: 'verdadeiro';
E: 'e';
OU: 'ou';
NAO: 'nao';

SE: 'se';
SENAO: 'senao';
ENTAO: 'entao';
FIM_SE: 'fim_se';
CASO: 'caso';
SEJA: 'seja';
FIM_CASO: 'fim_caso';

ENQUANTO: 'enquanto';
FIM_ENQUANTO: 'fim_enquanto';
PARA: 'para';
FIM_PARA: 'fim_para';
FACA: 'faca';
ATE: 'ate';

PROCEDIMENTO: 'procedimento';
FIM_PROCEDIMENTO: 'fim_procedimento';
FUNCAO: 'funcao';
FIM_FUNCAO: 'fim_funcao';
RETORNE: 'retorne';

LEIA : 'leia';
ESCREVA : 'escreva';

ATRIBUICAO: '<-';
IGUAL: '=';
DIFERENTE: '<>';
MAIOR: '>';
MENOR: '<';
MAIOR_IGUAL: '>=';
MENOR_IGUAL: '<=';

MAIS: '+';
MENOS: '-';
MULTIPLICACAO: '*';
DIVISAO: '/';
MOD: '%';

PONTEIRO: '^';
ENDERECO: '&';

ABREPAR: '(';
FECHAPAR: ')';
ABRECOL: '[';
FECHACOL: ']';
DOIS_PONTOS: ':';
VIRGULA: ',';
PONTO_PONTO: '..';
PONTO: '.';

CADEIA_NAO_FECHADA : '"' ( ~["\r\n] | '""' )*;
CADEIA : '"' ( ~["\r\n] | '""' )* '"';

NUM_INT : ('0'..'9')+;
NUM_REAL : ('0'..'9')+ ('.' ('0'..'9')+)?;

IDENT : [a-zA-Z_][a-zA-Z_0-9]*;

COMENTARIO_FECHADO : '{' ~('\n' | '\r' | '}')+ '}' -> skip;
COMENTARIO_NAO_FECHADO : '{' ~('}')+;
WS : [ \t\r\n ]+ -> skip;
ERR : . ;

programa
    : ALGORITMO declaracoes comandos FIM_ALGORITMO
    ;

declaracoes
    : (declaracao_var | declaracao_const | declaracao_subrotina)*
    ;

declaracao_var
    : DECLARE IDENT DOIS_PONTOS tipo
    ;

tipo
    : INTEIRO | REAL | LITERAL | LOGICO
    ;

declaracao_const
    : CONSTANTE IDENT DOIS_PONTOS tipo IGUAL expressao
    ;

declaracao_subrotina
    : procedimento
    | funcao
    ;

procedimento
    : PROCEDIMENTO IDENT (ABREPAR parametros? FECHAPAR)? declaracoes comandos FIM_PROCEDIMENTO
    ;

funcao
    : FUNCAO IDENT (ABREPAR parametros? FECHAPAR)? DOIS_PONTOS tipo declaracoes comandos FIM_FUNCAO
    ;

parametros
    : parametro (VIRGULA parametro)*
    ;

parametro
    : IDENT DOIS_PONTOS tipo
    ;

comandos
    : comando*
    ;

comando
    : leitura
    | escrita
    | atribuicao
    | se
    | caso
    | enquanto
    | para
    | chamadaProcedimento
    | retorne
    ;

leitura
    : LEIA ABREPAR IDENT FECHAPAR
    ;

escrita
    : ESCREVA ABREPAR listaExpressao FECHAPAR
    ;

listaExpressao
    : expressao (VIRGULA expressao)*
    ;

atribuicao
    : IDENT ATRIBUICAO expressao
    ;

se
    : SE expressao_logica ENTAO comandos (SENAO comandos)? FIM_SE
    ;

caso
    : CASO expressao SEJA seletores (SENAO comandos)? FIM_CASO
    ;

seletores
    : seletor+
    ;

seletor
    : valor_constante DOIS_PONTOS comandos
    ;

valor_constante
    : NUM_INT | CADEIA | VERDADEIRO | FALSO
    ;

enquanto
    : ENQUANTO expressao_logica FACA comandos FIM_ENQUANTO
    ;

para
    : PARA IDENT ATRIBUICAO expressao ATE expressao FACA comandos FIM_PARA
    ;

chamadaProcedimento
    : IDENT (ABREPAR listaExpressao? FECHAPAR)?
    ;

retorne
    : RETORNE expressao
    ;

expressao
    : expressao_aritmetica
    | expressao_logica
    ;

expressao_aritmetica
    : termo_aritmetico ((MAIS | MENOS) termo_aritmetico)*
    ;

termo_aritmetico
    : fator_aritmetico ((MULTIPLICACAO | DIVISAO | MOD) fator_aritmetico)*
    ;

fator_aritmetico
    : NUM_INT
    | NUM_REAL
    | IDENT
    | ABREPAR expressao_aritmetica FECHAPAR
    ;

expressao_logica
    : termo_logico ((OU) termo_logico)*
    ;

termo_logico
    : fator_logico ((E) fator_logico)*
    ;

fator_logico
    : NAO? relacional
    | VERDADEIRO
    | FALSO
    ;

relacional
    : expressao_aritmetica operador_relacional expressao_aritmetica
    ;

operador_relacional
    : IGUAL | DIFERENTE | MAIOR | MENOR | MAIOR_IGUAL | MENOR_IGUAL
    ;