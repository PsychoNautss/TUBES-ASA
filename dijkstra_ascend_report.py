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

def Dijkstra(graf, awal, tujuan):
    mulai = time.perf_counter()
    jarak = {simpul: float('inf') for simpul in graf}
    jarak[awal] = 0
    sebelumnya = {}
    belum_dikunjungi = set(graf.keys())

    while belum_dikunjungi:
        simpul_terdekat = min(
            (s for s in belum_dikunjungi if jarak[s] != float('inf')),
            key=lambda s: jarak[s],
            default=None
        )
        if simpul_terdekat is None or simpul_terdekat == tujuan:
            break
        belum_dikunjungi.remove(simpul_terdekat)
        for tetangga, bobot in graf[simpul_terdekat].items():
            total = jarak[simpul_terdekat] + bobot
            if total < jarak.get(tetangga, float('inf')):
                jarak[tetangga] = total
                sebelumnya[tetangga] = simpul_terdekat

    jalur = []
    simpul = tujuan
    while simpul in sebelumnya:
        jalur.insert(0, simpul)
        simpul = sebelumnya[simpul]
    if jalur:
        jalur.insert(0, simpul)

    waktu = time.perf_counter() - mulai
    total_grid = sum(graf[jalur[i]][jalur[i+1]] for i in range(len(jalur)-1))
    return jalur, total_grid, waktu

# Eksekusi
awal = "T Spawn"
tujuan = "B Site"
jalur, total_grid, waktu = Dijkstra(graf, awal, tujuan)
print("Jalur paling efisien (Dijkstra):", " -> ".join(jalur))
print("Total Grid: {} unit".format(total_grid))
print("Waktu Eksekusi:")
print("  Dalam milidetik: {:.8f} ms".format(waktu * 1000))
