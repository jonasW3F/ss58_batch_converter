import csv
from substrateinterface.utils.ss58 import ss58_decode, ss58_encode

def convert_address(addr, input_id, output_id):
    pk = ss58_decode(addr, valid_ss58_format=input_id)
    return ss58_encode(pk, ss58_format=output_id)

def convert_csv_addresses(input_file, output_file, input_id, output_id):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        # Create CSV reader and writer
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['new_address'] if 'new_address' not in reader.fieldnames else reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Iterate over the rows and convert addresses
        for row in reader:
            addr = row['address']
            row['new_address'] = convert_address(addr, input_id, output_id)
            writer.writerow(row)

# File paths
input_csv = 'input_addresses.csv'
output_csv = 'converted_addresses.csv'

# Network IDs
input_id = 42
output_id = 2

# Convert the addresses
convert_csv_addresses(input_csv, output_csv, input_id, output_id)
