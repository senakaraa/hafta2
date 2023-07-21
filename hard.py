def kac_adet_urun_satisi(cost, price):
    if cost >= price:
        raise ValueError("Birim maliyet, birim satış fiyatından düşük olmalıdır.")

    adet = 0
    while (price - cost) * adet <= 0:
        adet += 1

    return adet



cost = 100
price = 150

try:
    adet_urun = kac_adet_urun_satisi(cost, price)
    print(f"{adet_urun} adet ürün satıldığında şirket kâr eder.")
except ValueError as ve:
    print(ve)
