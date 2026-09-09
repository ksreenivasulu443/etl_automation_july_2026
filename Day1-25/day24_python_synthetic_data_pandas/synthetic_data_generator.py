import streamlit as st
import pandas as pd
import numpy as np
import random
import string
import io
import zipfile

from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce ETL Test Data Generator",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 E-Commerce ETL Test Data Generator")
st.caption(
    "Generate positive and negative test data for ETL / Data Quality testing"
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

# ============================================================
# GENERATOR FUNCTIONS
# ============================================================

def generate_customer_data(rows, selected_columns, scenario):
    data = []

    for i in range(rows):

        customer_id = f"CUST{100000 + i}"

        record = {
            "customer_id": customer_id,
            "name": fake.name(),
            "phone": fake.numerify("##########"),
            "gender": random.choice(["Male", "Female", "Other"]),
            "email": fake.email(),
            "date_of_birth": fake.date_of_birth(
                minimum_age=18,
                maximum_age=70
            ).strftime("%Y-%m-%d"),
            "city": fake.city(),
            "state": fake.state(),
            "country": "India",
            "postal_code": fake.postcode(),
            "registration_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            ).strftime("%Y-%m-%d"),
            "customer_status": random.choice(
                ["ACTIVE", "INACTIVE", "SUSPENDED"]
            )
        }

        data.append(record)

    df = pd.DataFrame(data)

    df = apply_negative_scenarios(
        df,
        scenario,
        primary_key="customer_id"
    )

    return df[selected_columns]


def generate_product_data(rows, selected_columns, scenario):
    data = []

    for i in range(rows):

        price = round(random.uniform(100, 50000), 2)
        cost = round(price * random.uniform(0.4, 0.8), 2)

        record = {
            "product_id": f"PROD{100000 + i}",
            "product_name": fake.catch_phrase(),
            "category": random.choice(
                ["Electronics", "Clothing", "Home",
                 "Beauty", "Sports", "Books"]
            ),
            "subcategory": random.choice(
                ["Mobile", "Laptop", "Shoes",
                 "Furniture", "Accessories", "Fitness"]
            ),
            "brand": random.choice(
                ["Nike", "Samsung", "Apple",
                 "Sony", "Adidas", "Dell"]
            ),
            "price": price,
            "cost": cost,
            "stock_quantity": random.randint(0, 500),
            "product_status": random.choice(
                ["ACTIVE", "INACTIVE", "DISCONTINUED"]
            ),
            "created_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ).strftime("%Y-%m-%d")
        }

        data.append(record)

    df = pd.DataFrame(data)

    df = apply_negative_scenarios(
        df,
        scenario,
        primary_key="product_id"
    )

    return df[selected_columns]


def generate_order_data(
    rows,
    selected_columns,
    scenario,
    customer_ids,
    product_df
):

    data = []

    for i in range(rows):

        order_id = f"ORD{100000 + i}"

        customer_id = random.choice(customer_ids)

        product_id = random.choice(
            product_df["product_id"].tolist()
        )

        quantity = random.randint(1, 10)
        unit_price = round(random.uniform(100, 30000), 2)

        discount = round(
            random.uniform(0, unit_price * 0.2),
            2
        )

        tax = round(
            (quantity * unit_price - discount) * 0.18,
            2
        )

        total_amount = round(
            quantity * unit_price
            - discount
            + tax,
            2
        )

        record = {
            "order_id": order_id,
            "customer_id": customer_id,
            "product_id": product_id,
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ).strftime("%Y-%m-%d"),
            "quantity": quantity,
            "unit_price": unit_price,
            "discount": discount,
            "tax": tax,
            "total_amount": total_amount,
            "payment_method": random.choice(
                ["Credit Card", "Debit Card",
                 "UPI", "Net Banking", "COD"]
            ),
            "order_status": random.choice(
                ["PLACED", "SHIPPED",
                 "DELIVERED", "CANCELLED"]
            )
        }

        data.append(record)

    df = pd.DataFrame(data)

    df = apply_negative_scenarios(
        df,
        scenario,
        primary_key="order_id"
    )

    return df[selected_columns]


def generate_transaction_data(
    rows,
    selected_columns,
    scenario,
    order_df
):

    data = []

    order_ids = order_df["order_id"].tolist()
    customer_map = dict(
        zip(
            order_df["order_id"],
            order_df["customer_id"]
        )
    )

    for i in range(rows):

        order_id = random.choice(order_ids)

        amount = round(
            random.uniform(100, 50000),
            2
        )

        record = {
            "transaction_id": f"TXN{100000 + i}",
            "order_id": order_id,
            "customer_id": customer_map[order_id],
            "transaction_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ).strftime("%Y-%m-%d"),
            "transaction_type": random.choice(
                ["PAYMENT", "REFUND", "CREDIT", "DEBIT"]
            ),
            "transaction_amount": amount,
            "payment_method": random.choice(
                ["Credit Card", "Debit Card",
                 "UPI", "Net Banking"]
            ),
            "transaction_status": random.choice(
                ["SUCCESS", "FAILED", "PENDING"]
            ),
            "currency": random.choice(
                ["INR", "USD", "EUR"]
            )
        }

        data.append(record)

    df = pd.DataFrame(data)

    df = apply_negative_scenarios(
        df,
        scenario,
        primary_key="transaction_id"
    )

    return df[selected_columns]


def generate_shipment_data(
    rows,
    selected_columns,
    scenario,
    order_df
):

    data = []

    order_ids = order_df["order_id"].tolist()

    customer_map = dict(
        zip(
            order_df["order_id"],
            order_df["customer_id"]
        )
    )

    for i in range(rows):

        order_id = random.choice(order_ids)

        shipment_date = fake.date_between(
            start_date="-1y",
            end_date="today"
        )

        delivery_date = shipment_date + timedelta(
            days=random.randint(1, 7)
        )

        record = {
            "shipment_id": f"SHIP{100000 + i}",
            "order_id": order_id,
            "customer_id": customer_map[order_id],
            "shipment_date": shipment_date.strftime(
                "%Y-%m-%d"
            ),
            "delivery_date": delivery_date.strftime(
                "%Y-%m-%d"
            ),
            "carrier": random.choice(
                ["DHL", "FedEx", "BlueDart",
                 "Delhivery", "DTDC"]
            ),
            "tracking_number": fake.bothify(
                "TRK##########"
            ),
            "shipping_city": fake.city(),
            "shipping_state": fake.state(),
            "shipment_status": random.choice(
                ["CREATED", "IN_TRANSIT",
                 "DELIVERED", "RETURNED"]
            )
        }

        data.append(record)

    df = pd.DataFrame(data)

    df = apply_negative_scenarios(
        df,
        scenario,
        primary_key="shipment_id"
    )

    return df[selected_columns]


# ============================================================
# NEGATIVE SCENARIO ENGINE
# ============================================================

def apply_negative_scenarios(
    df,
    scenario,
    primary_key=None
):

    if scenario == "Positive":

        return df

    if scenario == "Null Values":

        if len(df) > 0:

            columns = random.sample(
                list(df.columns),
                min(3, len(df.columns))
            )

            for col in columns:

                indexes = df.sample(
                    frac=0.05
                ).index

                df.loc[indexes, col] = None

    elif scenario == "Duplicate Records":

        if len(df) > 10:

            duplicate_rows = df.sample(
                min(10, len(df))
            )

            df = pd.concat(
                [df, duplicate_rows],
                ignore_index=True
            )

    elif scenario == "Invalid Email":

        if "email" in df.columns:

            indexes = df.sample(
                frac=0.05
            ).index

            df.loc[
                indexes,
                "email"
            ] = "invalid_email"

    elif scenario == "Invalid Phone":

        if "phone" in df.columns:

            indexes = df.sample(
                frac=0.05
            ).index

            df.loc[
                indexes,
                "phone"
            ] = "123"

    elif scenario == "Negative Amount":

        amount_columns = [
            c for c in df.columns
            if "amount" in c
            or c in ["price", "cost", "discount"]
        ]

        for col in amount_columns:

            indexes = df.sample(
                frac=0.05
            ).index

            df.loc[
                indexes,
                col
            ] = -abs(
                pd.to_numeric(
                    df.loc[indexes, col],
                    errors="coerce"
                )
            )

    elif scenario == "Invalid Date":

        date_columns = [
            c for c in df.columns
            if "date" in c
        ]

        for col in date_columns:

            indexes = df.sample(
                frac=0.05
            ).index

            df.loc[
                indexes,
                col
            ] = "INVALID_DATE"

    return df


# ============================================================
# UI
# ============================================================

st.sidebar.header("⚙️ Generator Configuration")

dataset_type = st.sidebar.selectbox(
    "Select Dataset",
    [
        "Customer",
        "Product",
        "Orders",
        "Transactions",
        "Shipment",
        "Generate All"
    ]
)

rows = st.sidebar.number_input(
    "Number of Rows",
    min_value=1,
    max_value=1_000_000,
    value=1000,
    step=100
)

scenario = st.sidebar.selectbox(
    "Test Scenario",
    [
        "Positive",
        "Null Values",
        "Duplicate Records",
        "Invalid Email",
        "Invalid Phone",
        "Negative Amount",
        "Invalid Date"
    ]
)

st.sidebar.subheader("📋 Column Selection")


def select_columns(column_dictionary):

    return st.sidebar.multiselect(
        "Select Columns",
        options=list(column_dictionary.keys()),
        default=list(column_dictionary.keys())
    )


# ============================================================
# SESSION STATE
# ============================================================

if "customer_df" not in st.session_state:
    st.session_state.customer_df = None

if "product_df" not in st.session_state:
    st.session_state.product_df = None

if "order_df" not in st.session_state:
    st.session_state.order_df = None

if "transaction_df" not in st.session_state:
    st.session_state.transaction_df = None

if "shipment_df" not in st.session_state:
    st.session_state.shipment_df = None


# ============================================================
# GENERATE BUTTON
# ============================================================

if dataset_type == "Customer":

    selected_columns = select_columns(
        CUSTOMER_COLUMNS
    )

elif dataset_type == "Product":

    selected_columns = select_columns(
        PRODUCT_COLUMNS
    )

elif dataset_type == "Orders":

    selected_columns = select_columns(
        ORDER_COLUMNS
    )

elif dataset_type == "Transactions":

    selected_columns = select_columns(
        TRANSACTION_COLUMNS
    )

elif dataset_type == "Shipment":

    selected_columns = select_columns(
        SHIPMENT_COLUMNS
    )

else:

    selected_columns = None


generate_button = st.sidebar.button(
    "🚀 Generate Test Data",
    use_container_width=True
)


# ============================================================
# GENERATE DATA
# ============================================================

if generate_button:

    with st.spinner("Generating test data..."):

        # ----------------------------------------------------
        # CUSTOMER
        # ----------------------------------------------------

        if dataset_type in [
            "Customer",
            "Orders",
            "Transactions",
            "Shipment",
            "Generate All"
        ]:

            customer_columns = (
                list(CUSTOMER_COLUMNS.keys())
                if dataset_type == "Generate All"
                else (
                    selected_columns
                    if dataset_type == "Customer"
                    else list(CUSTOMER_COLUMNS.keys())
                )
            )

            st.session_state.customer_df = (
                generate_customer_data(
                    rows,
                    customer_columns,
                    scenario
                )
            )

        # ----------------------------------------------------
        # PRODUCT
        # ----------------------------------------------------

        if dataset_type in [
            "Product",
            "Orders",
            "Generate All"
        ]:

            product_columns = (
                list(PRODUCT_COLUMNS.keys())
                if dataset_type == "Generate All"
                else (
                    selected_columns
                    if dataset_type == "Product"
                    else list(PRODUCT_COLUMNS.keys())
                )
            )

            st.session_state.product_df = (
                generate_product_data(
                    rows,
                    product_columns,
                    scenario
                )
            )

        # ----------------------------------------------------
        # ORDERS
        # ----------------------------------------------------

        if dataset_type in [
            "Orders",
            "Transactions",
            "Shipment",
            "Generate All"
        ]:

            if st.session_state.customer_df is None:

                st.session_state.customer_df = (
                    generate_customer_data(
                        rows,
                        list(CUSTOMER_COLUMNS.keys()),
                        "Positive"
                    )
                )

            if st.session_state.product_df is None:

                st.session_state.product_df = (
                    generate_product_data(
                        rows,
                        list(PRODUCT_COLUMNS.keys()),
                        "Positive"
                    )
                )

            order_columns = (
                list(ORDER_COLUMNS.keys())
                if dataset_type == "Generate All"
                else (
                    selected_columns
                    if dataset_type == "Orders"
                    else list(ORDER_COLUMNS.keys())
                )
            )

            st.session_state.order_df = (
                generate_order_data(
                    rows,
                    order_columns,
                    scenario,
                    st.session_state.customer_df[
                        "customer_id"
                    ].tolist(),
                    st.session_state.product_df
                )
            )

        # ----------------------------------------------------
        # TRANSACTIONS
        # ----------------------------------------------------

        if dataset_type in [
            "Transactions",
            "Generate All"
        ]:

            if st.session_state.order_df is None:

                st.session_state.order_df = (
                    generate_order_data(
                        rows,
                        list(ORDER_COLUMNS.keys()),
                        "Positive",
                        st.session_state.customer_df[
                            "customer_id"
                        ].tolist(),
                        st.session_state.product_df
                    )
                )

            transaction_columns = (
                list(TRANSACTION_COLUMNS.keys())
                if dataset_type == "Generate All"
                else selected_columns
            )

            st.session_state.transaction_df = (
                generate_transaction_data(
                    rows,
                    transaction_columns,
                    scenario,
                    st.session_state.order_df
                )
            )

        # ----------------------------------------------------
        # SHIPMENT
        # ----------------------------------------------------

        if dataset_type in [
            "Shipment",
            "Generate All"
        ]:

            if st.session_state.order_df is None:

                st.session_state.order_df = (
                    generate_order_data(
                        rows,
                        list(ORDER_COLUMNS.keys()),
                        "Positive",
                        st.session_state.customer_df[
                            "customer_id"
                        ].tolist(),
                        st.session_state.product_df
                    )
                )

            shipment_columns = (
                list(SHIPMENT_COLUMNS.keys())
                if dataset_type == "Generate All"
                else selected_columns
            )

            st.session_state.shipment_df = (
                generate_shipment_data(
                    rows,
                    shipment_columns,
                    scenario,
                    st.session_state.order_df
                )
            )

    st.success("✅ Test data generated successfully!")


# ============================================================
# DISPLAY RESULTS
# ============================================================

def display_dataframe(title, df):

    if df is not None:

        st.subheader(title)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows",
                len(df)
            )

        with col2:
            st.metric(
                "Columns",
                len(df.columns)
            )

        with col3:
            st.metric(
                "Null Values",
                int(df.isnull().sum().sum())
            )

        st.dataframe(
            df.head(100),
            use_container_width=True
        )


display_dataframe(
    "👤 Customer Data",
    st.session_state.customer_df
)

display_dataframe(
    "📦 Product Data",
    st.session_state.product_df
)

display_dataframe(
    "🛒 Order Data",
    st.session_state.order_df
)

display_dataframe(
    "💳 Transaction Data",
    st.session_state.transaction_df
)

display_dataframe(
    "🚚 Shipment Data",
    st.session_state.shipment_df
)


# ============================================================
# DOWNLOAD FUNCTIONS
# ============================================================

def dataframe_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


def create_zip():

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(
        zip_buffer,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        datasets = {
            "customer.csv":
                st.session_state.customer_df,

            "product.csv":
                st.session_state.product_df,

            "orders.csv":
                st.session_state.order_df,

            "transactions.csv":
                st.session_state.transaction_df,

            "shipment.csv":
                st.session_state.shipment_df
        }

        for filename, df in datasets.items():

            if df is not None:

                zip_file.writestr(
                    filename,
                    df.to_csv(index=False)
                )

    zip_buffer.seek(0)

    return zip_buffer


# ============================================================
# DOWNLOAD SECTION
# ============================================================

st.divider()

st.header("⬇️ Download Generated Data")

if st.session_state.customer_df is not None:

    st.download_button(
        "Download Customer CSV",
        dataframe_to_csv(
            st.session_state.customer_df
        ),
        "customer.csv",
        "text/csv"
    )

if st.session_state.product_df is not None:

    st.download_button(
        "Download Product CSV",
        dataframe_to_csv(
            st.session_state.product_df
        ),
        "product.csv",
        "text/csv"
    )

if st.session_state.order_df is not None:

    st.download_button(
        "Download Orders CSV",
        dataframe_to_csv(
            st.session_state.order_df
        ),
        "orders.csv",
        "text/csv"
    )

if st.session_state.transaction_df is not None:

    st.download_button(
        "Download Transactions CSV",
        dataframe_to_csv(
            st.session_state.transaction_df
        ),
        "transactions.csv",
        "text/csv"
    )

if st.session_state.shipment_df is not None:

    st.download_button(
        "Download Shipment CSV",
        dataframe_to_csv(
            st.session_state.shipment_df
        ),
        "shipment.csv",
        "text/csv"
    )


if any([
    st.session_state.customer_df is not None,
    st.session_state.product_df is not None,
    st.session_state.order_df is not None,
    st.session_state.transaction_df is not None,
    st.session_state.shipment_df is not None
]):

    st.download_button(
        "📦 Download ALL Files as ZIP",
        create_zip(),
        "ecommerce_test_data.zip",
        "application/zip",
        use_container_width=True
    )