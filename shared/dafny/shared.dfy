module AOCShared {
	newtype int32 = i | -0x80000000 <= i < 0x80000000
	newtype uint = i | i >= 0
	predicate seqHasNoNegatives(s: seq<int>) {
		forall i | 0 <= i < |s| :: s[i] > 0
	}

	function sumSeqR(s: seq<nat>):  (result: nat)
	{
		if |s| == 0 then 0
		else s[0] + sumSeqR(s[1..])
	}

	lemma sumSeqLemma(a: seq<nat>, b: seq<nat>) 
		ensures sumSeqR(a+b) == sumSeqR(a)+sumSeqR(b)
	{
		if a == [] {
			assert a + b == b;
		}
		else {
			sumSeqLemma(a[1..], b);
			calc {
			sumSeqR(a + b);
			{
				assert (a + b)[0] == a[0];
				assert (a + b)[1..] == a[1..] + b;
			}
			a[0] + sumSeqR(a[1..] + b);
			a[0] + sumSeqR(a[1..]) + sumSeqR(b);
			}
		}
	}

	function maxOf(a: int, b: int): int
	{
		if a >= b then a
		else b
	}

	function seqMax(s: seq<int>):int 
		requires |s| >= 1
		ensures forall x :: x in s ==> seqMax(s) >= x
		ensures seqMax(s) in s
	{
		if |s| == 1 then 
			s[0] 
		else if |s| == 2 then 
			maxOf(s[0], s[1])
		else 
			var rest:=seqMax(s[1..]);
			var res:=maxOf(s[0], rest);
			assert forall x :: x in s ==> res >= x by {
				forall x | x in s 
					ensures res >= x
				{
					if x in s[1..] {

					}
				}
			}
			res
	}

	lemma seqMaxLemma(s: seq<int>, n: nat)
		requires |s| >= 1
		requires 1 < n <= |s|
		ensures seqMax(s[..n]) == seqMax(s) ==> seqMax(s) in s[..n]
		ensures seqMax(s[..n]) < seqMax(s) ==> seqMax(s) !in s[..n]
	{
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
	{
		match |s| {
			case 1 => s[0]
			case 2 => if s[0] >= s[1] then s[0] else s[1]
			case _ => if s[0] >= max(s[1..]) then s[0] else max(s[1..])
		}
	}

	method sumSeq(s: seq<nat>)  returns (total: nat)
	ensures total == sumSeqR(s)
	{
		total := 0;
		var i := 0;
		while i < |s| 
			invariant 0 <= i <= |s|
			invariant total == sumSeqR(s[..i])
		{
			sumSeqLemma(s[..i],[s[i]]);
			assert s[..(i+1)] == s[..i]+[s[i]];
			total := total + s[i];
			i := i + 1;
		}
		assert s[..i] == s;
		return total;
	}

	predicate sorted(a: seq<int>) {
  		forall j, k :: 0 <= j < k < |a| ==> a[j] <= a[k]
	}

	predicate isMax(x: int, s: seq<int>) {
		forall i | 0 <= i < |s| :: s[i] <= x
	}
}
