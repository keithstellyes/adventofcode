include "shared.dfy"
include "../../shared/dafny/shared.dfy"

module AOC202201 {
	import opened AOC202201Shared
	import opened AOCShared

	method Main() {
		var data := parseFileData("1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000");
		expect |data| > 0;
		var result := algo(data);
		print(result);
	}

	method algo(bags: seq<seq<nat>>)  returns (result: nat)
	requires |bags| > 0
	ensures result in allCalorieTotals(bags)
	ensures result == seqMax(allCalorieTotals(bags))
	{
		var mostCals : nat;
		mostCals := 0;
		var totals := allCalorieTotals(bags);
		assert(forall i | 0 <= i < |bags| :: sumSeqR(bags[i]) in totals);
		assert(forall i | 0 <= i < |totals| :: max(totals) >= totals[i]);
		assert(mostCals <= max(totals));
		assert(seqMax(totals) in totals);
		var i := 0;
		while i < |bags| 
		invariant mostCals <= max(totals)
		invariant mostCals >= 0
		invariant mostCals == 0 || mostCals in totals
		invariant (mostCals != 0) ==> mostCals in totals
		invariant forall n | 0 <= n < i && n < |bags| :: totals[n] <= mostCals
		{
			var bag := bags[i];
			var currCals := sumSeq(bag);
			var oldMostCals := mostCals;
			if currCals > mostCals {
				mostCals := currCals;
			}
			assert mostCals >= currCals;
			assert currCals == 0 || mostCals != 0;
			assert currCals != 0 ==> mostCals != 0;
			assert mostCals in allCalorieTotals(bags);
			i := i + 1;
		}
		
		return mostCals;
	}
}
