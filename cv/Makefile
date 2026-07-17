SHELL := /bin/sh

MAIN := xijia_tao_cv
OUTPUT := ../files/cv.pdf

.PHONY: all clean publish

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex publications.tex
	@if command -v latexmk >/dev/null 2>&1; then \
		latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex; \
	elif command -v tectonic >/dev/null 2>&1; then \
		tectonic --keep-logs $(MAIN).tex; \
	elif command -v pdflatex >/dev/null 2>&1; then \
		pdflatex -interaction=nonstopmode -halt-on-error $(MAIN).tex && \
		pdflatex -interaction=nonstopmode -halt-on-error $(MAIN).tex; \
	else \
		echo "No TeX compiler found. Install latexmk, tectonic, or pdflatex." >&2; \
		exit 1; \
	fi

publish: $(MAIN).pdf
	cp $(MAIN).pdf $(OUTPUT)

clean:
	@if command -v latexmk >/dev/null 2>&1; then \
		latexmk -C $(MAIN).tex; \
	else \
		rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).pdf; \
	fi
