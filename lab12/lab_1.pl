% Andrew Thomas
% CS344 Lab12

killer(butch).
married(mia, marsellus).
dead(zed).
kills(marsellus, X) :- gives_massage(X, mia).
loves(mia, X) :- good_dancer(X).
eats(jules, X) :- is_nutritious(X); is_tasty(X).

/**
 * a. 
 *   i. A lot of my design choices are built around flexibility.
 *	 	For example, I could have had a loves_mia(X) test because
 * 		we only care about who Mia loves, but I wanted to be able to
 *		to expand if neccisary.
 *	 ii. It parses through the knowledge base to response
 *			1. Yes
 *			2. No (it knows nothing about witches)
 *			3. No (who is Hermione?)
 *			4. No (who is Hermione and what is a witch?)
 *			5. Yes (Harry is a quidditch player, therefore has a broom. Wizards have brooms and wands, just like Harry)
 *			6. Y = ron (Ron is the first wizard mentioned)
 *			7. No (still no idea what a witch is, it is probably sick of us asking)
 *
 * b. Yes it does. See below code. Prolog is pretty robust in its logical operations.
 */
 can_do_modes_ponens(me) :- is_good_at_logic(me).
 is_good_at_logic(me).

/**
 * c. Horn clauses cannot have more than one positive, but PL can.
 *		However, Horn clauses can contain varibles while PL cannot.
 * d. Yes. Ask operations end in a full stop, while tell statements do not.
 */