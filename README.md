## Descrizione del Funzionamento

Il programma `ETL Remove Test Files` è uno script Python progettato per rimuovere file con estensioni specifiche da una cartella data. I file vengono spostati nel cestino invece di essere eliminati definitivamente.

### Come Funziona:

1. **Configura il Percorso e le Estensioni:**
   Modifica il file `rimuovi_file.py` per impostare il percorso della cartella da cui vuoi rimuovere i file e le estensioni dei file da eliminare. Ad esempio:
   
   ```python
   cartella_da_cercare = r"C:\path\to\your\folder"
   estensioni_file = ["txt", "log", "csv"]
2. Esecuzione dello Script:
Esegui il comando python rimuovi_file.py per avviare il processo. Lo script cercherà tutti i file con le estensioni specificate nella cartella indicata e li sposterà nel cestino.
Esempio:
Se hai impostato cartella_da_cercare su C:\Users\tuo_nome\Desktop\prova e estensioni_file su ["txt", "log"], eseguendo lo script verranno spostati nel cestino tutti i file con estensione .txt e .log presenti in quella cartella.

Questo approccio ti consente di gestire facilmente e in modo sicuro i file di test o temporanei senza eliminarli definitivamente.

### Descrizione del Funzionamento:
- **Configura il Percorso e le Estensioni**: Personalizza il percorso della cartella e le estensioni dei file nel file `rimuovi_file.py`.
- **Esecuzione dello Script**: Avvia lo script con `python rimuovi_file.py` per spostare i file specificati nel cestino.

Questa sezione fornisce una panoramica concisa di come configurare ed eseguire il programma, rendendo più semplice il processo di utilizzo e comprensione.
