import csv
import os

def filter_columns():
    users = ["Alejandra", "Carlos", "Juan"]
    # Nota: la columna original está en minúscula ('body'), así que la capturamos así. Lo mismo para ID, Title, etc.
    desired_columns = ["ID", "Title", "body", "ux_smell", "reasoning"]
    
    for user in users:
        filename = f"issues_sample_{user}.csv"
        
        if not os.path.exists(filename):
            print(f"Advertencia: No se encontró el archivo {filename}, omitiendo...")
            continue
            
        print(f"Filtrando columnas para {filename}...")
        
        # Leer los datos originales
        rows_to_keep = []
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Verificamos si las columnas existen en el archivo original
            actual_columns = []
            for col in desired_columns:
                if col in reader.fieldnames:
                    actual_columns.append(col)
                elif col == "Body" and "body" in reader.fieldnames:
                    actual_columns.append("body") # Handle case mismatch
                    
            for row in reader:
                filtered_row = {col: row[col] for col in actual_columns}
                rows_to_keep.append(filtered_row)
                
        # Sobrescribir el archivo con solo las columnas específicas
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=actual_columns)
            writer.writeheader()
            writer.writerows(rows_to_keep)
            
        print(f"¡{filename} actualizado con éxito! Columnas actuales: {actual_columns}")

if __name__ == "__main__":
    filter_columns()
