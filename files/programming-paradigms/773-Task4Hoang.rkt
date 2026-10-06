#lang racket

;; Q1
(define (delall a lst)
  (cond
    ((empty? lst) '()) ; base case: empty list
    ((list? (car lst)) ; if first element is a sublist
     (cons (delall a (car lst))
           (delall a (cdr lst))))
    ((equal? a (car lst)) ; if it matches the atom, remove it
     (delall a (cdr lst)))
    (else ; otherwise keep it
     (cons (car lst) (delall a (cdr lst))))))

;; Q2
(define (getextremes lst)
  (cond
    ((empty? (cdr lst)) (list (car lst) (car lst))) ; one element
    (else
     (let ((rest (getextremes (cdr lst))))
       (list
        (if (> (car lst) (car rest)) (car lst) (car rest)) ; max
        (if (< (car lst) (cadr rest)) (car lst) (cadr rest)))))))

;; Q3
(define (unite s1 s2)
  (cond
    ((empty? s1) s2)
    ((contains? (car s1) s2)
     (unite (cdr s1) s2))
    (else
     (cons (car s1) (unite (cdr s1) s2)))))

;; Q4
(define (checkset lst)
  (cond
    ((empty? lst) #t) ; empty list is a set
    ((contains? (car lst) (cdr lst)) #f) ; duplicate found
    (else (checkset (cdr lst))))) ; continue checking
