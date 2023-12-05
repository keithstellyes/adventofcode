(defparameter *all-letters* "abcdefghijklmnopqrstuvwxyz")
(defun make-blank-ft ()
  (map 'list #'(lambda (c) (cons c 0)) *all-letters*))
(defun letter-freqs (ln)
  (let ((ft (make-blank-ft)))
    (loop for c across ln do
	  (push (cons c (+ 1 (cdr (assoc c ft)))) ft))
    (return-from letter-freqs ft)))

(defun checksum-dotted-pair (freqs)
  (cons (if (member 2 freqs) '1 '0) (if (member 3 freqs) '1 '0)))

(defun line-checksum (ln)
  (checksum-dotted-pair
    (map 'list  #'(lambda (c) (cdr (assoc c (letter-freqs ln))))
	 (remove-duplicates ln))))

(defparameter *checksum-pair*
  (reduce #'(lambda (a b) (cons (+ (car a) (car b)) (+ (cdr a) (cdr b))))
	  (with-open-file (stream (car *args*))
	    (loop for ln = (read-line stream nil 'eof)
		  until (eq ln 'eof)
		  collect (line-checksum ln)))))

(princ (* (car *checksum-pair*) (cdr *checksum-pair*)))
