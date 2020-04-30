import csv


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    companies = {}
    for line in reader:
        if list(line.values())[2] not in companies.keys():
            companies[list(line.values())[2]] = 1
        else:
            companies[list(line.values())[2]] += 1
    #  top-25
    for item in sorted(companies.items(), key=lambda x: x[1])[(len(companies.items()) - 25):(len(companies.items()))]:
        with open('cmc-finish.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([item[0], item[1]])
    return companies


if __name__ == "__main__":
    with open("cmc.csv") as f_obj:
        csv_dict_reader(f_obj)
