// Chibi Konoha
// by Kimio Kuramitsu
example Program '''
fib(n) = if n < 3 then 1 else fib(n-1)+fib(n-2)
print(fib(10))
'''
Program = {
  Statement*
  #Block
} EOF
EOF = !.
Statement = FuncDecl / LetDecl / Expression
_ = [ \t\r\n]*
FuncDecl = {
  Name '(' _ Name ')' _ '=' _ Expression
  #FuncDecl
} _
LetDecl = {
  Name '=' _ Expression
  #LetDecl
} _
example Expression if a == 1 then print(a) else 0
example Expression f(a+1)
example Expression 1+2*3
example Expression 1*2+3
example Expression 1-2-3
example Expression 1+2-3
Expression = IfExpr / Cmpr
IfExpr = {
  'if' _ Expression 
  'then' _ Expression 
  'else' _ Expression
  #If
}
Cmpr = { Sum '==' _ Sum #Eq}
  / { Sum '!=' _ Sum #Ne}
  / { Sum '<' _ Sum #Lt}
  / { Sum '>' _ Sum #Gt}
  / { Sum '<=' _ Sum #Lte}
  / { Sum '>=' _ Sum #Gte}
  / Sum
/*
Sum = { Prod ('+' _ Prod)+ #Add}
  / { Prod ('-' _ Prod)+ #Sub}
  / Prod
*/
/*
Prod = { Term ('*' _ Term)+ #Mul}
  / { Term ('/' _ Term)+ #Div}
  / Term
*/
Sum = Prod ( ^{ '+' Prod #Add } / ^ { '-' _ Prod #Sub} )*
Prod = Term ( ^{ '*' Term #Mul } / ^{ '/' _ Term #Div} )*
Term = FuncApp / Name / Value / '(' _ Expression ')' _
FuncApp = {
  Name '(' _ Expression ')' _
  #FuncApp
}
example Name x
example Name x2
Name = {
  [A-Za-z] [A-Za-z0-9]* 
  #Var
} _
example Value 0
example Value 10
Value = {
  [0-9]+ 
  #Int
} _
