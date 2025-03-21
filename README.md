# OpenFastTrace Analysis Tool

A Python tool for analyzing and visualizing OpenFastTrace aspec reports, with a focus on identifying broken chains, dependencies, and version issues.

Learn more about OpenFastTrace at: [itsallcode/openfasttrace](https://github.com/itsallcode/openfasttrace)

## Features

- 🔍 **Trace Chain Analysis**: Visualize and analyze chains of dependent specification items
- 🚨 **Failure Detection**: Identify broken chains and the reasons for failures
- 🎨 **Rich Terminal Output**: Beautiful console visualizations with colors and Unicode symbols
- 🧠 **Intelligent Analysis**: Detects orphaned items, shallow coverage, and outdated versions

## Installation

```bash
pip install oft-trace
```

## Commands

## docs

Generate documentation for all commands.

This command auto-generates comprehensive documentation based on command help text and docstrings.

### Usage
```
oft-trace docs [OPTIONS]
```

### Parameters

#### Options
- `--output`, `-o`: Output file for documentation
- `--format`, `-f`: Output format: markdown or plain (Default: markdown)

---

## list-items

List all specification items in the aspec file with improved filtering.

### Usage
```
oft-trace list-items <aspec_file> [OPTIONS]
```

### Parameters

#### Arguments
- `aspec_file`: Path to the aspec XML file

#### Options
- `--doctype`, `-t`: Filter by document type
- `--status`, `-s`: Filter by status
- `--coverage`, `-c`: Filter by coverage status (COVERED, UNCOVERED, ORPHANED, SHALLOW, OUTDATED)
- `--output`, `-o`: Path to output file (if not specified, print to console)

---

## trace

Analyze and display the trace chain for a specification item in an aspec XML file.

If spec_id is not provided, shows an overview of the entire report.

### Usage
```
oft-trace trace <aspec_file> [spec_id] [OPTIONS]
```

### Parameters

#### Arguments
- `aspec_file`: Path to the aspec XML file
- `spec_id`: ID of the specification item to analyze (if omitted, shows overview)

#### Options
- `--version`, `-v`: Specific version of the item to trace
- `--doctype`, `-t`: Filter by document type
- `--direction`, `-d`: Direction of links to trace: both, incoming, or outgoing (Default: both)
- `--output`, `-o`: Path to output file (if not specified, print to console)
- `--details`: Show detailed trace information
- `--visual`: Show visual representation of trace chain

---

## trace-failures

Analyze and report on all broken chains in the aspec file with improved clarity.

This command identifies items with coverage issues and analyzes the reasons 
for the failures in detail. Can output in machine-readable format for CI/testing.

Examples:
    oft-trace trace-failures data.aspec
    oft-trace trace-failures data.aspec --format json --output report.json
    oft-trace trace-failures data.aspec --limit 5 --include-covered

### Usage
```
oft-trace trace-failures <aspec_file> [OPTIONS]
```

### Parameters

#### Arguments
- `aspec_file`: Path to the aspec XML file

#### Options
- `--output`, `-o`: Path to output file (if not specified, print to console)
- `--limit`, `-l`: Limit the number of failures to analyze
- `--include-covered`, `-a`: Include all items including covered ones
- `--format`, `-f`: Output format: text, json, or summary (Default: text)

---

## validate

Validate trace coverage for CI/CD pipelines and return appropriate exit code.

This command is optimized for use in automated tests and CI environments.
It performs a trace analysis and returns a non-zero exit code if any trace failures exist.

### Usage
```
oft-trace validate <aspec_file> [OPTIONS]
```

### Parameters

#### Arguments
- `aspec_file`: Path to the aspec XML file

#### Options
- `--exit-on-failure`: Exit with non-zero code if trace failures exist
- `--exclude`, `-e`: Comma-separated list of document types to exclude from validation
- `--output`, `-o`: Write validation results to file in JSON format



## Understanding the Reports
### Coverage Types

✅ `COVERED` - Item is fully covered
🔍 `ORPHANED` - Item is not covered by any other items
⚠️ `SHALLOW` - Item has shallow coverage but misses deep coverage
♻️ `OUTDATED` - Item has version mismatch issues
❌ `UNCOVERED` - Item is completely uncovered

#### Example Terminal Output

```bash
FAILURE 1/5: req~payment-processing~2 [req]
Title: System must process payments securely

Failure reasons:
- ♻️ Version mismatch: arch-payment-module covers v1 but v2 is expected
- ❌ Missing coverage for types: impl

Trace chain visualization:
└── ❌ req~payment-processing~2 (v2) [req] (/specs/requirements.md:45)
    └── ♻️ VERSION MISMATCH: Covering v1 but v2 expected
        └── ⚠️ arch-payment-module~1 (v1) [arch] (/specs/architecture.md:67)
```


## Advanced Usage

### Programmatic Usage
You can also use the library programmatically in your Python code:

```python
from oft_trace.analyzer import TraceAnalyzer
from oft_trace.parser import parse_aspec_file

# Parse the file
result = parse_aspec_file("path/to/report.aspec")
spec_items, id_map, covering_map, covered_by_map, broken_chains = result

# Create analyzer
analyzer = TraceAnalyzer(spec_items, id_map, covering_map, covered_by_map, broken_chains)

```


## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


**This tool was generated with the assistance of AI technology.**

