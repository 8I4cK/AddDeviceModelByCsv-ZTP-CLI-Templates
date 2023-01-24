import csv

with open('models.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        model_name = line[0]
        model_type = line[1]
        model_vendor = line[2]
        model_os = line[3]
        
        print(f'Creating model: {model_name} | Type: {model_type} | Vendor: {model_vendor} | OS: {model_os}')
