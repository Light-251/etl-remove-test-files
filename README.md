# ETL Remove Test Files

Questo progetto Python fornisce uno script per rimuovere file con estensioni specificate da una determinata cartella. I file vengono spostati nel cestino anziché eliminati permanentemente.

## Prerequisiti

- Python 3.x
- `send2trash` per spostare i file nel cestino.

### Installazione delle dipendenze

Assicurati di avere Python installato e attiva l'ambiente virtuale. Poi installa `send2trash` eseguendo il seguente comando:

```bash
pip install send2trash

Utilizzo
Clona la repository e naviga nella cartella del progetto:


git clone <url-repository>
cd etl-remove-test-files
Crea e attiva un ambiente virtuale (opzionale ma raccomandato):

python -m venv venv
source venv/bin/activate  # Su macOS/Linux
.\venv\Scripts\activate  # Su Windows
Installa le dipendenze:

pip install -r requirements.txt
Modifica il percorso della cartella e le estensioni dei file nel file main.py:

cartella_da_cercare = r"C:\path\to\your\folder"
estensioni_file = ["txt", "log", "csv"]  # Elenca le estensioni che vuoi rimuovere
Esegui lo script:

python main.py
Questo sposterà i file con le estensioni specificate nel cestino.