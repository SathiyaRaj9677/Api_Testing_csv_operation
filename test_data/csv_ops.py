import csv

#Print all the lines/rows from the csv file which is available in the IDE 
with open("test_data/myfiles.csv", mode = 'r') as file:
    csvfile = csv.reader(file)
    for lines in csvfile:
        print(lines)

print("----------------------------------------------------------")

# Print all the lines/rows using dictreader from the csv file which is available in the IDE 
with open("test_data/myfiles.csv", mode = 'r') as file:
    csvfile = csv.DictReader(file)
    for lines in csvfile:
        print(lines)

print("----------------------------------------------------------")

#How print the rows without header
rows = []
with open("test_data/myfiles.csv", mode = 'r') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for lines in csvfile:
        rows.append(lines)
    print(rows)

for row in rows:
    print(row)

print("----------------------------------------------------------")

#How to validate a particular data is available in the row:
rows = []
with open("test_data/myfiles.csv", mode = 'r') as file:
    csvfile = csv.reader(file)
    header = next(csvfile)
    for lines in csvfile:
        rows.append(lines)
    print(rows)

for row in rows:
    if row[0] == "sam":
        print(row[0])
        break

print("----------------------------------------------------------")


#How To validate a particular data
# Define the target data for validation
target_user = "ram"
target_city = "perambalur"
expected_email = "ram@gmail.com"

# Open the CSV file
with open("test_data/myfiles.csv", mode='r') as file:
    csvfile = csv.reader(file)
    
    # Skip the header row
    next(csvfile)
    
    # Iterate through each row
    for row in csvfile:
        user, city, email = row
        
        # Check if this is the row we're looking for
        if user == target_user and city == target_city:
            # Validate the email
            if email == expected_email:
                print(f"Validation successful: {user}'s email is correct.")
            else:
                print(f"Validation failed: {user}'s email is incorrect.")
            break
    else:
        print(f"User {target_user} from {target_city} not found.")