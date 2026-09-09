import pytest
import pandas as pd
import snowflake.connector as snow


@pytest.mark.parametrize("source_table_name,target_table_name", [
    ("test_db.test_schema.customer_source",
     "test_db.test_schema.customer_target"),

    ("test_db.test_schema.order_source",
     "test_db.test_schema.order_target")
])
def test_migration_aggregates(source_table_name, target_table_name):
    conn = snow.connect(
        user='fedexadmin',
        password='Dharmavaram1@1@',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH',
    )

    source = pd.read_sql(sql=f"select count(1) from {source_table_name}", con=conn)

    print(source)
    target  = pd.read_sql(sql=f"select count(1) from {target_table_name}", con=conn)
    print(target)

    assert source.iloc[0,0] == target.iloc[0]