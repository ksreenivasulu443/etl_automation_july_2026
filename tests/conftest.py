import pandas as pd
import pytest

#
# # 1. Runs once when pytest starts
# def pytest_configure(config):
#     print("\n" + "=" * 70)
#     print(config)
#     print("PYTEST ETL AUTOMATION STARTED")
#     print("=" * 70)
# #
# # # 2. Runs after pytest collects all test cases
# # def pytest_collection_modifyitems(config, items):
# #     print("\nTest cases collected:")
# #     for item in items:
# #         print(" -", item.name)
#
#
#
# # 3. Runs before every test case
# def pytest_runtest_setup(item):
#     print("\n" + "-" * 70)
#     print(f"Test execution started: {item.name}")
#     print("-" * 70)
#
# # 4. Runs after every test case
# def pytest_runtest_teardown(item, nextitem):
#     print(f"Test execution completed: {item.name, nextitem}")
#     print("-" * 70)
#
#
# # 6. Runs after all test cases are completed
# def pytest_sessionfinish(session, exitstatus):
#
#     print("\n" + "=" * 70)
#     print("PYTEST ETL AUTOMATION COMPLETED")
#     print(f"Exit Status: {exitstatus}")
#     print("=" * 70)

@pytest.fixture(scope='session')
def read_fixture():
    print("+"*70)
    print("read fixture execution started.....")
    source = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.csv")
    target = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.csv")

    print("read fixture execution completed.....")
    print("+" * 70)
    return source, target

@pytest.fixture(scope="module")
def input_value1():
    print("input value1 fixture")
    return 10

@pytest.fixture(scope="module")
def input_value2():
    print("input value2 fixture")
    return 20

@pytest.fixture(scope="module")
def read_inputs(input_value1, input_value2):
    print("read inputs fixture")
    return input_value1, input_value2

