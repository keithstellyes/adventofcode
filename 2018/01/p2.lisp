; common lisp
; this can take a bit of time on the real input
(defparameter *freq* 0)
(defparameter *freq-history* '(0))
(defparameter *appears-twice* '())
(defun update-freq (d)
  (setq *freq* (+ *freq* d))
  (if (member *freq* *freq-history*)
  	(setq *appears-twice* (append *appears-twice* (list *freq*))))
  (setq *freq-history* (append *freq-history* (list *freq*))))

(defparameter *freq-changes*
(with-open-file (stream (car *args*))
    (loop for ln = (read-line stream nil 'eof) 
      until (eq ln 'eof) 
      collect (parse-integer ln))))

(loop  until *appears-twice* do (dolist (d *freq-changes*) (update-freq d))) 
(princ (car *appears-twice*))
