#!/usr/bin/env bash
for filename in test/*.py; do
	echo $filename
	python3 $filename || exit 1;
done
echo "All tests successful"
