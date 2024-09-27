import pandas as pd

# Load the CSV file
df = pd.read_csv('naturezas.csv', delimiter=';', encoding='windows-1252')

# Remove rows where 'descricao' contains 'FÁCIL' or 'FACIL'
df_cleaned = df[~df['natureza'].str.contains(';;', case=False)]

# Save the cleaned DataFrame back to a new CSV file
df_cleaned.to_csv('arquivo_limpo2.csv', index=False)
