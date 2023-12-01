; common list
(defun firstandlast (s) 
  (coerce 
    (list
     (char s 0)
     (char s (1- (length s))))
    'string))
(let ((total 0)
      (max-elf 0))
  (with-open-file (stream (car *args*))
	  (princ (apply '+ 
			(mapcar #'parse-integer
				(mapcar #'firstandlast 
					(loop for ln = (read-line stream nil 'eof) 
					      until (eq ln 'eof) 
					      collect (remove-if-not #'digit-char-p ln))))))))
