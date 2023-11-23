# to run: Rscript p1.R
library(readr)

# hm I could learn from this 
# https://rosettacode.org/wiki/FizzBuzz#R
lines <- read_lines("input")
curr_elf <- 0
elf_max <- 0
for(line in lines) {
	if(line == "") {
		if(curr_elf > elf_max) {
			elf_max <- curr_elf
		}
		curr_elf <- 0
	} else {
		curr_elf <- curr_elf + strtoi(line);
	}
}

print(elf_max)
