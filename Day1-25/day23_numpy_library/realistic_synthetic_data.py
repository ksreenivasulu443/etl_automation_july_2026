from faker import Faker
import pandas as pd
import random
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
fake = Faker('en_AU')

num_rows = 100

data = []

for _ in range(num_rows):
    data.append({
        "Identifier": fake.uuid4(),
        "Surname": fake.last_name(),
        "given name": fake.first_name(),
        "middle_initial": random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "suffix": "",
        "Primary_street_1": fake.street_address(),
        "Primary_street_2": "",
        "city": fake.city(),
        "state": fake.state(),
        "zipcode": fake.postcode(),
        "Primary_street_prev_1": fake.street_address(),
        "Primary_street_prev_2": "",
        "city_prev": fake.city(),
        "state_prev": fake.state(),
        "zipcode_prev": fake.postcode(),
        "Email": fake.email(),
        "Phone": fake.msisdn()[-10:],  # Indian 10-digit mobile number
        "birthmonth": random.randint(1, 12)
    })

df = pd.DataFrame(data)

print(df.head())