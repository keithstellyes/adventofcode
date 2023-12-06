; Within  the interval of 0...racetime_ms there is a single sub-interval
; that wins. So, we try a value in this sub-interval, then use that as a bound
; to then perform two binary searches on the beginning and endings of said
; sub interval. The resulting margin of error is 1 + (nmax-nmin)

; will we win if we hold for n ms?
(defun buttonpress-p (racetime racedist n)
  (>= (* n (- racetime n)) racedist))

; is this the smallest possible nmin/nmax
(defun nmin-p (racetime racedist nmin)
  (and (buttonpress-p racetime racedist nmin) (not (buttonpress-p racetime racedist (- nmin 1)))))
(defun nmax-p (racetime racedist nmax)
  (and (buttonpress-p racetime racedist nmax) (not (buttonpress-p racetime racedist (+ nmax 1)))))

; just needs to find any winning option at all, so we can split
; the problem into two binary search problems
; this allows an upper bound for the binary search for nmin, and the
; lower bound for nmax
(defun find-winning-option (racetime racedist)
  (let ((queue (list (floor (/ racetime 2)))))
    (loop (let ((n (pop queue)))
	    (if (buttonpress-p racetime racedist n)
	      (return-from find-winning-option n)
	      (concatenate q (list (floor (/ (+ n racedist) 2)))))))))

; the min number of seconds button must be held:
; ceil(/ racetime racedist)
; a simple binary search.
(defun find-nmin (racetime racedist mid)
  (let ((l (floor (/ racedist racetime))) (r mid))
    (loop while (<= l r) do (let ((m (floor (/ (+ l r) 2))))
			      (if (nmin-p racetime racedist m) (return-from find-nmin m)
				(if (or
					(not (buttonpress-p racetime racedist m))
					(not (buttonpress-p racetime racedist (- m 1))))
				       (setf l (+ m 1))
				      (setf r (- m 1))))))))

; a simple binary search
(defun find-nmax (racetime racedist mid)
  (let ((l mid) (r (- racetime 1)))
    (loop while (<= l r) do (let ((m (floor (/ (+ l r) 2))))
			      (if (nmax-p racetime racedist m) (return-from find-nmax m)
				(if (or
					(not (buttonpress-p racetime racedist m))
					(not (buttonpress-p racetime racedist (+ m 1))))
				       (setf r (- m 1))
				      (setf l (+ m 1))))))))


(defun btnprs (racetime racedist)
  (btnprs-moe racetime racedist (ceiling (/ racetime racedist)) (- racedist 1)))

(defun moe (racetime racedist)
  (let ((m (find-winning-option racetime racedist)))
    (+ 1 (- (find-nmax racetime racedist m) (find-nmin racetime racedist m)))))
