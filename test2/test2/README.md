# Analiza activității firmelor – 2014

## Obiectiv
Prelucrarea informațiilor economice la nivel de localitate și agregarea indicatorilor la nivel de județ folosind Python și Pandas.

## Fișiere
- `data_in/I2014.csv`: Siruta, DenLocalitate, NrFirme, NrSal, TotalCifraAfaceri, TotalProfit, TotalPierdere.
- `data_in/PopulatieLocalitati.csv`: Siruta, Localitate, Judet, Populatie.
- `.env`: căile fișierelor de intrare și ale rezultatelor.
- `main.py`: citirea și asocierea datelor, cerințele de prelucrare.
- `data_out/`: directorul fișierelor CSV rezultate.

## Pornire
1. Deschideți folderul proiectului în PyCharm sau într-un editor Python.
2. Instalați dependențele: `python -m pip install -r requirements.txt`.
3. Rulați `python main.py`.
4. Completați secțiunile `TODO 1`–`TODO 4` și rulați din nou.
5. Verificați fișierele generate în `data_out/`.

## Cerințe și barem

### 1. Raportul cifră de afaceri / salariați – 2 puncte
Salvați în `Output1.csv` localitățile care au salariați, în ordinea descrescătoare a raportului `TotalCifraAfaceri / NrSal`. Coloane: `Siruta`, `DenLocalitate`, `Raport CA/NrSal`.

### 2. Rata ocupării pe județe – 2 puncte
Salvați în `Output2.csv` rata ocupării, calculată ca număr de salariați la 1000 de locuitori, în ordinea descrescătoare a ratei. Coloane: `Judet`, `Rata Ocuparii`.

### 3. Profitul maxim pe locuitor – 2 puncte
Identificați pentru fiecare județ localitatea cu cel mai mare raport `TotalProfit / Populatie`. Salvați în `Output3.csv` coloanele `Judet`, `Localitate`.

### 4. Medii ponderate pe județe – 3 puncte
Calculați pentru fiecare județ media ponderată cu populația localităților pentru indicatorii `NrFirme`, `NrSal`, `TotalCifraAfaceri`, `TotalProfit`, `TotalPierdere`. Salvați în `Output4.csv` coloana `Judet` și cele cinci medii.

**1 punct din oficiu.**

## Recomandări
- `Siruta` este un identificator, nu o variabilă numerică pentru agregare.
- Evitați împărțirea la zero.
- La cerința 2, agregați salariații și populația înainte de calcularea ratei.
- La cerința 4, media este ponderată cu populația, nu media aritmetică simplă.
- Salvați fișierele CSV cu `index=False`.

## Rezultate
`data_out/Output1.csv`, `data_out/Output2.csv`, `data_out/Output3.csv`, `data_out/Output4.csv`.
