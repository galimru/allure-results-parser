#!/usr/bin/env python3

import os
import json
import glob

def format_duration(duration_ms):
    """Convert duration from milliseconds to a human-readable format (HhMmSs)."""
    seconds = duration_ms // 1000
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    # Construct the duration string
    duration_parts = []
    if hours > 0:
        duration_parts.append(f"{int(hours)}h")
    if minutes > 0 or hours > 0:  # Show minutes if there's at least an hour
        duration_parts.append(f"{int(minutes)}m")
    duration_parts.append(f"{int(seconds)}s")

    return ''.join(duration_parts)

def parse_allure_results(directory):
    results = {
        "passed": 0,
        "failed": 0,
        "broken": 0,
        "skipped": 0,
        "total": 0,
        "duration": 0.0
    }

    print(f"Parsing results from directory: {directory}")

    for json_file in glob.glob(os.path.join(directory, "*.json")):
        print(f"Processing file: {json_file}")
        with open(json_file, 'r') as f:
            data = json.load(f)
            if "status" in data:
                # Increment total test count
                results["total"] += 1

                # Calculate test duration (stop - start)
                start_time = data.get("start", 0)
                stop_time = data.get("stop", 0)
                results["duration"] += (stop_time - start_time)

                # Status handling
                status = data["status"]
                if status == "passed":
                    results["passed"] += 1
                elif status == "failed":
                    results["failed"] += 1
                elif status == "broken":
                    results["broken"] += 1
                elif status == "skipped":
                    results["skipped"] += 1

    # Add duration
    results["duration"] = format_duration(results["duration"])

    return results

def main():
    # Allure results directory passed as an input from GitHub Actions
    allure_dir = os.getenv('INPUT_ALLURE_DIRECTORY', './allure-results')

    # Check if directory exists
    if not os.path.exists(allure_dir):
        print(f"Directory {allure_dir} does not exist.")
        exit(1)

    # Parse the results
    results = parse_allure_results(allure_dir)

    # Set the results as outputs to be consumed by other steps
    print(f"::set-output name=passed::{results['passed']}")
    print(f"::set-output name=failed::{results['failed']}")
    print(f"::set-output name=broken::{results['broken']}")
    print(f"::set-output name=skipped::{results['skipped']}")
    print(f"::set-output name=total::{results['total']}")
    print(f"::set-output name=duration::{results['duration']}")

if __name__ == "__main__":
    main()
