all : recursive
	@find . -name '*.html' -print0 | xargs -0 $(MAKE) -s

recursive :
	@for makefile in `find . -mindepth 2 -name Makefile` ; do \
	    dir=`dirname $$makefile` ; \
	    echo "making $$dir/" ; \
	    ( cd $$dir ; make -s ) ; \
	done

presentation.html : presentation.txt docutils.conf
	@echo "making $@ from $<"
	@python2 ~/projects/docutils/docutils/tools/s52html.py $< $@

handout.html : presentation.txt docutils.conf
	@echo "making $@ from $<"
	@python2 ~/projects/docutils/docutils/tools/rst2html.py $< $@

%.html : %.txt docutils.conf
	@echo "making $@ from $<"
	@python2 ~/projects/docutils/docutils/tools/rst2html.py $< $@

checkin : 
	@svn ci -q --force-log -m. Makefile docutils.conf default.css
	@svn ci -q --force-log -m.

commit : checkin

install : all
	@cd .. ; ./push

updated :
	touch ../timestamp
