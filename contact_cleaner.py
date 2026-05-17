"""
Kyle Christensen
IS 303 - A03

Inputs:
- Number of contacts (int)
- For each contact: name (string), email (string)

Processes:
- Transform: convert names to title case and strip whitespace from emails
- Search: find duplicate email addresses
- Accumulator: count cleaned records

Outputs:
- Print original and cleaned contact information
- Print total cleaned records and duplicate count
"""

# Collect contacts from user
contacts = []

num_contacts = int(input("How many contacts do you want to clean in your contact book?  "))

for i in range(num_contacts):
    print(f"\nContact {i + 1}:")
    name = input("  Name: ")
    email = input("  Email: ")
    
    contact = {
        "name": name,
        "email": email
    }
    contacts.append(contact)

# Process the contacts
print("\n" + "="*16)
print("ORIGINAL CONTACTS")
print("="*16)

for contact in contacts:
    print(f"{contact['name']} - {contact['email']}")

# Transform pattern: clean the data
cleaned_contacts = []
for contact in contacts:
    cleaned_name = contact['name'].title()  # Convert to title case
    cleaned_email = contact['email'].strip().lower()  # Remove the spaces and lowercase
    
    cleaned_contact = {
        "name": cleaned_name,
        "email": cleaned_email
    }
    cleaned_contacts.append(cleaned_contact)

# Accumulator pattern --> count cleaned records
records_cleaned = len(cleaned_contacts)

# Search pattern --> find duplicate emails
duplicates = []
for i in range(len(cleaned_contacts)):
    for j in range(i + 1, len(cleaned_contacts)):
        if cleaned_contacts[i]['email'] == cleaned_contacts[j]['email']:
            if cleaned_contacts[i]['email'] not in duplicates:
                duplicates.append(cleaned_contacts[i]['email'])

# Summary output
print("\n" + "="*16)
print("CLEANED CONTACTS")
print("="*16)

for contact in cleaned_contacts:
    print(f"{contact['name']} - {contact['email']}")

print("\n" + "="*16)
print("CLEANING SUMMARY")
print("="*16)
print(f"Total records cleaned: {records_cleaned}")
print(f"Duplicate emails found: {len(duplicates)}")

if len(duplicates) > 0:
    print("\nDuplicate email addresses:")
    for email in duplicates:
        print(f"  - {email}")
else:
    print("No duplicate emails found!")