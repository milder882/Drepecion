import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("train.csv")

# Llenar los valores faltantes en las columnas numéricas con la mediana de las columnas correspondientes
df = df.fillna(df.median(numeric_only=True))

# Para las columnas categóricas, llenamos los valores faltantes con la moda (el valor más común)
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Histograma de la duración del sueño en relación con la depresión
plt.figure(figsize=(10, 6))
plt.title("Distribución de la duración del sueño según la depresión")
sns.histplot(data=df, x="Sleep Duration", hue="Depression", kde=True, bins=20)
plt.xlabel("Horas de sueño")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de la satisfacción laboral según la depresión
plt.figure(figsize=(10, 6))
plt.title("Distribución de la satisfacción laboral según la depresión")
sns.histplot(data=df, x="Job Satisfaction", hue="Depression", kde=True, bins=20)
plt.xlabel("Satisfacción laboral")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de barras de la presión académica en relación con la depresión
plt.figure(figsize=(10, 6))
plt.title("Presión académica en relación con la depresión")
sns.barplot(data=df, x="Depression", y="Academic Pressure", ci=None, palette="coolwarm")
plt.xlabel("Depresión")
plt.ylabel("Nivel de presión académica")
plt.show()

# Gráfico de barras para antecedentes familiares de enfermedad mental
plt.figure(figsize=(10, 6))
plt.title("Relación entre antecedentes familiares y depresión")
sns.countplot(data=df, x="Family History of Mental Illness", hue="Depression", palette="Set2")
plt.xlabel("Historia familiar de enfermedad mental")
plt.ylabel("Frecuencia")
plt.show()

# Histograma de pensamientos suicidas según la depresión

plt.figure(figsize=(10, 6))
plt.title("Distribución de pensamientos suicidas según la depresión")
sns.countplot(data=df, x="Have you ever had suicidal thoughts ?", hue="Depression", palette="pastel")
plt.xlabel("Pensamientos suicidas")
plt.ylabel("Frecuencia")
plt.show()

# Relación entre el estrés financiero y la depresión
plt.figure(figsize=(10, 6))
plt.title("Estrés financiero en relación con la depresión")
sns.barplot(data=df, x="Depression", y="Financial Stress", ci=None, palette="viridis")
plt.xlabel("Depresión")
plt.ylabel("Nivel de estrés financiero")
plt.show()
