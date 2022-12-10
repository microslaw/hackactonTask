## Table of contents
* [General info](#General-info)
* [Used languages and tools](#Used-languages-and-tools)
* [Setup](#Setup)
* [Functions](#Functions)
* [Authors](#Authors)


## General info
Polish curse word classification using simple heuristic.
	
## Used languages and tools:
* Python 3.10.7
	
## Setup
To censor words import censoring.py, and add badWords.txt to the same directory.
For in-file use examples see example1.py and example2.py

## Functions
* censorWord - if word variable is classified as a curse replaces all but first and last characters with '*', unless other replaceChar variable is specified
* isBadWord - returns true if word variable is classified as curse, or false otherwise

## Authors
BEST Gdansk hackaton team "Natural stupidity"
* microslaw
* mszablewski
* sgolebiewska
* szpkwsk