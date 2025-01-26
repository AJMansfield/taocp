SUBDIRS = $(shell ls -d */)

all:
	@for dir in $(SUBDIRS) ; do \
		if [ -r "$$dir"/Makefile ]; then \
			echo "Evaluating \"$$dir\""; \
			$(MAKE) -C "$$dir" ; \
		fi; \
	done;
