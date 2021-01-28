print("1. Дюймы в сантиметры\n"
      "2. Сантиметры в дюймы\n"
      "3. Мили в километры\n"
      "4. Километры в мили\n"
      "5. Фунты в килограммы\n"
      "6. Килограммы в фунты\n"
      "7. Унции в граммы\n"
      "8. Граммы в унции\n"
      "9. Галлон в литры\n"
      "10. Литры в галлоны\n"
      "11. Пинты в литры\n"
      "12. Литры в пинты\n")

def inch_to_sant(number):
    sant = number*2.54
    return sant

def sant_to_inch(number):
    inch = number/2.54
    return inch

def mile_to_kilo(number):
    mile = number/1.6
    return mile

def kilo_to_mile(number):
    kilo = number*1.6
    return kilo

def pound_to_kilo(number):
    kilo = number/2.2
    return kilo

def kilo_to_pound(number):
    pound = number*2.2
    return pound

def unc_to_gramm(number):
    gramm = number*28.34
    return gramm

def gramm_to_unc(number):
    unc = number*0.03
    return unc

def gallon_to_litre(number):
    litre = number*3.78
    return litre

def litre_to_gallon(number):
    gallon = number / 3.78
    return gallon

def pint_to_litre(number):
    litre = number * 2
    return litre

def litre_to_pinte(number):
    pinte = number / 2
    return pinte

while True:
    select = int(input('choose a number from 1 to 12:'))
    select_number = int(input('choose a value:'))
    if select == 1:
        print(inch_to_sant(select_number))
    if select == 2:
        print(sant_to_inch(select_number))
    if select == 3:
        print(mile_to_kilo(select_number))
    if select == 4:
        print(kilo_to_mile(select_number))
    if select == 5:
        print(pound_to_kilo(select_number))
    if select == 6:
        print(kilo_to_pound(select_number))
    if select == 7:
        print(unc_to_gramm(select_number))
    if select == 8:
        print(gramm_to_unc(select_number))
    if select == 9:
        print(gallon_to_litre(select_number))
    if select == 10:
        print(litre_to_gallon(select_number))
    if select == 11:
        print(pint_to_litre(select_number))
    if select == 12:
        print(litre_to_pinte(select_number))
    if select == 0:
        break







