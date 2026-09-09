import pandas as pd
import pytest

source = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info.csv")
target = pd.read_csv(r"C:\Users\Haritha\PycharmProjects\etl_automation_july_2026\input_files\Contact_info_7.csv")

def test_count():
    src_cnt = len(source)
    tgt_cnt = len(target)
    assert src_cnt == tgt_cnt

def test_duplicate():
    duplicates = target.groupby('Identifier').size().reset_index(name='count').query('count>1')
    duplicate_cnt = len(duplicates)
    assert duplicate_cnt == 0

def test_null_check():
    null_cnt = target['Identifier'].isna().sum()
    assert null_cnt == 0


# Assert ==> Assert is validator, it does compare conditions mentioned in assert and return either TRue or False, If True test pass else Fail