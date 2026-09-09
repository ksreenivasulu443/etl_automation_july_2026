import streamlit as st
import pandas as pd
import random
import io
import zipfile

from faker import Faker
from datetime import timedelta


# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce ETL Test Data Generator",
    page_icon="🛒",
    layout="wide"
)

fake = Faker()


# ============================================================
# PAGE TITLE
# ============================================================

# ============================================================
# ETL AUTOMATION LABS BANNER
# ============================================================

st.markdown(
    """
    <div style="
        background: linear-gradient(90deg, #0f172a, #1e3a8a);
        padding: 22px 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    ">
        <h1 style="
            color: white;
            margin: 0;
            font-size: 34px;
            font-weight: 700;
            letter-spacing: 2px;
        ">
            ETL AUTOMATION LABS
        </h1>

        <p style="
            color: #dbeafe;
            margin: 8px 0 0 0;
            font-size: 16px;
        ">
            ETL • Data Quality • Big Data • Automation Testing
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title(
    "🛒 E-Commerce ETL Test Data Generator"
)

st.markdown(
    """
Generate realistic **positive and negative test data** for
ETL, Data Quality, Data Warehouse and Data Engineering testing.
"""
)


# ============================================================
# COLUMN DEFINITIONS
# ============================================================

CUSTOMER_COLUMNS = {
    "customer_id": "Customer ID",
    "name": "Customer Name",
    "phone": "Phone",
    "gender": "Gender",
    "email": "Email",
    "date_of_birth": "Date of Birth",
    "city": "City",
    "state": "State",
    "country": "Country",
    "postal_code": "Postal Code",
    "registration_date": "Registration Date",
    "customer_status": "Customer Status"
}

PRODUCT_COLUMNS = {
    "product_id": "Product ID",
    "product_name": "Product Name",
    "category": "Category",
    "subcategory": "Sub Category",
    "brand": "Brand",
    "price": "Price",
    "cost": "Cost",
    "stock_quantity": "Stock Quantity",
    "product_status": "Product Status",
    "created_date": "Created Date"
}

ORDER_COLUMNS = {
    "order_id": "Order ID",
    "customer_id": "Customer ID",
    "product_id": "Product ID",
    "order_date": "Order Date",
    "quantity": "Quantity",
    "unit_price": "Unit Price",
    "discount": "Discount",
    "tax": "Tax",
    "total_amount": "Total Amount",
    "payment_method": "Payment Method",
    "order_status": "Order Status"
}

TRANSACTION_COLUMNS = {
    "transaction_id": "Transaction ID",
    "order_id": "Order ID",
    "customer_id": "Customer ID",
    "transaction_date": "Transaction Date",
    "transaction_type": "Transaction Type",
    "transaction_amount": "Transaction Amount",
    "payment_method": "Payment Method",
    "transaction_status": "Transaction Status",
    "currency": "Currency"
}

SHIPMENT_COLUMNS = {
    "shipment_id": "Shipment ID",
    "order_id": "Order ID",
    "customer_id": "Customer ID",
    "shipment_date": "Shipment Date",
    "delivery_date": "Delivery Date",
    "carrier": "Carrier",
    "tracking_number": "Tracking Number",
    "shipping_city": "Shipping City",
    "shipping_state": "Shipping State",
    "shipment_status": "Shipment Status"
}


DATASETS = [
    "Customer",
    "Product",
    "Orders",
    "Transactions",
    "Shipment"
]

SCENARIOS = [
    "Positive",
    "Null Values",
    "Duplicate Records",
    "Invalid Email",
    "Invalid Phone",
    "Invalid Date",
    "Negative Amount",
    "Invalid Foreign Key"
]


# ============================================================
# SESSION STATE
# ============================================================

if "generated_files" not in st.session_state:
    st.session_state.generated_files = {}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_column_definition(dataset):

    if dataset == "Customer":
        return CUSTOMER_COLUMNS

    if dataset == "Product":
        return PRODUCT_COLUMNS

    if dataset == "Orders":
        return ORDER_COLUMNS

    if dataset == "Transactions":
        return TRANSACTION_COLUMNS

    if dataset == "Shipment":
        return SHIPMENT_COLUMNS

    return {}


def generate_scenario_counts(
    rows,
    selected_scenarios,
    percentages
):

    configured = {
        scenario: percentages.get(
            scenario,
            0
        )
        for scenario in selected_scenarios
    }

    total_percentage = sum(
        configured.values()
    )

    if total_percentage > 100:

        return None

    # Automatically assign remaining
    # percentage to Positive
    remaining = 100 - total_percentage

    if "Positive" in configured:

        configured["Positive"] += remaining

    elif remaining > 0:

        configured["Positive"] = remaining

    counts = {}

    remaining_rows = rows

    scenario_list = list(
        configured.keys()
    )

    for index, scenario in enumerate(
        scenario_list
    ):

        if index == len(scenario_list) - 1:

            count = remaining_rows

        else:

            count = int(
                rows
                * configured[scenario]
                / 100
            )

            remaining_rows -= count

        counts[scenario] = count

    return counts


# ============================================================
# APPLY NULL SCENARIO
# ============================================================

def apply_null_values(
    df,
    count
):

    if count <= 0 or len(df) == 0:
        return

    protected_columns = [
        "customer_id",
        "product_id",
        "order_id",
        "transaction_id",
        "shipment_id"
    ]

    usable_columns = [
        col
        for col in df.columns
        if col not in protected_columns
    ]

    if not usable_columns:
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    for index in indexes:

        column = random.choice(
            usable_columns
        )

        df.loc[
            index,
            column
        ] = None


# ============================================================
# INVALID EMAIL
# ============================================================

def apply_invalid_email(
    df,
    count
):

    if (
        count <= 0
        or "email" not in df.columns
    ):
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    invalid_emails = [
        "invalid_email",
        "abc@",
        "@gmail.com",
        "test",
        "user@",
        "abc.gmail.com"
    ]

    for index in indexes:

        df.loc[
            index,
            "email"
        ] = random.choice(
            invalid_emails
        )


# ============================================================
# INVALID PHONE
# ============================================================

def apply_invalid_phone(
    df,
    count
):

    if (
        count <= 0
        or "phone" not in df.columns
    ):
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    invalid_phones = [
        "123",
        "12345",
        "abcdefghij",
        "123456789012345",
        "",
        "999999"
    ]

    for index in indexes:

        df.loc[
            index,
            "phone"
        ] = random.choice(
            invalid_phones
        )


# ============================================================
# INVALID DATE
# ============================================================

def apply_invalid_date(
    df,
    count
):

    if count <= 0:
        return

    date_columns = [
        col
        for col in df.columns
        if "date" in col
    ]

    if not date_columns:
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    invalid_dates = [
        "INVALID_DATE",
        "2026-99-99",
        "31/31/2026",
        "ABC",
        "0000-00-00"
    ]

    for index in indexes:

        column = random.choice(
            date_columns
        )

        df.loc[
            index,
            column
        ] = random.choice(
            invalid_dates
        )


# ============================================================
# NEGATIVE AMOUNT
# ============================================================

def apply_negative_amount(
    df,
    count
):

    if count <= 0:
        return

    amount_columns = [
        col
        for col in df.columns
        if (
            "amount" in col.lower()
            or col in [
                "price",
                "cost",
                "discount",
                "tax",
                "unit_price"
            ]
        )
    ]

    if not amount_columns:
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    for index in indexes:

        column = random.choice(
            amount_columns
        )

        try:

            value = float(
                df.loc[
                    index,
                    column
                ]
            )

            df.loc[
                index,
                column
            ] = -abs(value)

        except:

            df.loc[
                index,
                column
            ] = -100


# ============================================================
# INVALID FOREIGN KEY
# ============================================================

def apply_invalid_foreign_key(
    df,
    count
):

    if count <= 0:
        return

    foreign_key_columns = [
        col
        for col in [
            "customer_id",
            "product_id",
            "order_id"
        ]
        if col in df.columns
    ]

    if not foreign_key_columns:
        return

    indexes = random.sample(
        list(df.index),
        min(count, len(df))
    )

    for index in indexes:

        column = random.choice(
            foreign_key_columns
        )

        df.loc[
            index,
            column
        ] = (
            "INVALID_"
            + str(
                random.randint(
                    10000,
                    99999
                )
            )
        )


# ============================================================
# DUPLICATES
# ============================================================

def apply_duplicates(
    df,
    count
):

    if count <= 0 or len(df) == 0:
        return df

    duplicate_count = min(
        count,
        len(df)
    )

    duplicate_rows = df.sample(
        duplicate_count
    )

    return pd.concat(
        [
            df,
            duplicate_rows
        ],
        ignore_index=True
    )


# ============================================================
# CUSTOMER GENERATOR
# ============================================================

def generate_customer(
    rows,
    columns,
    scenario_counts
):

    records = []

    for i in range(rows):

        records.append(
            {
                "customer_id":
                    f"CUST{100000 + i}",

                "name":
                    fake.name(),

                "phone":
                    fake.numerify(
                        "##########"
                    ),

                "gender":
                    random.choice(
                        [
                            "Male",
                            "Female",
                            "Other"
                        ]
                    ),

                "email":
                    fake.email(),

                "date_of_birth":
                    fake.date_of_birth(
                        minimum_age=18,
                        maximum_age=70
                    ).strftime(
                        "%Y-%m-%d"
                    ),

                "city":
                    fake.city(),

                "state":
                    fake.state(),

                "country":
                    "India",

                "postal_code":
                    fake.postcode(),

                "registration_date":
                    fake.date_between(
                        start_date="-5y",
                        end_date="today"
                    ).strftime(
                        "%Y-%m-%d"
                    ),

                "customer_status":
                    random.choice(
                        [
                            "ACTIVE",
                            "INACTIVE",
                            "SUSPENDED"
                        ]
                    )
            }
        )

    df = pd.DataFrame(records)

    apply_null_values(
        df,
        scenario_counts.get(
            "Null Values",
            0
        )
    )

    apply_invalid_email(
        df,
        scenario_counts.get(
            "Invalid Email",
            0
        )
    )

    apply_invalid_phone(
        df,
        scenario_counts.get(
            "Invalid Phone",
            0
        )
    )

    apply_invalid_date(
        df,
        scenario_counts.get(
            "Invalid Date",
            0
        )
    )

    apply_invalid_foreign_key(
        df,
        scenario_counts.get(
            "Invalid Foreign Key",
            0
        )
    )

    df = apply_duplicates(
        df,
        scenario_counts.get(
            "Duplicate Records",
            0
        )
    )

    return df[columns]


# ============================================================
# PRODUCT GENERATOR
# ============================================================

def generate_product(
    rows,
    columns,
    scenario_counts
):

    records = []

    for i in range(rows):

        price = round(
            random.uniform(
                100,
                50000
            ),
            2
        )

        cost = round(
            price
            * random.uniform(
                0.4,
                0.8
            ),
            2
        )

        records.append(
            {
                "product_id":
                    f"PROD{100000 + i}",

                "product_name":
                    fake.catch_phrase(),

                "category":
                    random.choice(
                        [
                            "Electronics",
                            "Clothing",
                            "Home",
                            "Beauty",
                            "Sports",
                            "Books"
                        ]
                    ),

                "subcategory":
                    random.choice(
                        [
                            "Mobile",
                            "Laptop",
                            "Shoes",
                            "Furniture",
                            "Accessories",
                            "Fitness"
                        ]
                    ),

                "brand":
                    random.choice(
                        [
                            "Samsung",
                            "Apple",
                            "Nike",
                            "Sony",
                            "Adidas",
                            "Dell"
                        ]
                    ),

                "price":
                    price,

                "cost":
                    cost,

                "stock_quantity":
                    random.randint(
                        0,
                        500
                    ),

                "product_status":
                    random.choice(
                        [
                            "ACTIVE",
                            "INACTIVE",
                            "DISCONTINUED"
                        ]
                    ),

                "created_date":
                    fake.date_between(
                        start_date="-3y",
                        end_date="today"
                    ).strftime(
                        "%Y-%m-%d"
                    )
            }
        )

    df = pd.DataFrame(records)

    apply_null_values(
        df,
        scenario_counts.get(
            "Null Values",
            0
        )
    )

    apply_invalid_date(
        df,
        scenario_counts.get(
            "Invalid Date",
            0
        )
    )

    apply_negative_amount(
        df,
        scenario_counts.get(
            "Negative Amount",
            0
        )
    )

    apply_invalid_foreign_key(
        df,
        scenario_counts.get(
            "Invalid Foreign Key",
            0
        )
    )

    df = apply_duplicates(
        df,
        scenario_counts.get(
            "Duplicate Records",
            0
        )
    )

    return df[columns]


# ============================================================
# ORDERS GENERATOR
# ============================================================

def generate_orders(
    rows,
    columns,
    scenario_counts,
    customer_ids,
    product_ids
):

    records = []

    for i in range(rows):

        quantity = random.randint(
            1,
            10
        )

        unit_price = round(
            random.uniform(
                100,
                30000
            ),
            2
        )

        discount = round(
            random.uniform(
                0,
                unit_price * 0.2
            ),
            2
        )

        tax = round(
            (
                quantity * unit_price
                - discount
            ) * 0.18,
            2
        )

        total_amount = round(
            quantity * unit_price
            - discount
            + tax,
            2
        )

        records.append(
            {
                "order_id":
                    f"ORD{100000 + i}",

                "customer_id":
                    random.choice(
                        customer_ids
                    ),

                "product_id":
                    random.choice(
                        product_ids
                    ),

                "order_date":
                    fake.date_between(
                        start_date="-2y",
                        end_date="today"
                    ).strftime(
                        "%Y-%m-%d"
                    ),

                "quantity":
                    quantity,

                "unit_price":
                    unit_price,

                "discount":
                    discount,

                "tax":
                    tax,

                "total_amount":
                    total_amount,

                "payment_method":
                    random.choice(
                        [
                            "Credit Card",
                            "Debit Card",
                            "UPI",
                            "Net Banking",
                            "COD"
                        ]
                    ),

                "order_status":
                    random.choice(
                        [
                            "PLACED",
                            "SHIPPED",
                            "DELIVERED",
                            "CANCELLED"
                        ]
                    )
            }
        )

    df = pd.DataFrame(records)

    apply_null_values(
        df,
        scenario_counts.get(
            "Null Values",
            0
        )
    )

    apply_invalid_date(
        df,
        scenario_counts.get(
            "Invalid Date",
            0
        )
    )

    apply_negative_amount(
        df,
        scenario_counts.get(
            "Negative Amount",
            0
        )
    )

    apply_invalid_foreign_key(
        df,
        scenario_counts.get(
            "Invalid Foreign Key",
            0
        )
    )

    df = apply_duplicates(
        df,
        scenario_counts.get(
            "Duplicate Records",
            0
        )
    )

    return df[columns]


# ============================================================
# TRANSACTION GENERATOR
# ============================================================

def generate_transactions(
    rows,
    columns,
    scenario_counts,
    orders_df
):

    valid_orders = (
        orders_df[
            "order_id"
        ]
        .dropna()
        .tolist()
    )

    customer_map = dict(
        zip(
            orders_df["order_id"],
            orders_df["customer_id"]
        )
    )

    records = []

    for i in range(rows):

        order_id = random.choice(
            valid_orders
        )

        records.append(
            {
                "transaction_id":
                    f"TXN{100000 + i}",

                "order_id":
                    order_id,

                "customer_id":
                    customer_map.get(
                        order_id
                    ),

                "transaction_date":
                    fake.date_between(
                        start_date="-2y",
                        end_date="today"
                    ).strftime(
                        "%Y-%m-%d"
                    ),

                "transaction_type":
                    random.choice(
                        [
                            "PAYMENT",
                            "REFUND",
                            "CREDIT",
                            "DEBIT"
                        ]
                    ),

                "transaction_amount":
                    round(
                        random.uniform(
                            100,
                            50000
                        ),
                        2
                    ),

                "payment_method":
                    random.choice(
                        [
                            "Credit Card",
                            "Debit Card",
                            "UPI",
                            "Net Banking"
                        ]
                    ),

                "transaction_status":
                    random.choice(
                        [
                            "SUCCESS",
                            "FAILED",
                            "PENDING"
                        ]
                    ),

                "currency":
                    random.choice(
                        [
                            "INR",
                            "USD",
                            "EUR"
                        ]
                    )
            }
        )

    df = pd.DataFrame(records)

    apply_null_values(
        df,
        scenario_counts.get(
            "Null Values",
            0
        )
    )

    apply_invalid_date(
        df,
        scenario_counts.get(
            "Invalid Date",
            0
        )
    )

    apply_negative_amount(
        df,
        scenario_counts.get(
            "Negative Amount",
            0
        )
    )

    apply_invalid_foreign_key(
        df,
        scenario_counts.get(
            "Invalid Foreign Key",
            0
        )
    )

    df = apply_duplicates(
        df,
        scenario_counts.get(
            "Duplicate Records",
            0
        )
    )

    return df[columns]


# ============================================================
# SHIPMENT GENERATOR
# ============================================================

def generate_shipments(
    rows,
    columns,
    scenario_counts,
    orders_df
):

    valid_orders = (
        orders_df[
            "order_id"
        ]
        .dropna()
        .tolist()
    )

    customer_map = dict(
        zip(
            orders_df["order_id"],
            orders_df["customer_id"]
        )
    )

    records = []

    for i in range(rows):

        order_id = random.choice(
            valid_orders
        )

        shipment_date = (
            fake.date_between(
                start_date="-1y",
                end_date="today"
            )
        )

        delivery_date = (
            shipment_date
            + timedelta(
                days=random.randint(
                    1,
                    7
                )
            )
        )

        records.append(
            {
                "shipment_id":
                    f"SHIP{100000 + i}",

                "order_id":
                    order_id,

                "customer_id":
                    customer_map.get(
                        order_id
                    ),

                "shipment_date":
                    shipment_date.strftime(
                        "%Y-%m-%d"
                    ),

                "delivery_date":
                    delivery_date.strftime(
                        "%Y-%m-%d"
                    ),

                "carrier":
                    random.choice(
                        [
                            "DHL",
                            "FedEx",
                            "BlueDart",
                            "Delhivery",
                            "DTDC"
                        ]
                    ),

                "tracking_number":
                    fake.bothify(
                        "TRK##########"
                    ),

                "shipping_city":
                    fake.city(),

                "shipping_state":
                    fake.state(),

                "shipment_status":
                    random.choice(
                        [
                            "CREATED",
                            "IN_TRANSIT",
                            "DELIVERED",
                            "RETURNED"
                        ]
                    )
            }
        )

    df = pd.DataFrame(records)

    apply_null_values(
        df,
        scenario_counts.get(
            "Null Values",
            0
        )
    )

    apply_invalid_date(
        df,
        scenario_counts.get(
            "Invalid Date",
            0
        )
    )

    apply_invalid_foreign_key(
        df,
        scenario_counts.get(
            "Invalid Foreign Key",
            0
        )
    )

    df = apply_duplicates(
        df,
        scenario_counts.get(
            "Duplicate Records",
            0
        )
    )

    return df[columns]


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "⚙️ Generator Configuration"
)


# ============================================================
# GENERATION MODE
# ============================================================

generation_mode = st.sidebar.radio(
    "Generation Mode",
    [
        "Generate One File",
        "Generate All Files"
    ]
)


# ============================================================
# FILE SELECTION
# ============================================================

if generation_mode == "Generate One File":

    selected_file = st.sidebar.selectbox(
        "Select File",
        DATASETS
    )

else:

    selected_file = None


# ============================================================
# ROW COUNT
# ============================================================

rows = st.sidebar.number_input(
    "Number of Rows",
    min_value=1,
    max_value=1_000_000,
    value=1000,
    step=100
)


# ============================================================
# SCENARIO SELECTION
# ============================================================

st.sidebar.subheader(
    "🧪 Test Scenarios"
)

select_all_scenarios = st.sidebar.checkbox(
    "Select All Scenarios",
    value=False
)

if select_all_scenarios:

    selected_scenarios = SCENARIOS.copy()

else:

    selected_scenarios = st.sidebar.multiselect(
        "Select Scenario(s)",
        SCENARIOS,
        default=["Positive"]
    )


# ============================================================
# PERCENTAGE CONTROLS
# ============================================================

st.sidebar.subheader(
    "📊 Scenario Distribution"
)

percentages = {}

for scenario in selected_scenarios:

    if scenario == "Positive":

        percentages[scenario] = (
            st.sidebar.slider(
                "Positive %",
                0,
                100,
                70
            )
        )

    elif scenario == "Null Values":

        percentages[scenario] = (
            st.sidebar.slider(
                "Null Values %",
                0,
                100,
                5
            )
        )

    elif scenario == "Duplicate Records":

        percentages[scenario] = (
            st.sidebar.slider(
                "Duplicate %",
                0,
                100,
                5
            )
        )

    elif scenario == "Invalid Email":

        percentages[scenario] = (
            st.sidebar.slider(
                "Invalid Email %",
                0,
                100,
                5
            )
        )

    elif scenario == "Invalid Phone":

        percentages[scenario] = (
            st.sidebar.slider(
                "Invalid Phone %",
                0,
                100,
                5
            )
        )

    elif scenario == "Invalid Date":

        percentages[scenario] = (
            st.sidebar.slider(
                "Invalid Date %",
                0,
                100,
                5
            )
        )

    elif scenario == "Negative Amount":

        percentages[scenario] = (
            st.sidebar.slider(
                "Negative Amount %",
                0,
                100,
                3
            )
        )

    elif scenario == "Invalid Foreign Key":

        percentages[scenario] = (
            st.sidebar.slider(
                "Invalid FK %",
                0,
                100,
                2
            )
        )


configured_percentage = sum(
    percentages.values()
)


st.sidebar.metric(
    "Configured %",
    f"{configured_percentage}%"
)

if configured_percentage > 100:

    st.sidebar.error(
        "Configured percentage is greater than 100%"
    )

elif configured_percentage < 100:

    st.sidebar.info(
        f"{100 - configured_percentage}% "
        "will be Positive records."
    )


# ============================================================
# COLUMN SELECTION
# ============================================================

st.sidebar.subheader(
    "📋 Column Selection"
)


column_definition = get_column_definition(
    selected_file
) if selected_file else None


if generation_mode == "Generate One File":

    selected_columns = st.sidebar.multiselect(
        "Select Columns",
        list(
            column_definition.keys()
        ),
        default=list(
            column_definition.keys()
        )
    )

else:

    st.sidebar.info(
        "All columns will be generated for all files."
    )

    selected_columns = None


# ============================================================
# GENERATE BUTTON
# ============================================================

generate_button = st.sidebar.button(
    "🚀 Generate Test Data",
    use_container_width=True
)


# ============================================================
# GENERATION
# ============================================================

if generate_button:

    if not selected_scenarios:

        st.error(
            "Please select at least one scenario."
        )

        st.stop()

    if configured_percentage > 100:

        st.error(
            "Scenario percentages cannot exceed 100%."
        )

        st.stop()

    if (
        generation_mode == "Generate One File"
        and not selected_columns
    ):

        st.error(
            "Please select at least one column."
        )

        st.stop()

    scenario_counts = (
        generate_scenario_counts(
            rows,
            selected_scenarios,
            percentages
        )
    )

    if scenario_counts is None:

        st.error(
            "Scenario percentage is greater than 100%."
        )

        st.stop()

    progress = st.progress(0)

    # ========================================================
    # CUSTOMER
    # ========================================================

    if (
        generation_mode == "Generate All Files"
        or selected_file == "Customer"
    ):

        with st.spinner(
            "Generating Customer data..."
        ):

            customer_columns = (
                selected_columns
                if selected_file == "Customer"
                else list(
                    CUSTOMER_COLUMNS.keys()
                )
            )

            customer_df = generate_customer(
                rows,
                customer_columns,
                scenario_counts
            )

            st.session_state.generated_files[
                "customer.csv"
            ] = customer_df

    progress.progress(
        20 if generation_mode == "Generate All Files"
        else 100
    )

    # ========================================================
    # PRODUCT
    # ========================================================

    if (
        generation_mode == "Generate All Files"
        or selected_file == "Product"
    ):

        with st.spinner(
            "Generating Product data..."
        ):

            product_columns = (
                selected_columns
                if selected_file == "Product"
                else list(
                    PRODUCT_COLUMNS.keys()
                )
            )

            product_df = generate_product(
                rows,
                product_columns,
                scenario_counts
            )

            st.session_state.generated_files[
                "product.csv"
            ] = product_df

    if generation_mode == "Generate All Files":

        progress.progress(40)

    # ========================================================
    # PREPARE CUSTOMER / PRODUCT IDS
    # ========================================================

    if (
        "customer.csv"
        in st.session_state.generated_files
    ):

        customer_df = (
            st.session_state.generated_files[
                "customer.csv"
            ]
        )

    else:

        customer_df = generate_customer(
            rows,
            list(
                CUSTOMER_COLUMNS.keys()
            ),
            {
                "Positive": rows
            }
        )

    if (
        "product.csv"
        in st.session_state.generated_files
    ):

        product_df = (
            st.session_state.generated_files[
                "product.csv"
            ]
        )

    else:

        product_df = generate_product(
            rows,
            list(
                PRODUCT_COLUMNS.keys()
            ),
            {
                "Positive": rows
            }
        )

    customer_ids = (
        customer_df[
            "customer_id"
        ]
        .dropna()
        .tolist()
    )

    product_ids = (
        product_df[
            "product_id"
        ]
        .dropna()
        .tolist()
    )

    # ========================================================
    # ORDERS
    # ========================================================

    if (
        generation_mode == "Generate All Files"
        or selected_file == "Orders"
    ):

        with st.spinner(
            "Generating Orders data..."
        ):

            order_columns = (
                selected_columns
                if selected_file == "Orders"
                else list(
                    ORDER_COLUMNS.keys()
                )
            )

            orders_df = generate_orders(
                rows,
                order_columns,
                scenario_counts,
                customer_ids,
                product_ids
            )

            st.session_state.generated_files[
                "orders.csv"
            ] = orders_df

    if generation_mode == "Generate All Files":

        progress.progress(60)

    # ========================================================
    # PREPARE ORDERS
    # ========================================================

    if (
        "orders.csv"
        in st.session_state.generated_files
    ):

        orders_df = (
            st.session_state.generated_files[
                "orders.csv"
            ]
        )

    else:

        orders_df = generate_orders(
            rows,
            list(
                ORDER_COLUMNS.keys()
            ),
            {
                "Positive": rows
            },
            customer_ids,
            product_ids
        )

    # ========================================================
    # TRANSACTIONS
    # ========================================================

    if (
        generation_mode == "Generate All Files"
        or selected_file == "Transactions"
    ):

        with st.spinner(
            "Generating Transactions data..."
        ):

            transaction_columns = (
                selected_columns
                if selected_file == "Transactions"
                else list(
                    TRANSACTION_COLUMNS.keys()
                )
            )

            transactions_df = (
                generate_transactions(
                    rows,
                    transaction_columns,
                    scenario_counts,
                    orders_df
                )
            )

            st.session_state.generated_files[
                "transactions.csv"
            ] = transactions_df

    if generation_mode == "Generate All Files":

        progress.progress(80)

    # ========================================================
    # SHIPMENT
    # ========================================================

    if (
        generation_mode == "Generate All Files"
        or selected_file == "Shipment"
    ):

        with st.spinner(
            "Generating Shipment data..."
        ):

            shipment_columns = (
                selected_columns
                if selected_file == "Shipment"
                else list(
                    SHIPMENT_COLUMNS.keys()
                )
            )

            shipment_df = generate_shipments(
                rows,
                shipment_columns,
                scenario_counts,
                orders_df
            )

            st.session_state.generated_files[
                "shipment.csv"
            ] = shipment_df

    progress.progress(100)

    st.success(
        "✅ Test data generated successfully!"
    )


# ============================================================
# SCENARIO SUMMARY
# ============================================================

if generate_button:

    st.divider()

    st.subheader(
        "📊 Scenario Distribution"
    )

    summary = []

    for scenario, count in (
        scenario_counts.items()
    ):

        summary.append(
            {
                "Scenario": scenario,
                "Records": count,
                "Percentage":
                    round(
                        count / rows * 100,
                        2
                    )
            }
        )

    summary_df = pd.DataFrame(
        summary
    )

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# DISPLAY GENERATED FILES
# ============================================================

if st.session_state.generated_files:

    st.divider()

    st.header(
        "📁 Generated Files"
    )

    for filename, df in (
        st.session_state.generated_files.items()
    ):

        st.subheader(
            f"📄 {filename}"
        )

        col1, col2, col3, col4 = st.columns(
            4
        )

        with col1:

            st.metric(
                "Rows",
                f"{len(df):,}"
            )

        with col2:

            st.metric(
                "Columns",
                len(df.columns)
            )

        with col3:

            st.metric(
                "NULL Values",
                int(
                    df.isnull()
                    .sum()
                    .sum()
                )
            )

        with col4:

            st.metric(
                "Duplicates",
                int(
                    df.duplicated()
                    .sum()
                )
            )

        st.dataframe(
            df.head(100),
            use_container_width=True
        )

        csv_data = df.to_csv(
            index=False
        ).encode(
            "utf-8"
        )

        st.download_button(
            f"⬇️ Download {filename}",
            data=csv_data,
            file_name=filename,
            mime="text/csv",
            key=f"download_{filename}"
        )


# ============================================================
# DOWNLOAD ALL FILES
# ============================================================

if st.session_state.generated_files:

    st.divider()

    st.header(
        "📦 Download Files"
    )

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(
        zip_buffer,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for filename, df in (
            st.session_state.generated_files.items()
        ):

            zip_file.writestr(
                filename,
                df.to_csv(
                    index=False
                )
            )

    zip_buffer.seek(0)

    st.download_button(
        "📦 Download ALL Generated Files",
        data=zip_buffer,
        file_name="ecommerce_etl_test_data.zip",
        mime="application/zip",
        use_container_width=True
    )


# ============================================================
# CLEAR GENERATED FILES
# ============================================================

if st.session_state.generated_files:

    if st.button(
        "🗑️ Clear Generated Files"
    ):

        st.session_state.generated_files = {}

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "E-Commerce ETL Test Data Generator | "
    "Python + Faker + Pandas + Streamlit"
)