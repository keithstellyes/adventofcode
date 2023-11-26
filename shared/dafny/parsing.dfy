module Parsing {
	predicate charIsInt(c: char) {
		c >= '0' && c <= '9'
	}
	method strToUint(s: string) returns (parsedInteger: int, indexAfter: int)
	ensures indexAfter <= |s| + 1 
	ensures (s == "123" && parsedInteger == 123 && indexAfter == 4) || s != "123"
	ensures parsedInteger >= 0 
	ensures indexAfter >= 0
	{
		var i, mul : int;
		parsedInteger := 0;
		indexAfter := 0;
		mul := 1;
		while indexAfter < |s| && charIsInt(s[indexAfter]) {
			indexAfter := indexAfter + 1;
		}
		i := indexAfter - 1;
		while i >= 0 {
			var digit := (s[i] as int - '0' as int);
			parsedInteger := parsedInteger + digit * mul;
			mul := mul * 10;
			i := i - 1;
		}
		return parsedInteger, indexAfter;
	}
}
