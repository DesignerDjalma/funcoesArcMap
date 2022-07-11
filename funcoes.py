
import re

def gms_para_dg(valor, casas=15):
    grau, _, minuto, segundo, direcao =  re.split('[°\'"]', valor)
    gdc = (float(grau) + float(minuto)/60 + float(segundo)/(60*60)) * (-1 if direcao in ['W', 'S', 'O'] else 1)
    return round(gdc, casas)

def gd_para_gms(valor, casas=15):
    """transforma as coordenadas de grau decimal para grau minuto

    Args:
        valor (_type_): _description_
        casas (int, optional): _description_. Defaults to 15.
    """
    graus, r = int(valor), valor-int(valor)
    minutos, r2 = int(r*60), r*60-int(r*60) 
    segundos = round(r2*60, casas)
    resultado = '{}°{}\'{}\"'.format(graus, minutos, segundos)
    print(resultado)

def gms_para_gd_lista(arquivo_texto):
    """
    Args:
        valores (list): lista contendo os valores das coordenadas

    Returns:
        list: coordenadas transformadas
    """ 
    with open(arquivo_texto, 'r') as f:
        a = f.read().split('\n')
        for i in a:
            if not i:
                a.remove(i)
        
def gms_para_gd_converte(arq):
    with open(arq, 'r') as f:
        a = f.read()
        with open(arq[:-4]+'BKP.txt', "w") as g:
            g.write(a)

        b = a.split('\n')
        for i in b:
            if not i:
                b.remove(i)
        c = []
        for i in b:
            d = i.split(',')
            la = gms_para_dg(d[0].strip())
            lo = gms_para_dg(d[1].strip())
            c.append("{0}, {1}".format(la, lo))
    print(c)
    cor = ''
    for i in c:
        cor += str(i) + '\n'
        
    with open(arq, "w") as f:
        f.write(cor)
        

