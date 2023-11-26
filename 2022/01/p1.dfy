include "shared.dfy"
include "../../shared/dafny/shared.dfy"

module AOC202201 {
	import opened AOC202201Shared
	import opened AOCShared

	lemma linearSearch(haystack: seq<int>, needle: int, index: int) 
		requires |haystack| >= 1
		requires index < |haystack|
		requires 0 <= index
		ensures index < 2 || |haystack| < 2 || forall n | 0 <= n < index :: needle in haystack[n..(index + 1)]
	{
		
	}

	method Main() {
		var data := parseFileData("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000");
		assume(|data| > 0);
		var result := algo(data);
		print(result);
	}

	method algo(bags: seq<seq<int>>)  returns (result: int)
	requires |bags| > 0
	ensures result == max(allCalorieTotals(bags))
	{
		var mostCals := -1;
		var totals := allCalorieTotals(bags);
		assume(seqHasNoNegatives(totals));
		expect |totals| > 1;
		assert(forall i | 0 <= i < |bags| :: sumSeqR(bags[i]) in totals);
		assert(forall i | 0 <= i < |totals| :: max(totals) >= totals[i]);
		assert(mostCals <= max(totals));
		assert(max(totals) in totals);
		var i := 0;
		while i < |bags| 
		invariant mostCals <= max(totals)
		{
			var bag := bags[i];
			assume(seqHasNoNegatives(bag));
			subsetSmaller(bag);
			var currCals := sumSeqR(bag);
			if currCals > mostCals {
				mostCals := currCals;
			}
			if currCals == max(totals) {
				linearSearch(totals, max(totals), i);
			}
			assert(mostCals in totals);
			// linearSearchingForMax(bag, mostCals, i);
			// If we haven't found the max yet, then it's in the spaces we haven't checked
			assert(mostCals == max(totals) || max(totals) in totals[i..]);
			// If we've found the max, then it's our current spot or before
			assert(mostCals != max(totals) || max(totals) in totals[0..i]);
			i := i + 1;
			assert(i != |bags| || mostCals == max(totals));
		}
		return mostCals;
	}
}
