#!/usr/bin/perl

use strict;
use warnings;
use v5.10;
use Data::Dumper;

# input is like "678912345"

if (!@ARGV) {
	say "You did not pass a sequence of numbers to be analyzed";
	exit();
}

my @nums = split('', $ARGV[0]);

my $diffA;
my $diffB;

for (my $i = 0; $i < @nums - 2; $i++) {
	$diffA = $nums[$i] - $nums[$i + 1];
	$diffB = $nums[$i + 1] - $nums[$i + 2];
	
	if (!isSameSign($diffA, $diffB)) {
		say $nums[$i + 2];
		exit();
	}
}

sub isSameSign {
	my $first = shift;
	my $second = shift;
	my $product = $first * $second;
	if ($product > 0) {
		return 1;
	}
	else {
		return 0;
	}
}
