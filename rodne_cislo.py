def validace(rc):

    if len(rc) != 11:
        return False
        
        
    if "/" not in rc[6]:
        return False
        
    rc_bez_lomitka = rc[0:6] + rc[7:11]
    
    for i in range(len(rc_bez_lomitka)):
        if int(rc_bez_lomitka[i].isnumeric()) == False:
            return False

    rc_bez_lomitka_1 = rc_bez_lomitka[1::2]
    rc_bez_lomitka_2= rc_bez_lomitka[::2]

    soucet_a = 0
    soucet_b = 0

    for i in range(len(rc_bez_lomitka_1)):
        soucet_b =soucet_b + int(rc_bez_lomitka_1[i])

    for i in range(len(rc_bez_lomitka_2)):
        soucet_a =soucet_a + int(rc_bez_lomitka_2[i])
    
    if soucet_a - soucet_b != 0:
        return False

    return True



def rodne_cislo_data(rc):

    pohlavi = "M"
    den =  int(rc[4]+rc[5])
    mesic = int(rc[2]+rc[3])
    rok = int(rc[0]+rc[1])
    
    if rok < 85:
        rok = rok+2000
        
    else:
        rok = rok+1900

    if mesic > 12:
        mesic = mesic - 50
        pohlavi = "F"

    return pohlavi,den,mesic,rok


def rodne_cislo():
    while True:
        rodne_cislo = input("Zadej rodné číslo ve formátu _ _ _ _ _ _ / _ _ _ _ (planté pro rodná čísla od roku 1985 do současnosti): ")
        rc = list(rodne_cislo)
        
        if validace(rc) == False:
            print("Chybně zadané rodné číslo")
            continue
        else:
            break
    
    print(rodne_cislo_data(rc))
    
    
rodne_cislo()    
