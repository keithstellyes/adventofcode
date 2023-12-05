; impl from Rosetta Code
(defun levenshtein (a b)
  (let* ((la  (length a))
	 (lb  (length b))
	 (rec (make-array (list (1+ la) (1+ lb)) :initial-element nil)))
    (labels ((leven (x y)
		    (cond
		      ((zerop x) y)
		      ((zerop y) x)
		      ((aref rec x y) (aref rec x y))
		      (t (setf (aref rec x y)
			       (min (+ (leven (1- x) y) 1)
				    (+ (leven x (1- y)) 1)
				    (+ (leven (1- x) (1- y)) (if (char= (char a (- la x)) (char b (- lb y))) 0 1))))))))
  (leven la lb))))

(defparameter *lines*
  (with-open-file (stream (car *args*))
    (loop for ln = (read-line stream nil 'eof)
	  until (eq ln 'eof)
	  collect ln)))


(let ((i 0) (j 1))
  (loop do
	(cond ((= 1 (levenshtein (elt *lines* i) (elt *lines* j)))
	       ; found! print results then exit
	       (progn (princ (elt *lines* i))
		      (terpri)
		      (princ (elt *lines* j)) (return)))
	      (t (if (= j (1- (length *lines*))) (progn (setf i (+ 1 i)) (setf j (+ 1 i))) (setf j (+ 1 j)))))))
