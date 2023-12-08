(load "shared.lisp")
(defparameter *inp* (parse-network (car *args*)))


(defparameter *dirs* (car *inp*))
(defparameter *graph* (cdr *inp*))

(print (walk "AAA" *dirs* *graph*))
