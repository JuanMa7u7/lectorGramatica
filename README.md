# Analizador Lexico, Sintactico y Semantico de Gramatica tyny

## Gramatica en BNF
```
programa->secuencia_sent ;
secuencia_sent->sentencia secuencia_sent ;  
secuencia_sent->sentencia secuencia_sent ;  
secuencia_sent-> ;  
sentencia->sent_if ;  
sentencia->sent_repeat ;  
sentencia->sent_assign ;  
sentencia->sent_read ;  
sentencia->sent_write ;  
sent_if->if exp then secuencia_sent sent_if ;  
sent_if->end ;  
sent_if->else secuencia_sent end ;  
sent_repeat->repeat secuencia_sent until exp ;  
sent_assign->id := exp ;  
sent_read->read id ;  
sent_write->write exp ;  
exp->exp_simple exp ;  
exp->op_comparacion exp_simple ;  
exp-> ;  
op_comparacion->< ;  
op_comparacion->= ;  
exp_simple->term exp_simple ;  
exp_simple->opsuma term exp_simple ;  
exp_simple-> ;  
opsuma->+ ;  
opsuma->- ;  
term->factor term ;  
term->opmult factor term ;  
term-> ;  
opmult->* ;  
opmult->/ ;  
factor->( exp ) ;  
factor->intLiteral ;  
factor->id ;  
```



