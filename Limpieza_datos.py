import os
import pandas as pd

# Carpeta donde tienes los archivos
carpeta = "Docs"

# Lista para guardar los DataFrames
dataframes = []

columnas_deseadas = [
    "INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)",
    "PROGRAMA ACADÉMICO",
    "GÉNERO",
    "AÑO",
    "SEMESTRE",
    "INSCRITOS"
]



# Recorremos todos los archivos en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".xlsx"):
        ruta = os.path.join(carpeta, archivo)
        print(f"Leyendo: {ruta}")
        df = pd.read_excel(ruta)  # Lee cada archivo

        df.columns = df.columns.str.upper()

        columnas_existentes = [col for col in columnas_deseadas if col in df.columns]
        df_filt_cols = df[columnas_existentes]

        dataframes.append(df_filt_cols)

# Unificamos todos los DataFrames
df_final = pd.concat(dataframes, ignore_index=True)

print(df_final)

print(len(df_final))



#######FILTRAR COLUMNAS


# Renombrar columnas
df_final.rename(columns={
    "INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)": "INSTITUCION",
    "PROGRAMA ACADÉMICO": "PROGRAMA",
    "GÉNERO": "GENERO",
    "AÑO": "ANIO",
    "SEMESTRE": "SEMESTRE",
    "INSCRITOS": "TOTAL_INSCRITOS"
}, inplace=True)


print(df_final)


#Sumar los generos
df_agrupado = df_final.groupby(['INSTITUCION', 'PROGRAMA', 'ANIO', 'SEMESTRE'])['TOTAL_INSCRITOS'].sum().reset_index()


#####FILTRAR INSTITUCION

# Definimos una lista con las universidades que queremos filtrar
universidades_filtradas = ["UNIVERSIDAD DE ANTIOQUIA", "CORPORACION UNIVERSITARIA LASALLISTA"]

# Filtramos el DataFrame usando .isin()
df_final_F = df_agrupado.loc[
    df_agrupado["INSTITUCION"].isin(universidades_filtradas)
]


##CORPORACION UNIVERSITARIA LASALLISTA

print(df_final_F)

# Guardamos el archivo unificado
df_final_F.to_excel("unificado.xlsx", index=False)

#df_agrupado.to_excel("unificado.xlsx", index=False)


print("✅ Archivos unificados en 'unificado.xlsx'")






