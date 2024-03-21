def hisobla():
    '''Do'stlaringiz bilan bron joyga ovqatlanishga borganda
    hisob nech puldan tushganligini aniqlab beruvchi funksiya'''

    total = int(input('Umumiy hisob miqdori? $'))
    foiz = int(input('Necha foiz choy-chaqa bermoqchisiz? 10, 12 yoki 15 >>'))
    if foiz == 10 or foiz == 12 or foiz == 15:
        pass
    else:
        return 'Noto\'g\'ri foiz kiritildi'

    odam_soni = int(input('Hisobni necha kishi o\'rtasida bo\'lmoqchisiz? >>'))

    har_bir_kishi = (total + total * foiz * 0.01) / odam_soni

    return f'Har bir kishi: ${har_bir_kishi} dan to\'lashi kerak'

print(hisobla())
