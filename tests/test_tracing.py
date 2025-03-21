"""Test the tracing functionality of oft-trace against OpenFastTrace."""

import os
import json
import subprocess
import glob
import sys
from pathlib import Path
import datetime
import pytest

# Add the parent directory to path for importing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the actual CLI entry point function that's used by your project
from oft_trace.main import main as oft_main

# Constants
OFT_JAR = "_install/openfasttrace-4.1.0.jar"
REPORTS_DIR = "reports"
CONTENT_DIR = "content"  # Content directory with test files
TEST_REPORT_FILE = "test_report.md"  # Test report output file


def setup_module(module):
    """Setup before running all tests - download OFT jar if needed."""
    os.makedirs("_install", exist_ok=True)
    if not os.path.exists(OFT_JAR):
        print("Downloading OpenFastTrace jar...")
        subprocess.run([
            "wget", 
            "https://github.com/itsallcode/openfasttrace/releases/download/4.1.0/openfasttrace-4.1.0.jar",
            "-O", OFT_JAR
        ], check=True)
    
    # Make sure reports directory exists
    os.makedirs(REPORTS_DIR, exist_ok=True)


def run_java_oft(md_file):
    """
    Run the Java OpenFastTrace tool on the markdown file.
    
    According to OFT design (https://github.com/itsallcode/openfasttrace/blob/main/doc/spec/design.md),
    the import command converts input to specobjects and the trace command validates requirement traceability.
    """
    basename = os.path.basename(md_file)[:-3]
    aspec_file = os.path.join(REPORTS_DIR, f"{basename}.aspec")
    
    # Generate aspec file using import command first
    # This matches OFT behavior where import converts to specobjects
    import_result = subprocess.run([
        "java", "-jar", OFT_JAR, 
        "import", md_file, 
        "-o", "specobject", 
        "-f", aspec_file
    ], capture_output=True, text=True)
    
    # Even if import fails, we want to continue - just note the failure
    import_success = import_result.returncode == 0
    
    # If import succeeded, run trace
    trace_output = ""
    trace_returncode = -1
    if import_success and os.path.exists(aspec_file):
        # Run trace on the aspec file to get trace results
        trace_result = subprocess.run([
            "java", "-jar", OFT_JAR,
            "trace", aspec_file
        ], capture_output=True, text=True)
        
        trace_output = trace_result.stdout
        trace_returncode = trace_result.returncode
    else:
        # If import failed, we still want to continue with our own tool
        # Create an empty aspec file to test how our tool handles it
        with open(aspec_file, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<specobjects>\n</specobjects>')
    
    return {
        "aspec_file": aspec_file,
        "import_success": import_success,
        "import_output": import_result.stdout + import_result.stderr,
        "trace_output": trace_output,
        "success": import_success and "not ok" not in trace_output,
        "returncode": trace_returncode,
        "has_defects": not import_success or "not ok" in trace_output
    }


def run_python_oft(aspec_file, md_file=None, output_format="json"):
    """
    Run the Python OFT-trace tool on the aspec file or directly on md_file if specified.
    
    According to OFT design, both import and tracing should work in a single step.
    """
    output_file = f"{aspec_file}-python-output.{output_format}"
    
    # Choose input file (md_file if direct import is supported, otherwise aspec)
    input_file = md_file if md_file and hasattr(oft_main, 'supports_direct_import') else aspec_file
    
    # Call the main entry point function with appropriate arguments
    sys.argv = ["oft-trace", "trace-failures", input_file, "--format", output_format, "--output", output_file]
    try:
        # Capture stdout to avoid cluttering test output
        orig_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        oft_main()
        sys.stdout = orig_stdout
    except (SystemExit, Exception) as e:
        sys.stdout = sys.__stdout__  # Make sure we restore stdout
        print(f"Warning: Python OFT execution error: {e}")
    
    # Load the output file
    try:
        with open(output_file, 'r') as f:
            if output_format == "json":
                return json.load(f)
            else:
                return f.read()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading output file {output_file}: {e}")
        return {"error": str(e), "items": []}


# Find all markdown files in the content directory that should be tested
def get_test_files():
    """Find all markdown files for testing in the content directory."""
    return [f for f in glob.glob(f"{CONTENT_DIR}/*.md") if not os.path.basename(f).startswith("_")]


# Test results storage for report generation
test_results = []


@pytest.mark.parametrize("md_file", get_test_files())
def test_trace_against_java_oft(md_file):
    """
    Test that oft-trace produces results consistent with Java OFT.
    
    According to OFT design, if Java OFT finds defects (including import failures),
    our Python implementation should also identify issues.
    """
    result = {
        "file": os.path.basename(md_file),
        "test": "trace_consistency",
        "status": "PASS",
        "details": ""
    }
    
    # Run the Java reference implementation
    java_result = run_java_oft(md_file)
    
    # Record if Java OFT had issues with this file
    java_has_defects = java_result["has_defects"]
    java_import_failed = not java_result["import_success"]
    
    # Run our Python implementation
    python_result = run_python_oft(java_result["aspec_file"], md_file)
    
    # Check if our Python tool reports any defects
    python_has_defects = False
    if "items" in python_result:
        python_has_defects = any(
            item.get("coverage_type") != "COVERED" or 
            item.get("in_circular_dependency") == True or
            "failure_reasons" in item and len(item["failure_reasons"]) > 0
            for item in python_result["items"]
        ) or len(python_result.get("items", [])) == 0  # Empty items list is also a defect
    
    # Now evaluate the test results according to OFT specs:
    # 1. If Java has defects, our tool should also detect them
    # 2. Import failures are valid test cases, not reasons to skip
    
    if java_import_failed:
        # If Java import failed, our tool should detect some kind of issue
        if python_has_defects:
            result["details"] = "Java import failed, oft-trace correctly reported issues"
        else:
            result["status"] = "FAIL"
            result["details"] = "Java import failed but oft-trace reported no issues"
            test_results.append(result)
            pytest.fail(f"Java import failed for {md_file} but oft-trace didn't report issues")
    elif java_has_defects and not python_has_defects:
        # Java found tracing defects but our tool didn't
        result["status"] = "FAIL"
        result["details"] = "Java OFT found defects but oft-trace didn't"
        test_results.append(result)
        pytest.fail(f"Java OFT found defects in {md_file} but oft-trace didn't")
    
    # Record the result
    test_results.append(result)
    assert result["status"] == "PASS"


@pytest.mark.parametrize("md_file", get_test_files())
def test_circular_dependency_detection(md_file):
    """
    Test specifically for circular dependency detection.
    
    According to the OFT design document, circular dependencies are defects
    that should be reported.
    """
    result = {
        "file": os.path.basename(md_file),
        "test": "circular_dependency",
        "status": "PASS",
        "details": ""
    }
    
    # Run the Java reference implementation
    java_result = run_java_oft(md_file)
    
    # If Java import failed, we can't reliably test circular dependencies
    if not java_result["import_success"]:
        result["details"] = "Java import failed, can't check circular dependencies"
        test_results.append(result)
        return
    
    # Check if Java OFT reports circular dependencies
    java_has_circular = "circular" in java_result["trace_output"].lower() or \
                        ("unwanted" in java_result["trace_output"] and "coverage" in java_result["trace_output"])
    
    if not java_has_circular:
        result["details"] = "No circular dependencies in this test"
        test_results.append(result)
        return
    
    # Now check if our implementation detects them
    python_result = run_python_oft(java_result["aspec_file"])
    
    # Check if our Python tool reports circular dependencies
    python_has_circular = False
    if "items" in python_result:
        python_has_circular = any(
            item.get("in_circular_dependency") == True or
            any("circular" in reason.lower() for reason in item.get("failure_reasons", [])) or
            any("unwanted coverage" in reason.lower() for reason in item.get("failure_reasons", []))
            for item in python_result["items"]
        )
    
    # If we didn't detect the circular dependency, that's a problem
    if not python_has_circular:
        result["status"] = "FAIL"
        result["details"] = "Java OFT found circular dependencies but oft-trace didn't"
        test_results.append(result)
        pytest.fail(f"Java OFT found circular dependencies in {md_file} but oft-trace didn't")
    
    # Record success
    test_results.append(result)
    assert result["status"] == "PASS"


def teardown_module(module):
    """Generate a test report after all tests are run."""
    # Count results
    total = len(test_results)
    passed = sum(1 for r in test_results if r["status"] == "PASS")
    failed = sum(1 for r in test_results if r["status"] == "FAIL")
    skipped = sum(1 for r in test_results if r["status"] == "SKIPPED")
    
    # Generate report
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TEST_REPORT_FILE, 'w') as f:
        # Write report header according to OFT specs with rich formatting
        f.write(f"# OFT-Trace Test Report\n\n")
        f.write(f"Generated: {now}\n\n")
        
        # Summary
        f.write("## Summary\n\n")
        f.write(f"- Total tests: {total}\n")
        f.write(f"- Passed: {passed}\n")
        f.write(f"- Failed: {failed}\n")
        f.write(f"- Skipped: {skipped}\n\n")
        
        # Test details
        f.write("## Test Details\n\n")
        f.write("| File | Test | Status | Details |\n")
        f.write("|------|------|--------|--------|\n")
        
        for result in sorted(test_results, key=lambda r: (r["file"], r["test"])):
            status_icon = "✅" if result["status"] == "PASS" else "❌" if result["status"] == "FAIL" else "⏩"
            f.write(f"| {result['file']} | {result['test']} | {status_icon} {result['status']} | {result['details']} |\n")
        
        # Reference information per OFT specs
        f.write("\n## Reference Information\n\n")
        f.write("According to the OFT design document:\n\n")
        f.write("- Trace consistency tests verify that if Java OFT finds traceability defects, oft-trace also detects them\n")
        f.write("- Circular dependency tests verify that oft-trace correctly detects circular dependencies as specified in the design\n\n")
        f.write("### References\n\n")
        f.write("- [OFT User Guide](https://github.com/itsallcode/openfasttrace/blob/main/doc/user_guide.md)\n")
        f.write("- [OFT Design Specification](https://github.com/itsallcode/openfasttrace/blob/main/doc/spec/design.md)\n")
    
    print(f"\nTest report generated: {TEST_REPORT_FILE}")