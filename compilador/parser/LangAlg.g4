lexer grammar LangAlg;

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
