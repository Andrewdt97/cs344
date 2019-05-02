% Andrew Thomas
% CS 344

can_burn(X) :- made_of_wood(X).
made_of_wood(X) :- does_float(X).
does_float(X) :- weighs_as_duck(X).
witch(X) :- can_burn(X).

weighs_as_duck(woman).