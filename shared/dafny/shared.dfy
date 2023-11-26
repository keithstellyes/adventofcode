module AOCShared {
	newtype int32 = i | -0x80000000 <= i < 0x80000000
	newtype uint = i | i >= 0
	predicate seqHasNoNegatives(s: seq<int>) {
		forall i | 0 <= i < |s| :: s[i] > 0
	}

	lemma subsetSmaller(s: seq<int>)
		requires seqHasNoNegatives(s)
		ensures forall n | 0 <= n < |s| :: s[n] <= sumSeqR(s) 
		ensures |s| <= 1 || s[0] + sumSeqR(s[1..]) == sumSeqR(s)
	{
		
	}

	function sumSeqR(s: seq<int>):  (result: int)
	ensures (s == [] && result == 0) || s != []
	ensures (s == [0] && result == 0) || s != [0]
	ensures (s == [0, 1] && result == 1) || s != [0, 1]
	ensures (s == [1, 2, 3] && result == 1 + sumSeqR([2, 3])) || s != [1, 2, 3]
	ensures (s == [1, 2, 3] && result == 6) || s != [1, 2, 3]
	ensures (seqHasNoNegatives(s) && result >= 0) || !seqHasNoNegatives(s)
	{
		if |s| == 0 then 0
		else s[0] + sumSeqR(s[1..])
	}

	function maxBetweenTwoInts(a: int, b: int): (result: int)
	ensures a < b || maxBetweenTwoInts(a, b) == a
	{
		if a >= b then a
		else b
	}

	lemma maxer(s: seq<int>)
	requires |s| > 2
	decreases |s|
	ensures |s| < 2 || forall n | 1 <= n < |s| :: (max(s[..n]) < max(s)) ==> max(s) !in s[..n]
	ensures |s| < 2 || forall n | 1 <= n < |s| :: (max(s[..n]) == max(s)) ==> (max(s) in s[..n])
	ensures |s| < 2 || forall n | 1 <= n < |s| :: (max(s[..n]) != max(s)) ==> (max(s) in s[n..]) && max(s) !in s[..n]
	{
		assert(forall n | 0 <= n < |s| :: max([n]) == n);
		assert(forall l, n | 0 < |l| < |s| :: (max(l) == n) ==> n in l);
		assert(forall a, b | a in s && b in s && |s| > 2 :: max([a, b]) == max([b, a]));
		assert(forall l, n | 0 < |l| < |s| && n in l :: (max(l) < n) ==> n !in l);
		assert(forall l, m | 0 < |l| < |s| && 0 < |m| < |s| :: (max(l) < max(m)) ==> max(m) !in l);
		assert(forall l, m | 0 < |l| < |s| && 0 < |m| < |s| :: (max(l) == max(m)) ==> max(m) in l && max(l) in m);

		assert(|s| <= 1 || 1 + |s[1..]| == |s|);
		assert(|s| <= 1 || 1 <= |s[1..]|);
		assert(|s| <= 1 || |s[1..]| < |s|);
		if exists l : seq<int> :: |l| > 0 && |s[1..]| > |s| {
			assert false;
		}
		if exists n : int :: 1 <= n < |s| && max(s[..n]) > max(s) {
			assert false;
		}
		if exists n : int :: 1 <= n < |s| && max(s[..n]) == max(s) && max(s) !in s[..n] {
			assert false;
		}

		// want to do a proof by contradiction, see:
		// https://dev.to/hath995/writing-lemmas-in-dafny-55ai
	}
	
	function max (s: seq<int>): (result: int)
	requires |s| > 0
	decreases |s| - 1
	ensures |s| == 1 || forall i | 0 <= i < |s| :: result >= s[i]
	// these two ensures wnat to prove that:
	// if the max of one side of an array is the same as the max of the whole array,
	// then the max is in that one side
	ensures |s| < 2 || forall n | 1 <= n < |s| :: (max(s[..n]) < max(s)) ==> max(s) !in s[..n]
	ensures max(s) in s
	ensures |s| > 1 || |s| < |s[1..]|
	ensures |s| < 2 || forall n | 1 <= n < |s| - 2:: (max(s[..n]) == max(s)) ==> (max(s) in s[..n])
	ensures |s| < 2 || forall n | 1 <= n < |s| - 2:: (max(s[..n]) != max(s)) ==> (max(s) in s[n..]) && max(s) !in s[..n]
	ensures |s| <= 2 || forall a, b | a < b && a in s && b in s :: max([a, b]) == b && max([b, a]) == b
	ensures |s| <= 3 || forall a, b, c | a <= b < c && a in s && b in s && c in s && c != b :: max([a, b, c]) == c
	{
		maxer(s[1..]);
		match |s| {
			case 1 => s[0]
			case 2 => if s[0] >= s[1] then s[0] else s[1]
			case _ => if s[0] >= max(s[1..]) then s[0] else max(s[1..])
		}
	}

	method sumSeq(s: seq<int>)  returns (total: int)
	//ensures total == sumSeqR(s)
	{
		var i := 0;
		while i < |s| {
			total := total + s[i];
			i := i + 1;
		}
		return total;
	}

	predicate sorted(a: seq<int>) {
  		forall j, k :: 0 <= j < k < |a| ==> a[j] <= a[k]
	}

	predicate isMax(x: int, s: seq<int>) {
		forall i | 0 <= i < |s| :: s[i] <= x
	}
}