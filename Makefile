.PHONY: help
help:
	@echo "Test target script"
	@echo "  make run-script SCRIPT=<script_name> "

# Belirtilen Python scriptini çalıştır
.PHONY: run-script
run-script:
	python3 $(SCRIPT)