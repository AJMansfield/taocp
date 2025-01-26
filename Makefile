# copied from https://stackoverflow.com/a/9946567/1324631

SUBDIRS = $(shell ls -d */)

all:
	@for dir in "$(SUBDIRS)" ; do \
		if [ -r "$$dir"/Makefile ]; then \
			echo "Evaluating \"$$dir\""; \
			make -C "$$dir" ; \
		fi; \
	done;