import glob
import os

from send2trash import \
    send2trash  # Importa send2trash per spostare i file nel cestino


def rimuovi_file(cartelle, estensioni):
    for cartella in cartelle:
        for estensione in estensioni:
            # Costruisce il percorso del pattern da cercare per ciascuna estensione
            pattern = os.path.join(cartella, f'*.{estensione}')
            
            # Trova i file corrispondenti al pattern
            file_da_rimuovere = glob.glob(pattern)
            
            # Elimina i file trovati spostandoli nel cestino
            for file in file_da_rimuovere:
                try:
                    send2trash(file)  # Usa send2trash per spostare i file nel cestino
                    print(f'File spostato nel cestino: {file}')
                except Exception as e:
                    print(f'Errore durante lo spostamento del file {file} nel cestino: {e}')

if __name__ == "__main__":
    # Specifica la cartella e le estensioni dei file da rimuovere
    cartella_da_cercare = [
        r"C:\Progetti\ETL_REFACTOR\etl\workflow\processed",
        r"C:\Progetti\ETL_REFACTOR\etl\workflow\failed",
        r"C:\Progetti\ETL_REFACTOR\etl\workflow\input\sources"
        ]
    estensioni_file = ["xml"]  # Elenca le estensioni che vuoi rimuovere 
    
    rimuovi_file(cartella_da_cercare, estensioni_file) # Rimuove xml da: processed, failed, sources
    
    cartella_da_cercare = [
        r"C:\Progetti\ETL_REFACTOR\etl\workflow\out"
    ]
    estensioni_file = [
        "ok",
        "tar"
        ]
    
    rimuovi_file(cartella_da_cercare, estensioni_file) # Rimuove ok, tar da: out
    
    cartella_da_cercare = [
         r"C:\Progetti\ETL_REFACTOR\etl\workflow\input"
    ]
    
    estensioni_file = [
        "ok"
    ]
    
    # rimuovi_file(cartella_da_cercare, estensioni_file)
    