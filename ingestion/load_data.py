import duckdb

def load_data(file_path: str, table_name: str) -> None:
    # Connect to DuckDB (in-memory)
    conn = duckdb.connect()

    # Create a table and load data from the CSV file
    conn.execute(f"""
        CREATE TABLE {table_name} AS 
        SELECT * FROM read_csv_auto('{file_path}')
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    # Example usage
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\bureau.csv", "bureau")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\bureau_balance.csv", "bureau_balance")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\credit_card_balance.csv", "credit_card_balance")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\installments_payments.csv", "installments_payments")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\previous_application.csv", "previous_application")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\POS_CASH_balance.csv", "pos_cash_balance")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\application_train.csv", "application_train")
    load_data("D:\\DEPI\\Project\\credit-risk-analysis\\Data\\application_test.csv", "application_test")