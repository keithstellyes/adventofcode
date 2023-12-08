(load "shared.lisp")
(defparameter *inp* (parse-network (car *args*)))

(defparameter *dirs* (car *inp*))
(defparameter *graph* (cdr *inp*))

(defparameter *origins* (remove-if-not #'(lambda (node) (eq #\A (elt node 2))) (mapcar #'car *graph*)))

(print (reduce #'lcm (loop for origin in *origins*
      collect (walk origin *dirs* *graph*))))
