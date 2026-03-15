all:
	docker/dockerbuild.sh

image:
	docker build -t hnzhu/images:paper-build docker

.PHONY: all image

clean:
	rm -f *.aux *.bbl *.blg *.log *.dvi *.out *.idx *.bak *~ *.toc *.lof *.nav *.snm
	rm -f *.bcf *.run.xml *.synctex.gz
	rm -f *.fdb_latexmk *.fls
	rm -f main.pdf
