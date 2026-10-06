% Question 1: Return the final element of a list
final_element([X], X).

final_element([_|T], Last) :-
    final_element(T, Last).


% Question 2: Find the maximum number in a list
max_list_custom([X], X).

max_list_custom([H|T], Max) :-
    max_list_custom(T, TailMax),
    H >= TailMax,
    Max = H.

max_list_custom([H|T], Max) :-
    max_list_custom(T, TailMax),
    H < TailMax,
    Max = TailMax.


% Main method
:- initialization(main).

main :-
    final_element([apple, orange, banana, grape], Last),
    write('Final element: '),
    write(Last),
    nl,

    max_list_custom([3, 7, 2, 9, 5], Max),
    write('Maximum number: '),
    write(Max),
    nl,

    halt.