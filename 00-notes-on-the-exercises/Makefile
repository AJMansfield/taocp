CHAPTER = "NOTES ON THE EXERCISES"
EXERCISES = $(shell seq --format='%02.0f' 01 04)

EX_TARGETS = $(addprefix ex,$(EXERCISES))
ex_fmt_order = ex-head-$(1) ex$(1) ex-foot-$(1)
EX_ORDER = $(foreach ex,$(EXERCISES),$(call ex_fmt_order,$(ex)))

.PHONY: all title
all: title $(EX_ORDER)
	@echo "taocp: all exercises complete for $(CHAPTER)"
title:
	@echo "taocp: running exercises for $(CHAPTER)"
ex-head-%:
	@echo "taocp: running exercise $*"
ex-foot-%: ex-head-% ex% | ex-head-% ex%
	@echo "taocp: completed exercise $*"

ex%: %.md
	test -r $<
ex%: %.py
	python $<
ex04:
	@echo SKIP