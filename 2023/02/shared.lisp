(load "~/quicklisp/setup.lisp")
(ql:quickload "cl-ppcre")

; "1 blue"
; I think this should maybe be a cons instead of a list?
; was getting an error, used cons instead of list, put that dot inbetween
; then it was complaining about cadr not being a variable or something?
; need to come back to this
(defun parse-round-pick (round-pick) 
  (let ((parts (cl-ppcre:split " " round-pick)))
    (list (parse-integer (car parts)) (cadr parts))))

; ("1 blue" "2 red")
(defun parse-round-picks (round-picks)
  (loop for round-pick in round-picks collect (parse-round-pick round-pick)))

; "1 blue, 2 red"
(defun parse-round (round)
  (let ((endIndex (nth-value 1 (cl-ppcre:scan ":? " round))))
    (parse-round-picks (cl-ppcre:split ", " (subseq round endIndex)))))

; "Game 1: 1 blue, 2 red"
(defun parse-game (line) 
  (let ((game-id (cl-ppcre:scan-to-strings "[0-9]*" line :start 5)))
    (list (parse-integer game-id) (loop for round in (cl-ppcre:split ";" line :start (+ 5 (length game-id)))
					collect (parse-round round)))))
