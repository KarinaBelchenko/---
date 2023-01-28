from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"Р’ РєР°РєРѕРј РІР°СЂРёР°РЅС‚Рµ Р·Р°РїРёСЃР°С‚СЊ РґР°РЅРЅС‹Рµ?\n\n"
                    f"1 Р’Р°СЂРёР°РЅС‚:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Р’Р°СЂРёР°РЅС‚:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Р’С‹Р±РµСЂРёС‚Рµ РЅРѕРјРµСЂ РІР°СЂРёРЅР°С‚Р°: "))

    while var != 1 and var != 2:
        var = int(input("Р•С‰С‘ РѕРґРёРЅ С€Р°РЅСЃ! Р’Р°С€ РІС‹Р±РѕСЂ: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('РЈСЃРїРµС€РЅРѕ!!')




    



def print_data():
    print('1 С„Р°Р№Р»: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_second.append(''.join(data_first[j:i]))
                j = i
        data_first = data_first_second
        print(''.join(data_first))



    print('2 С„Р°Р№Р»: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())

        print(*data_second)
    
    return data_first, data_second




def put_data():
    data_first, data_second = print_data()

    data_first = data_first[:n] + [f'{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[n+1:]


def delete_data():
    pass