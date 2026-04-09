import csv
import random
import os

def distribute_issues():
    input_file = 'issues_only_predicted.csv'
    
    # Clasificaciones que NO se consideran un smell de UX
    NON_SMELLS = {"Bug", "No UX", "Feature request"}
    
    smells_list = []
    non_smells_list = []
    
    print("Leyendo el archivo de clasificación...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                ux_smell = row.get('ux_smell', '').strip()
                if not ux_smell:
                    continue
                if ux_smell in NON_SMELLS:
                    non_smells_list.append(row)
                else:
                    smells_list.append(row)
    except FileNotFoundError:
        print(f"Error: {input_file} no encontrado en el directorio actual.")
        return

    print(f"Total de 'smells' encontrados: {len(smells_list)}")
    print(f"Total de 'no smells' encontrados: {len(non_smells_list)}")

    # Mezclar aleatoriamente pero usar semilla para que sea reproducible la misma selección si se vuelve a correr
    random.seed(42)  
    random.shuffle(smells_list)
    random.shuffle(non_smells_list)
    
    # Validar que tengamos la cantidad necesaria
    if len(smells_list) < 3 * 64:
        print(f"Advertencia: No hay suficientes smells para repartir (hay {len(smells_list)}, se necesitan {3*64}).")
    if len(non_smells_list) < 3 * 63:
        print(f"Advertencia: No hay suficientes no-smells para repartir (hay {len(non_smells_list)}, se necesitan {3*63}).")

    users = ["Alejandra", "Carlos", "Juan"]
    smells_per_user = 64
    non_smells_per_user = 63
    
    print("\nComenzando la separación de los datos para el equipo...")
    for i, user in enumerate(users):
        # Seleccionar las muestras exclusivas para cada usuario
        user_smells = smells_list[i * smells_per_user : (i + 1) * smells_per_user]
        user_non_smells = non_smells_list[i * non_smells_per_user : (i + 1) * non_smells_per_user]
        
        user_data = user_smells + user_non_smells
        
        # Mezclar el data set del usuario para que le toquen mezclados los de grupo smell o non-smell
        random.shuffle(user_data)
        
        output_path = f"issues_sample_{user}.csv"
        print(f"Guardando {len(user_data)} registros ({len(user_smells)} smells, {len(user_non_smells)} no-smells) para {user} en -> {output_path}")
        
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(user_data)
            
    print("\n¡Desglose completado con éxito!")

if __name__ == "__main__":
    distribute_issues()
