import pytest
import pandas as pd
import snowflake.connector as snow


# ============================================================
# 1. ROW COUNT VALIDATION
# ============================================================

@pytest.mark.parametrize("source_table_name,target_table_name", [
    (
        "test_db.test_schema.customer_source",
        "test_db.test_schema.customer_target"
    ),
    (
        "test_db.test_schema.order_source",
        "test_db.test_schema.order_target"
    )
])
def test_migration_aggregates(source_table_name, target_table_name):

    conn = snow.connect(
        user='fedexadmin',
        password='YOUR_PASSWORD',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH'
    )

    source = pd.read_sql(
        f"SELECT COUNT(1) AS ROW_COUNT FROM {source_table_name}",
        con=conn
    )

    target = pd.read_sql(
        f"SELECT COUNT(1) AS ROW_COUNT FROM {target_table_name}",
        con=conn
    )

    print("\nSOURCE:")
    print(source)

    print("\nTARGET:")
    print(target)

    assert source.iloc[0, 0] == target.iloc[0, 0]

    conn.close()


# ============================================================
# 2. SCHEMA VALIDATION
# ============================================================

@pytest.mark.parametrize("source_table_name,target_table_name", [
    (
        "test_db.test_schema.customer_source",
        "test_db.test_schema.customer_target"
    ),
    (
        "test_db.test_schema.order_source",
        "test_db.test_schema.order_target"
    )
])
def test_schema(source_table_name, target_table_name):
    conn = snow.connect(
        user='fedexadmin',
        password='Dharmavaram1@1@',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH',
    )

    source_table = source_table_name.split(".")[-1].upper()
    target_table = target_table_name.split(".")[-1].upper()

    source_query = f"""
        SELECT
            COLUMN_NAME,
            DATA_TYPE,
            ORDINAL_POSITION
        FROM test_db.information_schema.columns
        WHERE TABLE_SCHEMA = 'TEST_SCHEMA'
        AND TABLE_NAME = '{source_table}'
        ORDER BY ORDINAL_POSITION
    """

    target_query = f"""
        SELECT
            COLUMN_NAME,
            DATA_TYPE,
            ORDINAL_POSITION
        FROM test_db.information_schema.columns
        WHERE TABLE_SCHEMA = 'TEST_SCHEMA'
        AND TABLE_NAME = '{target_table}'
        ORDER BY ORDINAL_POSITION
    """

    source = pd.read_sql(source_query, con=conn)
    target = pd.read_sql(target_query, con=conn)

    print("\nSOURCE SCHEMA:")
    print(source)

    print("\nTARGET SCHEMA:")
    print(target)

    pd.testing.assert_frame_equal(
        source.reset_index(drop=True),
        target.reset_index(drop=True),
        check_dtype=False
    )

    conn.close()


# ============================================================
# 3. DUPLICATE VALIDATION
# ============================================================

@pytest.mark.parametrize("table_name,primary_key", [
    (
        "test_db.test_schema.customer_source",
        "customer_id"
    ),
    (
        "test_db.test_schema.customer_target",
        "customer_id"
    ),
    (
        "test_db.test_schema.order_source",
        "order_id"
    ),
    (
        "test_db.test_schema.order_target",
        "order_id"
    )
])
def test_duplicates(table_name, primary_key):

    conn = snow.connect(
        user='fedexadmin',
        password='YOUR_PASSWORD',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH'
    )

    query = f"""
        SELECT
            {primary_key},
            COUNT(*) AS DUPLICATE_COUNT
        FROM {table_name}
        GROUP BY {primary_key}
        HAVING COUNT(*) > 1
    """

    result = pd.read_sql(query, con=conn)

    print(f"\nDUPLICATES IN {table_name}")
    print(result)

    assert result.empty

    conn.close()


# ============================================================
# 4. NULL VALIDATION
# ============================================================

@pytest.mark.parametrize("table_name,column_name", [

    # Customer Source
    (
        "test_db.test_schema.customer_source",
        "customer_id"
    ),
    (
        "test_db.test_schema.customer_source",
        "first_name"
    ),
    (
        "test_db.test_schema.customer_source",
        "email"
    ),

    # Customer Target
    (
        "test_db.test_schema.customer_target",
        "customer_id"
    ),
    (
        "test_db.test_schema.customer_target",
        "first_name"
    ),
    (
        "test_db.test_schema.customer_target",
        "email"
    ),

    # Order Source
    (
        "test_db.test_schema.order_source",
        "order_id"
    ),
    (
        "test_db.test_schema.order_source",
        "customer_id"
    ),
    (
        "test_db.test_schema.order_source",
        "order_date"
    ),

    # Order Target
    (
        "test_db.test_schema.order_target",
        "order_id"
    ),
    (
        "test_db.test_schema.order_target",
        "customer_id"
    ),
    (
        "test_db.test_schema.order_target",
        "order_date"
    )
])
def test_nulls(table_name, column_name):

    conn = snow.connect(
        user='fedexadmin',
        password='YOUR_PASSWORD',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH'
    )

    query = f"""
        SELECT COUNT(*) AS NULL_COUNT
        FROM {table_name}
        WHERE {column_name} IS NULL
    """

    result = pd.read_sql(query, con=conn)

    null_count = result.iloc[0, 0]

    print(
        f"\nTable   : {table_name}"
        f"\nColumn  : {column_name}"
        f"\nNULLs   : {null_count}"
    )

    assert null_count == 0

    conn.close()


# ============================================================
# 5. FULL DATA COMPARISON
# ============================================================

@pytest.mark.parametrize("source_table_name,target_table_name", [
    (
        "test_db.test_schema.customer_source",
        "test_db.test_schema.customer_target"
    ),
    (
        "test_db.test_schema.order_source",
        "test_db.test_schema.order_target"
    )
])
def test_data_compare(source_table_name, target_table_name):

    conn = snow.connect(
        user='fedexadmin',
        password='YOUR_PASSWORD',
        account='kefeety-io28450',
        warehouse='COMPUTE_WH'
    )

    source_query = f"""
        SELECT *
        FROM {source_table_name}
        ORDER BY 1
    """

    target_query = f"""
        SELECT *
        FROM {target_table_name}
        ORDER BY 1
    """

    source = pd.read_sql(source_query, con=conn)
    target = pd.read_sql(target_query, con=conn)

    print("\nSOURCE DATA:")
    print(source)

    print("\nTARGET DATA:")
    print(target)

    # Row count
    assert len(source) == len(target), \
        f"Row count mismatch: {len(source)} != {len(target)}"

    # Column count
    assert len(source.columns) == len(target.columns), \
        f"Column count mismatch"

    # Column names
    assert list(source.columns) == list(target.columns), \
        f"Column names mismatch"

    # Complete data comparison
    pd.testing.assert_frame_equal(
        source.reset_index(drop=True),
        target.reset_index(drop=True),
        check_dtype=False
    )

    conn.close()