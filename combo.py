import re
import chardet

def extract_email_password(account_list):
    # Regular expression to match email and password
    email_password_pattern = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)[^a-zA-Z0-9]*([a-zA-Z0-9!@#$%^&*()_+]+)')
    
    # Set to store unique email:password pairs
    unique_accounts = set()
    
    for account in account_list:
        match = email_password_pattern.search(account)
        if match:
            email = match.group(1)
            password = match.group(2)
            unique_accounts.add(f"{email}:{password}")
    
    return unique_accounts

def read_accounts_from_file(file_path):
    # Detect the file encoding using chardet
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    
    # Read the file using the detected encoding
    with open(file_path, 'r', encoding=encoding) as file:
        return file.readlines()

def save_accounts_to_file(file_path, accounts):
    # Save the file with UTF-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:
        for account in accounts:
            file.write(account + "\n")

# File paths
input_file = "accounts.txt"  # Replace with your input file path
output_file = "formatted_accounts.txt"  # Replace with your desired output file path

# Read accounts from the input file
try:
    account_list = read_accounts_from_file(input_file)
except Exception as e:
    print(f"Error: {e}")
    exit()

# Extract and format email:password pairs, removing duplicates
formatted_accounts = extract_email_password(account_list)

# Save the formatted accounts to the output file
save_accounts_to_file(output_file, formatted_accounts)

print(f"Formatted accounts saved to {output_file}")