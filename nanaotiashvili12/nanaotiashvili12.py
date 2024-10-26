import csv

with open('titanic.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)  
    survived_list = []

 
    for row in csv_reader:
        if int(row[1]) == 1:  
            survived_list.append(row)


with open('survived.csv', 'w') as survived_file:
    csv_writer = csv.writer(survived_file)
    csv_writer.writerow(headers) 
    csv_writer.writerows(survived_list)
print("survived.csv ") 




import csv

with open('organizations-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) 
    organizations = list(csv_reader) 


sorted_organizations = sorted(organizations, key=lambda x: int(x['Number of employees']))


with open('sorted_csv.csv', 'w', newline='') as sorted_file:
    fieldnames = organizations[0].keys()
    csv_writer = csv.DictWriter(sorted_file, fieldnames=fieldnames)
    csv_writer.writeheader()  
    csv_writer.writerows(sorted_organizations)


print("sorted_csv.csv")



import csv

with open('organizations-100.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  
    ssl_companies = []

    for row in csv_reader:
        if row['Website'].startswith('https://'):
            ssl_companies.append({
                'ID': row['Organization Id'],
                'Company Name': row['Name'],
                'Website': row['Website'],
                'Industry': row['Industry'],
                'Number of Employees': row['Number of employees']
            })

with open('ssl_companies.csv', 'w', newline='') as ssl_file:
    fieldnames = ['ID', 'Company Name', 'Website', 'Industry', 'Number of Employees']
    csv_writer = csv.DictWriter(ssl_file, fieldnames=fieldnames)
    csv_writer.writeheader() 
    csv_writer.writerows(ssl_companies)
print("ssl_companies.csv ")
