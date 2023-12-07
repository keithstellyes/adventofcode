(load "shared.lisp")

(defparameter *crabs* (parse-crabs (car *args*)))
(defparameter *median* (nth (floor (length *crabs*) 2) *crabs*))
(print (reduce '+ (mapcar #'(lambda (el) (abs (- *median* el))) *crabs*)))
