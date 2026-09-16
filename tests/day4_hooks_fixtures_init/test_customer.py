import pandas as pd
import pytest


@pytest.mark.regression
@pytest.mark.functional
def test_count1(read_fixture): # pytest testmethod/case always expects input as fixtures, we can't pass general variables global/locals
    source, target = read_fixture
    src_cnt = len(source)
    tgt_cnt = len(target)
    assert src_cnt == tgt_cnt

# @pytest.mark.sanity
# @pytest.mark.functional
# def test_duplicate1(read_fixture):
#     source, target = read_fixture
#     duplicates = target.groupby('Identifier').size().reset_index(name='count').query('count>1')
#     duplicate_cnt = len(duplicates)
#     assert duplicate_cnt == 0


# @pytest.mark.smoke
# @pytest.mark.functional
# def test_null_check1(read_fixture):
#     source, target = read_fixture
#     null_cnt = target['Identifier'].isna().sum()
#     assert null_cnt == 0
