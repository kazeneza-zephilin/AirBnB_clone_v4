#!/bin/bash

# AirBnB Clone v4 - Test Runner
# This script runs all unit tests in the hbtn_tests directory

echo "🧪 Running AirBnB Clone v4 Unit Tests..."
echo "========================================"

# Change to the project root directory
cd "$(dirname "$0")/../.."

# Set environment for file storage testing
export HBNB_TYPE_STORAGE=file

# Run all Python unit tests
echo "Running Python unit tests..."
python3 -m unittest discover -s dev/hbtn_tests -p "test_*.py" -v

echo ""
echo "========================================"
echo "✅ Test run completed!"
