all: presentation.html handout.html

presentation.html : presentation.txt docutils.conf
	@echo "checking in $< and making $@"
	#@svn ci -q --force-log  -m. $<
	@rst2s5.py --strip-comments $< $@

handout.html : presentation.txt docutils.conf
	@echo "checking in $< and making $@"
	#@svn ci -q --force-log  -m. $<
	@rst2html.py --strip-comments $< $@
