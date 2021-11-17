
def d_in_sm (d):
    sm=d/2.54
    return sm

def sm_in_d (sm):
    d=sm*2.54
    return d

def m_in_km (m):
    km=m/1.609
    return km

def km_in_m (km):
    m=km*1.609
    return m

def ft_in_kg (ft):
    kg=ft/2.205
    return kg

def kg_in_ft (kg):
    ft=kg*2.205
    return ft

def yc_in_g (yc):
    g=yc*28.35
    return g

def g_in_yc (g):
    yc=g/28.35
    return yc

def gal_in_l (gal):
    l=gal*3.785
    return l

def l_in_gal (l):
    gal=l/3.785
    return gal

def pint_in_l (pint):
    l=pint/2.113
    return l

def l_in_pint (l):
    pint=l*2.113
    return pint


dictOfCommands = {
    1: [d_in_sm, 'дюймов в сантиметры'],
    2: [sm_in_d, 'сантиметров в дюймы'],
    3: [m_in_km, 'милей в километры'],
    4: [km_in_m, 'километров в мили'],
    5: [ft_in_kg, 'фунтов в килограммы'],
    6: [kg_in_ft, 'килограммов в фунты'],
    7: [yc_in_g, 'унций в граммы'],
    8: [g_in_yc, 'граммов в унции'],
    9: [gal_in_l, 'галлонов в литры'],
    10: [l_in_gal, 'литров в галлоны'],
    11: [pint_in_l, 'пинт в литры'],
    12: [l_in_pint, 'литров в пинты']
}

while True:
    type_of = int(input("Введите тип конвертации: "))
    number = float(input("Введите количество: "))
    if type_of == 0:
        break
    else:
        a = dictOfCommands.get(type_of)
        print(f"Перевод {a[1]} завершен. Ответ: {a[0](number)}")