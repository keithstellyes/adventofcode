(load "shared.lisp")
; did they pick more than 12+13+14 cubes?
(defun round-picked-not-too-many-pieces? (round)
  (> 39 (apply '+ (mapcar #'car round))))

(defparameter *piece-limits* '(("red" . 12) ("green" . 13) ("blue" . 14)))

; e.g. 
; (15 "blue") => nil
; (1 "red") => t
(defun round-pick-not-too-many-of-a-color? (round-pick)
  ; common lisp assoc needs the :test to properly match strings
  (<= (car round-pick) 
      (cdr (assoc (cadr round-pick) *piece-limits* :test #'equal))))

(defun round-picked-not-too-many-of-a-color? (round)
  (every #'round-pick-not-too-many-of-a-color? round))

(defun round-satisfies-part1? (round)
  (and (round-picked-not-too-many-of-a-color? round) (round-picked-not-too-many-pieces? round)))

(defun game-satisfies-part1? (game)
  (every #'round-satisfies-part1? (cadr game)))

(defparameter *games*
  (with-open-file (stream (car *args*))
    (loop for ln = (read-line stream nil 'eof) 
	  until (eq ln 'eof) 
	  collect (parse-game ln))))

(print (apply '+ (mapcar #'car (remove-if-not #'game-satisfies-part1? *games*))))
