(load "shared.lisp")

; have initial minimums (in an assoc list?)
; iterate over rounds,
; for every round, iterate over round picks, updating minimum
(defun game-mins (game)
  (let ((mins '(("red" . 0) ("green" . 0) ("blue" . 0))))
    (loop for round in (cadr game) do 
	  (loop for rp in round do 
		(push 
		  (cons (cadr rp) . ((max (car rp) (cdr (assoc (cadr rp) mins :test #'string=))))) mins)))
    mins))

(defun game-mins-power (game-mins-list)
  (* (cdr (assoc "red" game-mins-list :test #'string=))
     (cdr (assoc "green" game-mins-list :test #'string=))
     (cdr (assoc "blue" game-mins-list :test #'string=))))

(print (reduce '+ (with-open-file (stream (car *args*))
		    (loop for ln = (read-line stream nil 'eof) 
			  until (eq ln 'eof) 
			  collect (game-mins-power (game-mins (parse-game ln)))))))
