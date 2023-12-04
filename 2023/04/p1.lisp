(load "shared.lisp")
(defun score-card (winning-numbers)
  (cond ((= winning-numbers 0) (return-from score-card 0))
	(t (expt 2 (- winning-numbers 1)))))

(defparameter *winning-numbers*
  (mapcar #'score-card (play-cards-file (car *args*))))

(print (reduce '+ *winning-numbers*))
