import utils
import read_csv
import graphics

def run():
    data = read_csv.read_csv('world_population.csv')
    country = input('Digita el pais => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        graphics.generate_bar_chart(labels, values)
    
    print(result)

    names, percentenge = utils.world_population(data)
    graphics.generate_pie_chart(names,percentenge)

if __name__ == '__main__': ## Esto sirve para correr el modulo aunque sea manejado por otro modulo 
    run() ## Se aplica la funcion 