import pandas as pd
import matplotlib.pyplot as plt

def read_review_dates():
    f = 't23clientes.xlsx'
    read_f = pd.read_excel(f, engine='openpyxl')
    
    tres_filas = read_f.head(3)
    num_columns = len(read_f.columns)
    num_rows = len(read_f)
    type_column = read_f.dtypes
    
    salida = (
         f'Todas las filas del xlsx:\n{read_f}\n\n'
         f'Las tres primeras filas del xlsx:\n{tres_filas}\n\n' 
         f'Este es el numero de columnas: {num_columns}\n' 
         f'Este es el numero de filas: {num_rows}\n' 
         'Tipos de datos de las columnas:\n'
         f'{type_column.to_string()}'
    )
    return salida    


def MenuOpciones():
    f = 't23clientes.xlsx'
    read_f = pd.read_excel(f, engine='openpyxl')
    while True:   
        try:
            opciones = int(input('''Escoge entre estas opciones:
            1. – Gráficos para los datos de las mujeres\n
            2. – Gráficos por ciudad\n
            3. – Análisis de compras y compras online del mes\n
            4. - Terminar: '''))

            if opciones == 1:
                GraficosMujeres(read_f)
            elif opciones == 2:
                GraficosCiudad(read_f)
            elif opciones == 3:
                AnalisisCompras(read_f)
            elif opciones == 4:
                print(f'Hasta luego :)')
                break
            else:
                print('Vuelve e ingresa un numero correcto')
                continue
        except ValueError as error:
            print(f'Ingresaste un dato incorrecto: {error}, vuelve a ingresar un dato')
            continue

def GraficosMujeres(dataframe):
    dataframe_mujeres = dataframe[dataframe['sexo'].str.lower() == 'mujer']
    dataframe_compras = dataframe_mujeres[(dataframe_mujeres['compras'] > 0) & (dataframe_mujeres['comprasonline'] > 0)]

    Graficas(dataframe_compras)

def GraficosCiudad(dataframe):
    while True:
        try:
            opciones = int(input('''Escoge entre estas opciones:
            1. – Bogotá\n
            2. – Medellín\n
            3. – Cali\n
            4. – Menu principal: '''))

            if opciones == 1:
                dataframe_ciudad = dataframe[dataframe['ciudad'].str.lower() == 'bogotá']
            elif opciones == 2:
                dataframe_ciudad = dataframe[dataframe['ciudad'].str.lower() == 'medellín']
            elif opciones == 3:
                dataframe_ciudad = dataframe[dataframe['ciudad'].str.lower() == 'cali']
            elif opciones == 4:
                print("Volviendo al menú principal.")
                return
            else:
                print('Ingresa un número correcto')
                continue

            if dataframe_ciudad.empty:
                print(f'No hay datos para la ciudad seleccionada.')
            else:
                dataframe_compras = dataframe_ciudad[(dataframe_ciudad['compras'] > 0) & (dataframe_ciudad['comprasonline'] > 0)]
                
                if not dataframe_compras.empty:
                    Graficas(dataframe_compras)
                else:
                    print(f"No hay datos suficientes para generar gráficas para {dataframe_ciudad['ciudad'].iloc[0]}.")

        except ValueError as error:
            print(f'Ingresaste un dato incorrecto: {error}, vuelve a ingresar un dato')
            continue



def Graficas(dataframe):
    if dataframe.empty: 
        print("El DataFrame está vacío. No se puede graficar.") 
        return 
    estado_civil_counts = dataframe['estcivil'].value_counts(normalize=True) * 100 
    if not estado_civil_counts.empty: 
        estado_civil_counts.plot(kind='bar', color='green') 
        plt.title('Porcentaje de clientes por estado civil') 
        plt.xlabel('Estado civil') 
        plt.ylabel('Porcentaje') 
        plt.xticks(rotation=45) 
        plt.savefig('grafico_estado_civil.png') 
        plt.close() 
    
    sexo_counts = dataframe['sexo'].value_counts(normalize=True) * 100 
    if not sexo_counts.empty: 
        sexo_counts.plot(kind='bar', color='green') 
        plt.title('Porcentaje de clientes por sexo') 
        plt.xlabel('Sexo') 
        plt.ylabel('Porcentaje') 
        plt.xticks(rotation=0) 
        plt.savefig('grafico_estado_sexo.png') 
        plt.close() 
        
    if not dataframe['compras'].empty: 
        dataframe['compras'].plot(kind='hist', bins=10, color='green', edgecolor='black') 
        plt.title('Histograma de Frecuencias absolutas de compras') 
        plt.xlabel('Compras') 
        plt.ylabel('Suma total') 
        plt.xticks(rotation=45)
        plt.savefig('histograma_compras.png') 
        plt.close() 
        
    compras_estado_civil = dataframe.groupby('estcivil')['compras'].sum() 
    if not compras_estado_civil.empty: 
        compras_estado_civil.plot(kind='bar', color='green')
        plt.title('Suma total de compras por estado civil') 
        plt.xlabel('Estado civil') 
        plt.ylabel('Suma total') 
        plt.xticks(rotation=45) 
        plt.savefig('compras_estado_civil.png') 
        plt.close() 
        
    compras_online_sexo = dataframe.groupby('sexo')['comprasonline'].sum() 
    if not compras_online_sexo.empty: 
        compras_online_sexo.plot(kind='bar', color='green') 
        plt.title('Suma total de compras online por sexo') 
        plt.xlabel('Sexo') 
        plt.ylabel('Suma Total de Compras Online') 
        plt.xticks(rotation=0) 
        plt.savefig('compras_online_sexo.png') 
        plt.close() 
        
    if not dataframe[['compras', 'comprasonline']].empty: 
        dataframe.plot(kind='scatter', x='compras', y='comprasonline', color='green')
        plt.title('Scatter por compras y compras online') 
        plt.xlabel('Compras') 
        plt.ylabel('Compras online') 
        plt.savefig('scatter_compras_comprasonline.png') 
        plt.close()


def AnalisisCompras(dataframe):

    visitas_ciudad = dataframe.groupby('ciudad')['visitas_web'].mean()
    print(f'Ciudad con mayor visitas en la web es: {visitas_ciudad.idxmax()}')

    visitas_sexo = dataframe.groupby('sexo')['visitas_web'].mean()
    print(f'Sexo con menor visitas en la web es: {visitas_sexo.idxmin()}')

    compras_ciudad_estado = dataframe.groupby(['ciudad','estcivil'])['compras'].sum()
    compras_ciudad_estado_max = compras_ciudad_estado.groupby('ciudad').idxmax()
    print(f'Este es total de compras por ciudad y estado civil: {compras_ciudad_estado}')
    print(f'Estado civil con mas compras por ciudad: {compras_ciudad_estado_max}')

    compras_online_ciudad_estado = dataframe.groupby(['ciudad', 'estcivil'])['comprasonline'].sum()
    compras_online_ciudad_estado_min = compras_online_ciudad_estado.groupby('ciudad').idxmin()
    print(f'Este es total de compras online por ciudad y estado civil: {compras_ciudad_estado}')
    print(f'Estado civil con menos compras por ciudad: {compras_online_ciudad_estado_min}')

    promedio_ciudad_sexo = dataframe.groupby(['ciudad', 'sexo'])['compras'].mean()
    print(f'Promedio de compras por ciudad y sexo: {promedio_ciudad_sexo}')

    promedio_online_ciudad_sexo = dataframe.groupby(['ciudad', 'sexo'])['comprasonline'].mean()
    print(f'Promedio de compras online por ciudad y sexo: {promedio_online_ciudad_sexo}')

    promedio_visitas_ciudad_sexo = dataframe.groupby(['ciudad', 'sexo'])['visitas_web'].mean()
    promedio_visitas_ciudad_sexo_max = promedio_visitas_ciudad_sexo.groupby('sexo').idxmax()
    print(f'Promedio de visitas en la web por ciudad y sexo: {promedio_visitas_ciudad_sexo}')
    print(f'En esta ciudad se hacen mas visitas en promedio al web por sexo : {promedio_visitas_ciudad_sexo_max}')

    promedio_visitas_ciudad_estcivil = dataframe.groupby(['ciudad', 'estcivil'])['visitas_web'].mean()
    promedio_visitas_ciudad_estcivil_min = promedio_visitas_ciudad_estcivil.groupby('estcivil').idxmin() 
    print(f'Promedio de visitas en la web por ciudad y estado civil: {promedio_visitas_ciudad_estcivil}')
    print(f'Ciudad con menos visitas en promedio al sitio web por estado civil: {promedio_visitas_ciudad_estcivil_min}')


if __name__ == "__main__":
    dataframe = read_review_dates()
    MenuOpciones()



