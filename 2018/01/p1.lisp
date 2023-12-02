; common list
(let ((total 0))
  (with-open-file (stream (car *args*))
    (princ (apply '+ 
	(loop for ln = (read-line stream nil 'eof) 
	      until (eq ln 'eof) 
	      collect (parse-integer ln))))))
