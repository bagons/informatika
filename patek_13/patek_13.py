import datetime 

# načíst si data
date_1 = datetime.date.fromisoformat(input())
date_2 = datetime.date.fromisoformat(input())

# zjistit který je den v týdnu
date_1_day = date_1.weekday()

# kolik dní proběhene mezi daty, abychom mezi nimi mohli najít každé sedmé
pocet_dnu = (date_2 - date_1).days

# 
pocet_dnu_do_patku = [4 - date_1_day, 11 - date_1_day][date_1_day > 4]

# posuneme počet dnů mezi daty, aby jsme se dostali k pátku
# pak iterujeme po týdnech
for i in range(((pocet_dnu - pocet_dnu_do_patku) // 7) + 1):
    nahodny_patek = date_1 + datetime.timedelta(days=pocet_dnu_do_patku + i * 7)
    
    if nahodny_patek.day == 13:
        print("nalezen !", nahodny_patek)