(load "~/quicklisp/setup.lisp")
(ql:quickload "cl-ppcre")

(defun parse-network (fn)
  (with-open-file (stream fn)
    (let ((dirs (read-line stream))
	  (nodes  (mapcar #'(lambda (ng) (cons (car ng) (list (cl-ppcre:split ", " (cadr ng)))))
			  (progn (read-line stream)
				 (loop for ln = (read-line stream nil 'eof)
				       until (eq ln 'eof)
				       collect (cl-ppcre:split " = "
							       (remove-if #'(lambda (c) (find c "()")) ln)))))))
      (return-from parse-network (cons dirs nodes)))))

(defun walk (pos dirs graph)
  (let ((index 0))
    (loop do
	  (progn
	    (if (eq #\L (elt *dirs* (mod index (length dirs))))
	      (setf pos (car (cadr (assoc pos graph :test #'string=))))
	      (setf pos (cadr (cadr (assoc pos graph :test #'string=)))))
	    (setf index (+ 1 index)))
	  until (eq (elt pos 2) #\Z))
    (return-from walk index)))


