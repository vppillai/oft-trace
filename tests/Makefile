SHELL := /bin/bash
OFT_VERSION = 4.1.0
INSTALL_DIR = _install

install:
	mkdir -p $(INSTALL_DIR)
	@if [ ! -f "$(INSTALL_DIR)/openfasttrace-${OFT_VERSION}.jar" ]; then \
		echo "Downloading openfasttrace-${OFT_VERSION}.jar..."; \
		wget https://github.com/itsallcode/openfasttrace/releases/download/4.1.0/openfasttrace-${OFT_VERSION}.jar -O $(INSTALL_DIR)/openfasttrace-${OFT_VERSION}.jar; \
	else \
		echo "Using existing openfasttrace-${OFT_VERSION}.jar"; \
	fi

distclean: clean
	rm -rf $(INSTALL_DIR)

clean:
	rm -rf reports
	rm -rf venv

.PHONY: aspec
aspec: install
	mkdir -p reports
	@for mdfile in $$(find . -name "*.md" -type f); do \
		basename=$$(basename $$mdfile .md); \
		echo "Processing $$mdfile -> reports/$$basename.aspec"; \
		java -jar $(INSTALL_DIR)/openfasttrace-${OFT_VERSION}.jar trace $$mdfile -o aspec -f reports/$$basename.aspec || echo "Error processing $$mdfile"; \
	done

.PHONY: test-trace
test-trace: venv install aspec
	@echo "Running trace validation tests..."
	@failed=0; \
	passed=0; \
	total=0; \
	results=""; \
	for aspecfile in $$(find reports -name "*.aspec" -type f); do \
		basename=$$(basename $$aspecfile .aspec); \
		echo "Testing $$basename"; \
		total=$$((total + 1)); \
		oft-trace trace-failures $$aspecfile --format json > reports/$$basename-trace.json; \
		exit_code=$$?; \
		expected_file="./$$basename-trace.json"; \
		test_result=""; \
		if [ ! -f "$$expected_file" ]; then \
			echo "❌ $$basename failed: expected file $$expected_file not found"; \
			echo "   Run 'make update-expected' to create expected output files"; \
			failed=$$((failed + 1)); \
			test_result="❌ MISSING_EXPECTED"; \
		else \
			echo "📊 Comparing with expected output..."; \
			if command -v jq > /dev/null; then \
				# Filter out timestamp and aspec_file path before comparing \
				diff -u <(jq 'del(.timestamp) | del(.aspec_file)' "$$expected_file" | jq --sort-keys .) \
					   <(jq 'del(.timestamp) | del(.aspec_file)' reports/$$basename-trace.json | jq --sort-keys .) > reports/$$basename-diff.txt; \
			else \
				echo "⚠️ Warning: jq not found, falling back to full diff (may include timestamp differences)"; \
				diff -u "$$expected_file" reports/$$basename-trace.json > reports/$$basename-diff.txt; \
			fi; \
			if [ $$? -eq 0 ]; then \
				echo "✅ $$basename passed"; \
				rm -f reports/$$basename-diff.txt; \
				passed=$$((passed + 1)); \
				test_result="✅ PASS"; \
			else \
				echo "❌ $$basename failed: output differs from expected"; \
				echo "   See diff in reports/$$basename-diff.txt"; \
				failed=$$((failed + 1)); \
				test_result="❌ DIFF"; \
			fi; \
		fi; \
		results="$$results\n$$basename | $$test_result"; \
	done; \
	echo -e "\n----------------------------------------"; \
	echo "          TEST RESULTS SUMMARY          "; \
	echo "----------------------------------------"; \
	echo "Test | Result"; \
	echo "----------------------------------------"; \
	echo -e "$$results" | sort; \
	echo "----------------------------------------"; \
	echo "TOTAL: $$total  PASSED: $$passed  FAILED: $$failed"; \
	echo "----------------------------------------"; \
	[ $$failed -eq 0 ]

.PHONY: update-expected
update-expected: aspec
	@echo "Updating expected output files..."
	@for aspecfile in $$(find reports -name "*.aspec" -type f); do \
		basename=$$(basename $$aspecfile .aspec); \
		echo "Generating $$basename-trace.json"; \
		oft-trace trace-failures $$aspecfile --format json > reports/$$basename-trace.json; \
		cp reports/$$basename-trace.json "./$$basename-trace.json"; \
		echo "✅ Updated $$basename-trace.json"; \
	done

venv:
	python3 -m venv venv
	venv/bin/pip install -e ../

.PHONY: docs
docs: venv
	@mkdir -p docs
	@echo "Generating command documentation..."
	venv/bin/oft-trace docs --output docs/commands.md
	@echo "✅ Documentation generated at docs/commands.md"