# builtin - skip, skipif, xfail, parameterize,
# custom - any name

import pytest
import sys

# @pytest.mark.skip
# def test_count():
#     assert True
#
# @pytest.mark.skipif(condition=  1==1 ,reason="1==1")
# def test_duplicate():
#     assert True
#
# @pytest.mark.xfail
# def test_null():
#     assert True
#
#
# def test_data_compare():
#     assert True


# environment = 'UAT'
#
# @pytest.mark.skipif(environment !='PROD',reason=f'This test executes only in prod but user tried to run in other lower environment {environment}')
# def test_prod_test():
#     assert True
#
# @pytest.mark.skipif(sys.version_info >= (3, 10), reason="Requires Python 3.11 or higher")
# def test_4():
#     assert True

@pytest.mark.parametrize("user_name, password, expected",[('user2','pw2','postlogin'),('user1','pw1','postlogin'),('user2','incorrectpw','incorrect password..please retry')])
def test_login(user_name, password, expected):
    assert True


@pytest.mark.parametrize("source_query,target_query", [
    ("SELECT COUNT(*) FROM source_table",
     "SELECT COUNT(*) FROM target_table"),

    ("SELECT COUNT(*) FROM source_table2",
     "SELECT COUNT(*) FROM target_table2"),

    ("SELECT COUNT(*) FROM source_table3",
     "SELECT COUNT(*) FROM target_table3"),

    ("SELECT COUNT(*) FROM source_table4",
         "SELECT COUNT(*) FROM target_table4"),

    ("SELECT COUNT(*) FROM source_table5",
         "SELECT COUNT(*) FROM target_table5"),

    ("SELECT COUNT(*) FROM source_table6",
     "SELECT COUNT(*) FROM target_table6"),

    ("SELECT COUNT(*) FROM source_table7",
     "SELECT COUNT(*) FROM target_table7"),
])
def test_migration_aggregates(source_query, target_query):
    conn = snow.connect(
        user='fedexadmin',
        password='Dharmavaram1@1@',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH',
    )


    assert source_result == target_result




@pytest.mark.parametrize("target_query", [

    ( "SELECT pkey,count(1) count FROM target_table group by pkey having count(1)>1"),

    ("SELECT COUNT(*) FROM target_table2"),

    ("SELECT COUNT(*) FROM target_table3"),

    ( "SELECT COUNT(*) FROM target_table4"),

    ( "SELECT COUNT(*) FROM target_table5"),

    ( "SELECT COUNT(*) FROM target_table6"),

    ( "SELECT COUNT(*) FROM target_table7"),
])
def test_migration_duplicate(db_connection1,db_connection2,source_query, target_query):
    source_result = db_connection1.execute(source_query).fetchone()[0]
    target_result = db_connection2.execute(target_query).fetchone()[0]

    assert source_result == target_result