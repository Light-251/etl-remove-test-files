import os

# Percorso della cartella da cui vuoi ottenere i nomi dei file
directory_path = r'/path/to/your/folder'

# Nome del file di output dove verranno salvati i nomi dei file
output_file = 'file_list.txt'

# Ottieni i nomi dei file nella cartella
file_names = os.listdir(directory_path)

# Filtro per includere solo i file (esclude le directory)
file_names = [f for f in file_names if os.path.isfile(os.path.join(directory_path, f))]

# Salva i nomi dei file nel file di output
with open(output_file, 'w') as f:
    for file_name in file_names:
        f.write(file_name + '\n')

print(f"I nomi dei file sono stati salvati in {output_file}.")
