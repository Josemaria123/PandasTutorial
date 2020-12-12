import pandas as pd

#Load the Data
df = pd.read_csv("Pokemon.csv")
print(df.head())

#Reading the Headers

print(df.columns)

#Read a specific column
print(df.Name)
print(df[["Name", "Type 1", "Attack"]])


#Read a specific row

print(df.iloc[2]) #iloc = integer location (Row index)

#Read multiple rows

print(df[["Name", "Type 1", "Attack"]].iloc[1:4])

#Read a specific location

print(df.iloc[2,1]) #df.iloc[Row, Column]

#iterate through each row

for index, row in df.iterrows():
    print(index, row)


#iterate through a specific column and obtain those values

for index, row in df.iterrows():  #we will get al the names of the Name Column
    print(index, row["Name"])

#Filter by Type 1 pokemon == Fire use the df.loc method

print(df["Name"].loc[df["Type 1"] == "Fire"]) #Filtra los nombre de los pokemones tipo fuego y los imprime

#Describe method returns the basic stats of my dataframe

print(df["Attack"].loc[df["Type 1"] == "Fire"].describe()) #Retorna las stats de ataque de todos los pokemones tipo Fuego
print(df["Attack"].loc[df["Type 1"] == "Grass"].describe())


#Sorting Data

print(df.sort_values("Name", ascending=False)) #Sortea los datos por nombre en orden alfabetico y ascending = false en orden descendente

#Changing the data

print(df.columns)
df['Total'] = df['Speed'] + df['Attack'] #Creo una nueva columna en mis datos
print(df['Total'].head(5))


#Remove a specific column

df = df.drop(columns=['Total']) #importante poner el df al frente porque queda guardado en memoria igual
print(df.columns)
print(df.head(5))

#Otra forma de agregar una columna nueva mas rapido

df['Total'] = df.iloc[:, 4:10].sum(axis = 1) #Suma los valores de las columnas 4 a 9 de todas las filas y el axis = 1 es horizontal, axis = 0 es vertical
print(df[['Name', 'Total']].head(5))

#Saving Data and exporting in a desired format

df.to_csv('modified.csv', index=False)
df.to_excel('modifiedExcel.xlsx', index=False) #Save data to excel

#Filtering Data

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')] #Puedo aplicar todos los filtros que quiera.

new_df = new_df.reset_index(drop=True) #Resetea los index de mi nuevo dataframe

new_df = df.loc[df['Name'].str.contains('Mega')] #Filtra por palabras

new_df = df.loc[~df['Name'].str.contains('Mega')] #Filtra todos los que tienen Mega con ~ que es negacion y los imprime


# Import re es para regex, me sirve para encontrar palabras o valores dentro de mis datos

 # Conditional Changes

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' #Modifico la palabra Fire por Flamer. Si type 1 = Fire, entonces esos Type 1 = Flamer
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE' #Puedo modificar varias columnas si quiero

#Agreggate Statitics (GrouBy)

df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) #MEDIA POR TIPO DE POKEMON

df['Count'] = 1
df = df.groupby(['Type 1']).count()['Count'] #Saca la cuenta de cuantos pokemones hay segun su tipo 1

#Chunksize

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('modified.csv', chunksize=5): #Si trabajo con datos que pesan teras entonces chunksize limita lo que proceso cada 5 filas, cada fila es como 10 o 20 bytes
    print("CHUNK DF")
    print(df)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df, results])  #Concatena 2 dataframes, el new_df y los results
    print(new_df)