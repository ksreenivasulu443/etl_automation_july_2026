import pandas as pd
import pytest

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

