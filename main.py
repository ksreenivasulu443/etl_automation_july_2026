

import pytest
import pandas as pd


# 1. Runs once when pytest starts
def pytest_configure(config):
    print("\n" + "=" * 70)
    print("PYTEST ETL AUTOMATION STARTED")
    print("=" * 70)


# 2. Runs after pytest collects all test cases
def pytest_collection_modifyitems(config, items):
    print("\nTest cases collected:")
    for item in items:
        print(" -", item.name)


# 3. Runs before every test case
def pytest_runtest_setup(item):
    print("\n" + "-" * 70)
    print(f"Test execution started: {item.name}")
    print("-" * 70)


# 4. Runs after every test case
def pytest_runtest_teardown(item, nextitem):
    print(f"Test execution completed: {item.name}")
    print("-" * 70)


# 5. Captures test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        if report.passed:
            print(f"RESULT: {item.name} - PASSED")

        elif report.failed:
            print(f"RESULT: {item.name} - FAILED")

        elif report.skipped:
            print(f"RESULT: {item.name} - SKIPPED")


# 6. Runs after all test cases are completed
def pytest_sessionfinish(session, exitstatus):

    print("\n" + "=" * 70)
    print("PYTEST ETL AUTOMATION COMPLETED")
    print(f"Exit Status: {exitstatus}")
    print("=" * 70)


# Fixture
@pytest.fixture(scope="session")
def read_fixture():


    source = pd.read_csv(
        r"C:\Users\Haritha\PycharmProjects"
        r"\etl_automation_july_2026"
        r"\input_files\Contact_info.csv"
    )

    target = pd.read_csv(
        r"C:\Users\Haritha\PycharmProjects"
        r"\etl_automation_july_2026"
        r"\input_files\Contact_info.csv"
    )


    return source, target