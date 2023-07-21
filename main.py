def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

try:
    girilen_sayi = int(input("Lütfen bir sayı girin: "))
    if asal_mi(girilen_sayi):
        print(f"{girilen_sayi} bir asal sayıdır.")
    else:
        print(f"{girilen_sayi} bir asal sayı değildir.")
except ValueError:
    print("Geçerli bir tam sayı girmediniz.")
