import random
import csv


def idGenerator():
    identifier = random.randint(0, 999)
    return str(identifier).zfill(3)


def fixedIdGeneration(file):
    identifier = idGenerator()
    try:
        with open(file, 'r') as csvFile:
            csvReader = csv.DictReader(csvFile)
            for line in csvReader:
                if 'ID' in line and line['ID'] == identifier:
                    identifier = idGenerator()
                    csvFile.seek(0)  # reset file pointer
                    continue
                else:
                    break
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return None
    return identifier


def findId(file, fieldName, value):
    with open(file, 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            if row[fieldName] == value:
                return row['ID']
    return None
