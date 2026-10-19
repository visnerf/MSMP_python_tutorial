"""
LEKCE 1 - SAMOSTATNÁ CVIČENÍ A ÚKOLY
Doplňte kód pod příslušná zadání.
"""
# %% Úkol 1: Proměnné a datové typy
"""
ÚKOL 1: Proměnné a datové typy
Zadání:
Nadefinujte proměnné pro moderní tříválcový motor 1.0 TSI.
1. Vytvořte proměnnou pro název motoru.
2. Vytvořte proměnnou pro počet válců (3).
3. Vytvořte proměnné pro vrtání (74.5 mm) a zdvih (76.4 mm).
4. Pomocí funkce type() si vypište na obrazovku a ověřte, že počet válců 
   je celočíselný typ (int) a vrtání je desetinné číslo (float).
"""
# Sem napište kód pro Úkol 1:
engineName = "1.0 TSI"
cylinders = 3
bore = 74.5  # in mm
stroke = 76.4  # in mm  
print(type(cylinders))  # Should print <class 'int'>
print(type(bore))  # Should print <class 'float'>



# %% Úkol 2: Matematika a vzorce
"""
ÚKOL 2: Matematika a vzorce
Zadání:
Máme zadaný kompresní objem jednoho válce V_c = 0.000045 m3.
1. Vypočítejte zdvihový objem jednoho válce V_z v m3 (použijte vrtání a zdvih z Úkolu 1).
   Nezapomeňte milimetry nejprve převést na metry. Zadejte 'import math' pro číslo pí.
2. Vypočítejte kompresní poměr epsilon. Vzorec: epsilon = (V_z + V_c) / V_c
3. Vypočítejte střední pístovou rychlost c_s [m/s] při otáčkách n = 4000 min-1.
   Vzorec: c_s = 2 * z * (n / 60), kde z je zdvih v metrech.
"""

import math
V_c = 0.000045
n_otacky = 4000
# Sem napište kód pro Úkol 2:
V_c = 0.000045  # kompresní objem jednoho válce v m3
V_z = math.pi * (bore / 1000 / 2) ** 2 * (stroke / 1000)  # zdvihový objem jednoho válce v m3
epsilon = (V_z + V_c) / V_c  # kompresní poměr
c_s = 2 * (stroke / 1000) * (n_otacky / 60)  # střední pístová rychlost v m/s






"""
ÚKOL 3: Formátovaný výstup (F-stringy)
Zadání:
Vypište na obrazovku hezky zformátovanou větu, která bude obsahovat 
vypočtený kompresní poměr (zaokrouhlený na 1 desetinné místo) a 
střední pístovou rychlost (zaokrouhlenou na 2 desetinná místa) z Úkolu 2.
"""
# Sem napište kód pro Úkol 3:
textik = f"Zdvihový objem jednoho válce V_z: {V_z:.6f} m3, Kompresní poměr epsilon: {epsilon:.1f}, Střední pístová rychlost c_s: {c_s:.2f} m/s"
print(textik)




"""
ZÁVĚREČNÝ ÚKOL: Termodynamický oběh (Sabatheho/Dual cycle)
Zadání:
Sabatheho oběh kombinuje izochorický i izobarický přívod tepla.
Vaším úkolem je dopočítat stavové veličiny (tlak p, teplotu T, objem v) pro body 1 až 5.

- Bod 1: Sání (výpočet 'v1' ze stavové rovnice)
- Bod 2: Izoentropická komprese (v2 = v1/eps, p2 = p1*eps^kappa, T2 = T1*eps^(kappa-1))
- Bod 3: Izochorický přívod tepla (v3 = v2, p3 = p2*alpha, T3 = T2*alpha)
- Bod 4: Izobarický přívod tepla (p4 = p3, v4 = v3*beta, T4 = T3*beta)
- Bod 5: Izoentropická expanze (v5 = v1, p5 = p4*(v4/v5)^kappa, T5 = T4*(v4/v5)^(kappa-1))

U každého bodu vypište jeho stavové veličiny pomocí print() a f-stringu!
"""
# Zadané konstanty
r = 287.15        # Plynová konstanta vzduchu [J/(kg.K)]
kappa = 1.4       # Poissonova konstanta [-]
p1 = 100000       # Počáteční tlak [Pa]
T1 = 293.15       # Počáteční teplota [K]

# Termodynamické parametry Sabatheho oběhu
epsilon = 16.5    # Kompresní poměr (v1 / v2)
alpha = 1.6       # Stupeň zvýšení tlaku (p3 / p2)
beta = 1.4        # Stupeň předběžné expanze (v4 / v3)

# ZDE ZAČNĚTE POČÍTAT:

# Bod 1:
v1 = r * T1 / p1  # Stavová rovnice: v = R*T/p  

# Bod 2:
v2 = v1 / epsilon
p2 = p1 * epsilon ** kappa
T2 = T1 * epsilon ** (kappa - 1)


# Bod 3:
v3 = v2
p3 = p2 * alpha
T3 = T2 * alpha

# Bod 4:
v4 = v3 * beta
p4 = p3
T4 = T3 * beta



# Bod 5:
v5 = v1
p5 = p4 * (v4 / v5) ** kappa
T5 = T4 * (v4 / v5) ** (kappa - 1)

print(f"Bod 1: p1 = {p1:.2f} Pa, T1 = {T1:.2f} K, v1 = {v1:.6f} m3")
print(f"Bod 2: p2 = {p2:.2f} Pa, T2 = {T2:.2f} K, v2 = {v2:.6f} m3")
print(f"Bod 3: p3 = {p3:.2f} Pa, T3 = {T3:.2f} K, v3 = {v3:.6f} m3")
print(f"Bod 4: p4 = {p4:.2f} Pa, T4 = {T4:.2f} K, v4 = {v4:.6f} m3")
print(f"Bod 5: p5 = {p5:.2f} Pa, T5 = {T5:.2f} K, v5 = {v5:.6f} m3")

# Graf p-v diagramu Sabatheho oběhu
import matplotlib.pyplot as plt

pocet_kroku = 100

# 1 -> 2: izoentropická komprese, p * v**kappa = konst.
v_komprese = [
    v1 + (v2 - v1) * i / pocet_kroku
    for i in range(pocet_kroku + 1)
]
p_komprese = [p1 * (v1 / v) ** kappa for v in v_komprese]

# 2 -> 3: izochorický přívod tepla.
# 3 -> 4: izobarický přívod tepla.
# 4 -> 5: izoentropická expanze, p * v**kappa = konst.
v_expanzni = [
    v4 + (v5 - v4) * i / pocet_kroku
    for i in range(pocet_kroku + 1)
]
p_expanzni = [p4 * (v4 / v) ** kappa for v in v_expanzni]

tlak_kpa = 1000
fig, ax = plt.subplots()
ax.plot(v_komprese, [p / tlak_kpa for p in p_komprese], color="tab:red",
        label="1–2: izoentropická komprese")
ax.plot([v2, v3], [p2 / tlak_kpa, p3 / tlak_kpa], color="tab:orange",
        label="2–3: izochorický přívod tepla")
ax.plot([v3, v4], [p3 / tlak_kpa, p4 / tlak_kpa], color="tab:green",
        label="3–4: izobarický přívod tepla")
ax.plot(v_expanzni, [p / tlak_kpa for p in p_expanzni], color="tab:blue",
        label="4–5: izoentropická expanze")
ax.plot([v5, v1], [p5 / tlak_kpa, p1 / tlak_kpa], color="tab:purple",
        label="5–1: izochorický odvod tepla")

# Práce je plocha pod křivkou v p-v diagramu; p*v má jednotku J/kg.
ax.fill_between(v_komprese, [p / tlak_kpa for p in p_komprese], 0,
                color="tab:red", alpha=0.12, label="Práce dodaná při kompresi")
ax.fill_between([v3, v4], [p3 / tlak_kpa, p4 / tlak_kpa], 0,
                color="tab:blue", alpha=0.12, label="Práce odvedená při expanzi")
ax.fill_between(v_expanzni, [p / tlak_kpa for p in p_expanzni], 0,
                color="tab:blue", alpha=0.12)

objemy_bodu = [v1, v2, v3, v4, v5]
tlaky_bodu = [p1, p2, p3, p4, p5]
ax.scatter(objemy_bodu, [p / tlak_kpa for p in tlaky_bodu],
           color="black", zorder=3)
for cislo_bodu, (objem, tlak) in enumerate(zip(objemy_bodu, tlaky_bodu), start=1):
    ax.annotate(str(cislo_bodu), (objem, tlak / tlak_kpa),
                xytext=(5, 5), textcoords="offset points")

w_komprese = (p2 * v2 - p1 * v1) / (1 - kappa)
w_izobara = p3 * (v4 - v3)
w_expanzni = (p5 * v5 - p4 * v4) / (1 - kappa)
w_odvedena = w_izobara + w_expanzni
w_celkova = w_odvedena - abs(w_komprese)
ax.text(
    0.02, 0.98,
    f"Dodaná práce při kompresi: {abs(w_komprese) / 1e3:.1f} kJ/kg\n"
    f"Odvedená práce při expanzi: {w_odvedena / 1e3:.1f} kJ/kg\n"
    f"Výsledná práce oběhu: {w_celkova / 1e3:.1f} kJ/kg",
    transform=ax.transAxes, va="top",
    bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "gray"},
)
print(f"Práce dodaná při kompresi: {abs(w_komprese) / 1e3:.2f} kJ/kg")
print(f"Práce odvedená při expanzi: {w_odvedena / 1e3:.2f} kJ/kg")
print(f"Výsledná práce oběhu: {w_celkova / 1e3:.2f} kJ/kg")

ax.set_title("Sabatheho oběh v p-v diagramu")
ax.set_xlabel("Měrný objem v [m³/kg]")
ax.set_ylabel("Tlak p [kPa]")
ax.grid(True)
ax.legend(fontsize="small")
fig.tight_layout()
plt.show()
