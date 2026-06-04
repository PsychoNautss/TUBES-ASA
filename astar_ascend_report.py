import time

# Graf berbobot (Map Ascend - Valorant)
graf = {
    'T Spawn':       {'A Lobby': 4, 'Mid Courtyard': 5, 'B Lobby': 6},
    'A Lobby':       {'A Main': 4},
    'A Main':        {'A Site': 3},
    'A Site':        {'A Link': 3},
    'A Link':        {'B Link': 6},
    'Mid Courtyard': {'Mid Catwalk': 3, 'Market': 4},
    'Mid Catwalk':   {'A Site': 4},
    'Market':        {'B Link': 3},
    'B Lobby':       {'B Main': 4},
    'B Main':        {'B Site': 3},
    'B Link':        {'B Site': 2},
    'B Site':        {}
}

heuristik = {
    'T Spawn': 10,
    'A Lobby': 9,
    'A Main': 8,
    'A Site': 7,
    'A Link': 6,
    'Mid Courtyard': 4,
    'Mid Catwalk': 6,
    'Market': 4,
    'B Lobby': 5,
    'B Main': 3,
    'B Link': 2,
    'B Site': 0
}

def astar(graf, awal, tujuan):
    mulai = time.perf_counter()
    terbuka = [(awal, [awal], 0)]
    dikunjungi = set()
    while terbuka:
        terbuka.sort(key=lambda x: x[2] + heuristik.get(x[0], float('inf')))
        simpul, jalur, biaya = terbuka.pop(0)
        if simpul == tujuan:
            waktu = time.perf_counter() - mulai
            return jalur, biaya, waktu
        dikunjungi.add(simpul)
        for tetangga, bobot in graf.get(simpul, {}).items():
            if tetangga not in dikunjungi:
                terbuka.append((tetangga, jalur + [tetangga], biaya + bobot))
    return [], 0, float('inf')

# Eksekusi program
awal = "T Spawn"
tujuan = "B Site"
jalur, total_grid, waktu = astar(graf, awal, tujuan)

# Output hasil
print("Jalur paling efisien (A*):", " -> ".join(jalur))
print("Total Grid: {} unit".format(total_grid))
print("Waktu Eksekusi:")
print("  - Dalam milidetik: {:.8f} ms".format(waktu * 1000))
