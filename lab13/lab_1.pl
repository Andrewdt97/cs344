% Andrew Thomas
% CS 344 Lab13

%3.2
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(Z, Y), in(X, Z).

%4.5
tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

listtran([],[]).
listtran([H | T], [H2 | T2]) :- tran(H, H2), listtran(T, T2).

% Yes it can. Generalized modus ponens works for Horn clauses.
% Since Prolog only utilizes horn clauses, it implements modus ponens.
alive(X) :- isTyping(X).
isTyping(Andrew).
alive(Andrew).