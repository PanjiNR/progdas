def kalkulasi_statistik(data_pendapatan):
    data = sorted(data_pendapatan)
    n = len(data)
    
    rerata = sum(data) / n
    tertinggi = max(data)
    terendah = min(data)
    

    sum_i_yi = sum((i + 1) * val for i, val in enumerate(data))
    gini = (2 * sum_i_yi) / (n * sum(data)) - (n + 1) / n
    
    return {
        "rata_rata": rerata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "gini": round(gini, 4)
    }