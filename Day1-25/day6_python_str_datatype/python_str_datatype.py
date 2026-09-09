"""
#Documentation strings
#This is python_str_datatype.py create to practice str datatype
#created by : Sreeni
#created on : 23/07/2026
"""

import sys

str1 = "ETL Automation labs"


print("str1 value", str1)
print("str1 type", type(str1))
print("str1 id", id(str1))
print("str1 methods", dir(str1))
print("str1 size ", str1.__sizeof__())
print("size of str1 using sys", sys.getsizeof(str1))

print("str1 upper", str1.upper())
print("str1 lower", str1.lower())
print("-"*100)
str2 = 'ETL Automation labs'

print("str2 value", str2)
print("str2 type", type(str2))
print("str2 id", id(str2))
print("size of str2 using sys", sys.getsizeof(str2))

# str3 =  " It\'s raining outside "
#
# print("str3 value", str3)
# print("str3 type", type(str3))
# print("str3 id", id(str3))
# print("size of str3 using sys", sys.getsizeof(str3))

print("-"*100)
str4 = """ETL Automation labs"""

print("str4 value", str4)
print("str4 type", type(str4))
print("str4 id", id(str4))
print("size of str3 using sys", sys.getsizeof(str4))


print("-"*100)
str5 = '''ETL Automation labs'''

print("str5 value", str5)
print("str5 type", type(str5))
print("str5 id", id(str5))
print("size of str5 using sys", sys.getsizeof(str5))

str6 = ''' ETL (Extract, Transform, Load) testing ensures the accuracy, ' " integrity, and performance of data as it moves through the ETL process. Below are the key types of ETL testing:

1. Source Data Validation Testing This ensures that the data extracted from source systems is accurate and complete. It involves verifying data types, formats, ranges, and identifying anomalies like missing or duplicate records.

2. Source-to-Target Data Reconciliation Testing This type compares data in the source and target systems to ensure completeness and accuracy. It checks for mismatches in record counts, data values, and transformations to avoid data loss or corruption.

3. Data Transformation Testing This validates that data transformations adhere to business rules. It involves checking calculations, aggregations, filtering, and data joins to ensure the transformed data is accurate and usable.

4. Data Validation Testing This ensures the data in the target system meets quality standards. It includes checks for null values, format inconsistencies, and plausibility of data values.

5. Referential Integrity Testing This verifies that relationships between tables, such as foreign key constraints, are maintained after the ETL process. It ensures data dependencies and relationships are intact. '''


pkey = 'CustomerId' # "CustomerID"

query = ''' SELECT s.s_name, m.score, m.status, d.address_city, d.email_id, d.accomplishments
FROM student s
INNER JOIN marks m ON s.s_id = m.s_id
INNER JOIN details d ON m.school_id = d.school_id '''

date ="23-07-2026"


print
