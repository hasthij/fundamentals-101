Opening files
# Writing
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")

# Reading
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

CSV Format

name,age,city
Anna,25,Colombo
Ravi,30,Kandy

Writing
import csv

rows = [
    ["name", "age", "city"],
    ["Anna", 25, "Colombo"],
    ["Ravi", 30, "Kandy"],
]

with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)      # writerow() for one row


Reading
import csv

with open("people.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])

main functions of JSON
json.dump(data, file)
json.load(file)
json.dumps(data)
json.loads(text)

Status Codes
200 - OK
201 - Created
400 - Bad Request
404 - Not Found
500 - Server Error

import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url,timeout=10)

print(response.status_code)
data = response.json()
print(data) use [] to get only certain parts of the JSON return 