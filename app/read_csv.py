import csv

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        header = next(reader)
        data = []
        for row in reader:                                                  ## Existe un metodo que resume todo este proceso y es Dictreader
            iterable = zip(header, row)                                     ## Convierte todas las lineas del csv en diccionarios automatico
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
    


if __name__ == '__main__':
    data = read_csv('world_population.csv')
    print(data)