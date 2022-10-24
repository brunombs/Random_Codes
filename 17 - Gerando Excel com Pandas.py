import pandas as pd

carros = {
    'marca': ['Nissan', 'Audi'],
    'modelo': ['Frontier', 'Q3'],
    'ano': ['2022', '2021']
}

dataframe = pd.DataFrame(carros)
dataframe.to_excel('./carros.xlsx')