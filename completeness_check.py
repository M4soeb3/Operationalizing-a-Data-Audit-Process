def check_completeness(dataframe, required_columns):
    missing_data = dataframe[required_columns].isnull().sum()
    print("Missing data counts:\n", missing_data)
    if missing_data.any():
        print("Warning: Missing values detected.")
    else:
        print("All required columns are complete.")
    return missing_data

required_columns = ['customer_id', 'transaction_date', 'amount']
check_completeness(data, required_columns)
