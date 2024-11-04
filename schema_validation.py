import pandas as pd

# Expected schema
expected_schema = {
    'customer_id': 'int64',
    'transaction_date': 'datetime64[ns]',
    'amount': 'float64',
    'status': 'object'
}

def validate_schema(dataframe, schema):
    for col, dtype in schema.items():
        if col not in dataframe.columns or dataframe[col].dtype != dtype:
            print(f"Schema mismatch: Column {col} should be {dtype}, but is {dataframe[col].dtype}")
            return False
    print("Schema validation passed.")
    return True

# Load sample data
data = pd.read_csv('data/transactions.csv', parse_dates=['transaction_date'])
validate_schema(data, expected_schema)
