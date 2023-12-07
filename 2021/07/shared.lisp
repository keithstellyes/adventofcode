(load "~/quicklisp/setup.lisp")
(ql:quickload "cl-ppcre")

(defun parse-crabs (fn)
  (sort (with-open-file (stream fn)
	  (mapcar #'parse-integer
		  (remove-if #'(lambda (s) (= 0 (length s)))
			     (cl-ppcre:split "," (read-line stream))))) #'<))


