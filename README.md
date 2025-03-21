# Allure Results Parser

Welcome to the **Allure Results Parser**! This GitHub Action makes it super easy to parse your Allure test results in JSON format and get key metrics about your tests. Whether you're tracking passed, failed, or skipped tests, we've got you covered!

## How it works

This action simplifies the process of extracting important metrics from your Allure JSON files. You can effortlessly gather essential information such as the number of tests that passed, failed, broken, or were skipped, along with the total count of tests and the overall duration of the test run. With this action, you can gain valuable insights into your testing process, allowing you to make data-driven decisions to improve your test suite.


## Inputs

Here's what you need to provide:

| Name               | Description                                       | Required | Default           |
|--------------------|---------------------------------------------------|----------|-------------------|
| `allure_directory` | The path to the folder containing your Allure JSON files | Yes      | `./allure-results` |

## Outputs

After running the action, you'll get these handy outputs:

| Name      | Description                          |
|-----------|--------------------------------------|
| `passed`  | Count of tests that passed          |
| `failed`  | Count of tests that failed          |
| `broken`  | Count of tests that were broken     |
| `skipped` | Count of tests that were skipped    |
| `total`   | Total count of tests                |
| `duration`  | The total duration of all tests in a human-readable format (HhMmSs). |

## Usage

### Example Workflow

Here’s how to use the action in your GitHub workflow:

```yaml
name: Parse Allure Results

on: [push]

jobs:
  parse-results:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Parse Allure Results
        id: parse_allure
        uses: galimru/allure-results-parser@v1.0.0
        with:
          allure_directory: ./allure-results

      - name: Display Results
        run: |
          echo "Passed: ${{ steps.parse_allure.outputs.passed }}"
          echo "Failed: ${{ steps.parse_allure.outputs.failed }}"
          echo "Broken: ${{ steps.parse_allure.outputs.broken }}"
          echo "Skipped: ${{ steps.parse_allure.outputs.skipped }}"
          echo "Total: ${{ steps.parse_allure.outputs.total }}"
          echo "Duration: ${{ steps.parse_allure.outputs.duration }}"          
```