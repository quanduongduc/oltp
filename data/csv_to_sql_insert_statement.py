import csv

def csv_to_sql(csv_file, table_name, output_sql_file):
    # Open CSV file for reading
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        
        # Open SQL file for writing
        with open(output_sql_file, 'w') as sql_file:
            # Iterate over each row in the CSV file
            for row in reader:
                # Generate SQL INSERT statement
                formatted_row = []
                for value in row:
                    if value.isdigit():  # Check if the value is a number
                        formatted_row.append(value)  # Keep it as is
                    else:
                        formatted_row.append(repr(value))  # Use repr() for non-numeric values
                sql_insert = f"INSERT INTO {table_name} VALUES ({', '.join(formatted_row)});\n"
                # Write SQL INSERT statement to the SQL file
                sql_file.write(sql_insert)


# Example usage
csv_file = 'amazon_prime_users_dataset/dim_location_data.csv'  # Change this to the path of your CSV file
table_name = 'location'  # Change this to the name of your SQL table
output_sql_file = '1_databases_creation/location_data.sql'  # Change this to the path where you want to save the SQL file

csv_to_sql(csv_file, table_name, output_sql_file)
