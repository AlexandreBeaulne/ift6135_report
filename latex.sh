#!/bin/bash

NAME=$1
rm -f *.pdf
rm -f *.aux *.log *.out *.bbl *.blg *.bst
pdflatex $NAME
bibtex $NAME
pdflatex $NAME
pdflatex $NAME
rm -f *.aux *.log *.out *.bbl *.blg *.bst

