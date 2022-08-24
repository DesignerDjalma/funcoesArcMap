import re

def gms_para_dg(valor, casas=15):
    grau, _, minuto, segundo, direcao =  re.split('[°\'"]', valor)
    gdc = (float(grau) + float(minuto)/60 + float(segundo)/(60*60)) * (-1 if direcao in ['W', 'S', 'O'] else 1)
    print(round(gdc, casas))
    #return round(gdc, casas)

la = '01°23\'54,835"S'
lo = '46°16\'22,564"W'

print(la,lo)