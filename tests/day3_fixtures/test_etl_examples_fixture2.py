import pandas as pd
import pytest


def test_count2(read_fixture): # pytest testmethod/case always expects input as fixtures, we can't pass general variables global/locals
    print("Test count execution started.....")
    source, target = read_fixture
    src_cnt = len(source)
    tgt_cnt = len(target)
    assert src_cnt == tgt_cnt
#
def test_duplicate2(read_fixture):
    source, target = read_fixture
    duplicates = target.groupby('Identifier').size().reset_index(name='count').query('count>1')
    duplicate_cnt = len(duplicates)
    assert duplicate_cnt == 0
#
def test_null_check2(read_fixture):
    source, target = read_fixture
    null_cnt = target['Identifier'].isna().sum()
    assert null_cnt == 0
