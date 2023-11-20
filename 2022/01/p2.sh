#!/bin/env bash

./pre.sh | tail -3  | sed -z '$s/\n$//' | sed -z 's/\n/+/g' | sed -z 's/$/\nquit/' | bc
