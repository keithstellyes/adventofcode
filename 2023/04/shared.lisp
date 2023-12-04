(load "~/quicklisp/setup.lisp")
(ql:quickload "cl-ppcre")

(defun play-cards-file (fn)
  (with-open-file (stream fn)
    (loop for ln = (read-line stream nil 'eof)
	  until (eq ln 'eof)
	  collect (length (play-card (parse-card ln))))))


; a list that looks like: ((scratched numbers) (winning numbers))
(defun parse-card (ln)
  (mapcar #'parse-space-integer-list (cl-ppcre:split " \\| " (subseq ln (+ 2 (search ":" ln))))))

(defun parse-space-integer-list (space-separated-list)
  (mapcar #'parse-integer
	  (remove-if #'(lambda (s) (= 0 (length s)))
		     (cl-ppcre:split "\\s+" space-separated-list))))

(defun play-card (card)
  (remove-if-not #'(lambda (num) (member num (cadr card)))
		 (car card)))


