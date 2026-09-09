file_format = input("Enter file format: ").upper().strip()

if file_format == 'CSV':
    header = input("Enter header: ").upper().strip()
    sep = input("Enter sep (supported comma or pipe) : ").lower().strip()
    if header == 'Y' and sep in ( '|', 'pipe'):
        print("reading data from CSV with header and sep is |")
    elif header == 'Y' and sep in ( ',', 'comma'):
        print("reading data from CSV with header and sep is comma")
    elif header == 'N' and sep in ( '|', 'pipe'):
        print("reading data from CSV without header and sep is |")
    elif header == 'N' and sep in ( ',', 'comma'):
        print("reading data from CSV without header and sep is comma")
    else:
        print("we are inside csv file read and we only support header Y/N and sep = comma or pipe")
    
    print("reading data from CSV")
elif file_format == 'PARQUET':
    print("reading data from PARQUET")
elif file_format == 'AVRO':
    print("reading data from AVRO")
elif file_format == 'JSON':
    print("reading data from JSON")
elif file_format == 'EXCEL':
    print("reading data from EXCEl")
elif file_format == 'TXT':
    print("reading data from TXT")
elif file_format == 'HTML':
    print("reading data from HTML")
else:
    print("hello, We will only support csv, parquet,avro, json, txt, excel, html...try from the list of formats the mentioned here")
