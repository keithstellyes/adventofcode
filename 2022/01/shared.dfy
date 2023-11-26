include "../../shared/dafny/parsing.dfy"
include "../../shared/dafny/shared.dfy"

module AOC202201Shared {
	import opened Parsing
	import opened AOCShared
	function allCalorieTotals(bags: seq<seq<nat>>) : (totals: seq<nat>) 
	ensures |bags| == |totals|
	ensures |bags| == 0 || forall bag | 0 <= bag < |bags| :: totals[bag] == sumSeqR(bags[bag])
	{
		if |bags| == 0 then []
		else [sumSeqR(bags[0])] + allCalorieTotals(bags[1..])
	}

	method parseFileData(data: string) returns (bags: seq<seq<nat>>) {
		var index := 0;
		var bag: seq<nat>;
		bag := [];
		bags := [];
		while index < |data| {
			var startingIndex := index;
			var cals, newIndex: int;
			expect(charIsInt(data[index]));
			cals, newIndex := strToUint(data[index..|data|]);
			index := newIndex + index;
			bag := bag + [cals];
			if index < |data| {
				expect(data[index] == '\n');
			}
			index := index + 1;
			if(index < |data| && data[index] == '\n') {
				bags := bags + [bag];
				bag := [];
				index := index + 1;
			}
			print(cals); print("\n");
		}
		return bags;
	}
}
