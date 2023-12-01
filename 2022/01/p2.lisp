; common list
(let ((elf-sums '())
      (curr-elf 0))
  (with-open-file (stream "input")
    (loop for ln = (read-line stream nil 'eof)
	  until (eq ln 'eof)
	  collect (cond
		    ((string= ln "")
		     (push curr-elf elf-sums)
		     (setq curr-elf 0))
		    (t (setq curr-elf (+ curr-elf (parse-integer ln)))))))
  (sort elf-sums #'>)
  (princ (apply '+ (subseq elf-sums 0 3))))
