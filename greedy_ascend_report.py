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

def greedy_bfs(graf, awal, tujuan):
    mulai = time.perf_counter()
    terbuka = [(awal, [awal])]
    dikunjungi = set()
    while terbuka:
        terbuka.sort(key=lambda x: heuristik.get(x[0], float('inf')))
        simpul, jalur = terbuka.pop(0)
        if simpul == tujuan:
            waktu = time.perf_counter() - mulai
            total_grid = sum(graf[jalur[i]][jalur[i+1]] for i in range(len(jalur)-1))
            return jalur, total_grid, waktu
        dikunjungi.add(simpul)
        for tetangga in graf.get(simpul, {}):
            if tetangga not in dikunjungi:
                terbuka.append((tetangga, jalur + [tetangga]))
    return [], 0, float('inf')

awal = "T Spawn"
tujuan = "B Site"
jalur, total_grid, waktu = greedy_bfs(graf, awal, tujuan)
print("Jalur paling efisien (Greedy):", " -> ".join(jalur))
print("Total Grid: {} unit".format(total_grid))
print("Waktu Eksekusi:")
print("  - Dalam milidetik: {:.8f} ms".format(waktu * 1000))
