"""Analiza activității firmelor în anul 2014 – varianta 2 (Pandas).

Completați secțiunile TODO. Fiecare cerință se salvează într-un CSV separat.
Date de intrare: data_in/I2014.csv și data_in/PopulatieLocalitati.csv.
"""

from pathlib import Path
import pandas as pd


DATA_IN = Path("data_in")
DATA_OUT = Path("data_out")
DATA_OUT.mkdir(parents=True, exist_ok=True)

firme = pd.read_csv(DATA_IN / "I2014.csv")
populatie = pd.read_csv(DATA_IN / "PopulatieLocalitati.csv")

# Asocierea se face prin codul Siruta, nu prin numele localității.
date = firme.merge(populatie[["Siruta", "Judet", "Populatie"]], on="Siruta", how="inner")


# CERINȚA 1 (1,5 puncte) – Output1.csv
# Calculați PROFITUL MEDIU PE FIRMĂ pentru fiecare localitate cu NrFirme > 0.
# Formula: TotalProfit / NrFirme.
# Coloane: Siruta, DenLocalitate, ProfitPeFirma.
# Ordonați descrescător după ProfitPeFirma.
# Indicii: .loc[], .copy(), /, .sort_values(), .to_csv(index=False).
# TODO 1: calculați indicatorul și salvați Output1.csv.


prob1 = firme[firme["NrFirme"]> 0].copy()
prob1.loc[:, "ProfitPeFirma"] = prob1["TotalProfit"] / prob1["NrFirme"]
prob1 = prob1[["Siruta","DenLocalitate","ProfitPeFirma"]]
prob1 = prob1.sort_values( by = "ProfitPeFirma" , ascending=False)
prob1.to_csv(DATA_OUT / "Output1.csv", index=False)

# CERINȚA 2 (1,5 puncte) – Output2.csv
# Calculați NUMĂRUL DE FIRME LA 1000 DE LOCUITORI pentru fiecare județ.
# Formula: (suma NrFirme / suma Populatie) * 1000.
# Luați în calcul numai localitățile cu Populatie > 0.
# Coloane: Judet, FirmeLa1000Locuitori.
# Ordonați descrescător după FirmeLa1000Locuitori.
# Indicii: .loc[], .groupby("Judet"), .sum(), .sort_values().
# Atenție: întâi însumați valorile pe județ, apoi calculați raportul.
# TODO 2: calculați indicatorul și salvați Output2.csv.

dateF = pd.merge(firme,populatie,on="Siruta")
prob2 = dateF[dateF["Populatie"]>0].copy()
prob2.groupby("Judet")[["NrFirme","Populatie"]].sum()
prob2.loc[:,"FirmeLa1000Locuitori"]= (prob2["NrFirme"]/prob2["Populatie"])*1000
prob2 = prob2[["Judet","FirmeLa1000Locuitori"]]
prob2 = prob2.sort_values(by="FirmeLa1000Locuitori", ascending=False)
prob2.to_csv(DATA_OUT / "Output2.csv", index=False)

# CERINȚA 3 (1,5 puncte) – Output3.csv
# Identificați, în fiecare județ, localitatea cu CEA MAI MARE CIFRĂ DE AFACERI.
# Coloane: Judet, DenLocalitate, TotalCifraAfaceri.
# Ordonați rezultatul alfabetic după Judet.
# În caz de egalitate, alegeți localitatea cu numele alfabetic mai mic.
# Indicii: .sort_values(), .drop_duplicates("Judet"), .to_csv().
# TODO 3: selectați localitatea câștigătoare și salvați Output3.csv.

prob3 = dateF.sort_values(
    by=["Judet", "TotalCifraAfaceri", "DenLocalitate"],
    ascending=[True, False, True]
).drop_duplicates("Judet")
prob3 = prob3[["Judet", "DenLocalitate", "TotalCifraAfaceri"]]
prob3.to_csv(DATA_OUT / "Output3.csv", index=False)


# CERINȚA 4 (1,5 puncte) – Output4.csv
# Calculați pentru fiecare județ PROFITUL NET AGREGAT:
# ProfitNet = suma TotalProfit - suma TotalPierdere.
# Coloane: Judet, ProfitNet.
# Ordonați descrescător după ProfitNet.
# Indicii: .groupby("Judet"), .sum(), scădere, .sort_values().
# TODO 4: calculați ProfitNet și salvați Output4.csv.

prob4 = dateF.copy()
prob4 = dateF.groupby("Judet")[["TotalProfit", "TotalPierdere"]].sum()
prob4["ProfitNet"] = prob4["TotalProfit"] - prob4["TotalPierdere"]
prob4 = prob4[["ProfitNet"]]
prob4 = prob4.sort_values(by="ProfitNet", ascending=False)
prob4.to_csv(DATA_OUT / "Output4.csv")


# CERINȚA 5 (1,5 puncte) – Output5.csv
# Calculați NUMĂRUL MEDIU DE SALARIAȚI PE FIRMĂ pentru fiecare județ.
# Formula: suma NrSal / suma NrFirme.
# Excludeți județele pentru care suma NrFirme este 0.
# Coloane: Judet, SalariatiPeFirma.
# Ordonați descrescător după SalariatiPeFirma.
# Indicii: .groupby("Judet"), .sum(), filtrare, /, .sort_values().
# Atenție: nu calculați media simplă a rapoartelor pe localități.
# TODO 5: calculați indicatorul și salvați Output5.csv.

prob5 = dateF[dateF["NrFirme"]>0].copy()
prob5 = prob5.groupby("Judet")[["NrFirme","NrSal"]].sum()
prob5["SalariatiPeFirma"] = prob5["NrSal"]/prob5["NrFirme"]
prob5 = prob5[["SalariatiPeFirma"]]
prob5 = prob5.sort_values(by="SalariatiPeFirma", ascending=False)
prob5.to_csv(DATA_OUT / "Output5.csv")


# CERINȚA 6 (1,5 puncte) – Output6.csv
# Selectați PRIMELE 10 LOCALITĂȚI cu cea mai mare MARJĂ A PROFITULUI.
# Formula: MarjaProfit = (TotalProfit / TotalCifraAfaceri) * 100.
# Includeți doar localitățile cu TotalCifraAfaceri > 0.
# Coloane: Siruta, DenLocalitate, Judet, MarjaProfit.
# Ordonați descrescător după MarjaProfit și păstrați primele 10 rânduri.
# Indicii: .loc[], .copy(), /, .sort_values(), .head(10).
# TODO 6: calculați marja, selectați primele 10 și salvați Output6.csv.

prob6 = dateF[dateF["TotalCifraAfaceri"]>0].copy()
prob6["MarjaProfit"] = (prob6["TotalProfit"] / prob6["TotalCifraAfaceri"]) * 100
prob6 = prob6[["Siruta", "DenLocalitate", "Judet","MarjaProfit"]]
prob6 = prob6.sort_values(by="MarjaProfit", ascending=False)
prob6 = prob6.head(10)
prob6.to_csv(DATA_OUT / "Output6.csv", index=False)


prob7 = dateF.sort_values(
    by=["TotalCifraAfaceri"],
    ascending=[False])
prob7 = prob7.head(1)
prob7.to_csv(DATA_OUT / "Output7.csv")
# 1 punct din oficiu. TOTAL: 10 puncte.
# Pentru fiecare fișier CSV utilizați index=False.
