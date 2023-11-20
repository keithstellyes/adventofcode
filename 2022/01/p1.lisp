; common list
(let ((elf-sums '())
      (curr-elf 0)
      (max-elf 0))
  (with-open-file (stream "input")
    (loop for ln = (read-line stream nil 'eof)
	  until (eq ln 'eof)
	  collect (cond 
		    ((string= ln "") 
		     (push curr-elf elf-sums)
		     (if (> curr-elf max-elf) (setq max-elf curr-elf))
		     (setq curr-elf 0))
		    (t (setq curr-elf (+ curr-elf (parse-integer ln)))))))
  (princ max-elf))
