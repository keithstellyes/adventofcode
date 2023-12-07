(load "shared.lisp")

(defun sigma (n)
  (ash (* n (+ n 1)) -1))
(defparameter *crabs* (parse-crabs (car *args*)))
; example math wants ceil, input wants floor
(defparameter *mean* (floor (/ (reduce '+ *crabs*) (length *crabs*))))
(defparameter *s1* (reduce '+ (mapcar #'(lambda (crab) (sigma (abs (- crab *mean*)))) *crabs*)))
(defparameter *s2* (reduce '+ (mapcar #'(lambda (crab) (sigma (abs (- crab (+ 1 *mean*))))) *crabs*)))
(print (min *s1* *s2*))
