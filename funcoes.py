#   TUTORIAL RAPIDO DE COMO USAR.   #


    # EXECUCAO DO SCRIPT (TECLA F5)
    # >>> INFORMAR CAMINHO DO PROJETO (OPCIONAL)
    # >>> INFORMAR CAMINHO DO SHAPE
    # >>> EDITAR ARQUIVO INFORMACOES QUE SERA GERADO, CONFIRMAR.

# NUNCA ESQUECER
# PRIMEIRO LONGITUTE, DEPOIS LATITUDE
# utm: 200000.00, 9700000.00
# gms: 50°0'0.0"W, 2°0'0.0"S 
# gd: -50.0, -2.0


###################
#                 #
#   IMPORTACOES   # 
#                 #
###################

import sys
#sys.stdout.shell.write("Importando Modulos...\n","COMMENT")

import re
import os
import json
import shutil
import fnmatch
import getpass
import arcpy

# funções destaque do dia

def gms2gd(d,g,m,s):
    gdc = (float(g) + float(m)/60 + float(s)/(60*60)) * (d)
    return gdc
    
def f2(*lista):
    v = gms2gd(*lista)
    v = str(v)
    v = v.replace('.',',')
    print(v)


#########################
#                       #
#   CLASSES E FUNCOES  # 
#                       #
#########################

class Constantes:

    """Constantes necessarias para o projeto"""

    NOME_MUNICIPIOS = {'ABAETETUBA':'ABAETETUBA',
        'ABEL FIGUEIREDO':'ABEL FIGUEIREDO',
        'ACARÁ':'ACARA',
        'AFUÁ':'AFUA',
        'ÁGUA AZUL DO NORTE':'AGUA AZUL DO NORTE',
        'ALENQUER':'ALENQUER',
        'ALMEIRIM':'ALMEIRIM',
        'ALTAMIRA':'ALTAMIRA',
        'ANAJÁS':'ANAJAS',
        'ANANINDEUA':'ANANINDEUA',
        'ANAPU':'ANAPU',
        'AUGUSTO CORRÊA':'AUGUSTO CORREA',
        'AURORA DO PARÁ':'AURORA DO PARA',
        'AVEIRO':'AVEIRO',
        'BAGRE':'BAGRE',
        'BAIÃO':'BAIAO',
        'BANNACH':'BANNACH',
        'BARCARENA':'BARCARENA',
        'BELÉM':'BELEM',
        'BELTERRA':'BELTERRA',
        'BENEVIDES':'BENEVIDES',
        'BOM JESUS DO TOCANTINS':'BOM JESUS DO TOCANTINS',
        'BONITO':'BONITO',
        'BRAGANÇA':'BRAGANCA',
        'BRASIL NOVO':'BRASIL NOVO',
        'BREJO GRANDE DO ARAGUAIA':'BREJO GRANDE DO ARAGUAIA',
        'BREU BRANCO':'BREU BRANCO',
        'BREVES':'BREVES',
        'BUJARU':'BUJARU',
        'CACHOEIRA DO ARARI':'CACHOEIRA DO ARARI',
        'CACHOEIRA DO PIRIÁ':'CACHOEIRA DO PIRIA',
        'CAMETÁ':'CAMETA',
        'CANAÃ DOS CARAJÁS':'CANAA DOS CARAJAS',
        'CAPANEMA':'CAPANEMA',
        'CAPITÃO POÇO':'CAPITAO POCO',
        'CASTANHAL':'CASTANHAL',
        'CHAVES':'CHAVES',
        'COLARES':'COLARES',
        'CONCEIÇÃO DO ARAGUAIA':'CONCEICAO DO ARAGUAIA',
        'CONCÓRDIA DO PARÁ':'CONCORDIA DO PARA',
        'CUMARU DO NORTE':'CUMARU DO NORTE',
        'CURIONÓPOLIS':'CURIONOPOLIS',
        'CURRALINHO':'CURRALINHO',
        'CURUÁ':'CURUA',
        'CURUÇÁ':'CURUCA',
        'DOM ELISEU':'DOM ELISEU',
        'ELDORADO DO CARAJÁS':'ELDORADO DO CARAJAS',
        'FARO':'FARO',
        'FLORESTA DO ARAGUAIA':'FLORESTA DO ARAGUAIA',
        'GARRAFÃO DO NORTE':'GARRAFAO DO NORTE',
        'GOIANÉSIA DO PARÁ':'GOIANESIA DO PARA',
        'GURUPÁ':'GURUPÁ',
        'IGARAPÉ-AÇU':'IGARAPE-ACU',
        'IGARAPÉ-MIRI':'IGARAPE-MIRI',
        'INHANGAPI':'INHANGAPI',
        'IPIXUNA DO PARÁ':'IPIXUNA DO PARA',
        'IRITUIA':'IRITUIA',
        'ITAITUBA':'ITAITUBA',
        'ITUPIRANGA':'ITUPIRANGA',
        'JACAREACANGA':'JACAREACANGA',
        'JACUNDÁ':'JACUNDA',
        'JURUTI':'JURUTI',
        'LIMOEIRO DO AJURU':'LIMOEIRO DO AJURU',
        'MÃE DO RIO':'MAE DO RIO',
        'MAGALHÃES BARATA':'MAGALHAES BARATA',
        'MARABÁ':'MARABA',
        'MARACANÃ':'MARACANA',
        'MARAPANIM':'MARAPANIM',
        'MARITUBA':'MARITUBA',
        'MEDICILÂNDIA':'MEDICILANDIA',
        'MELGAÇO':'MELGACO',
        'MOCAJUBA':'MOCAJUBA',
        'MOJU':'MOJU',
        'MOJUÍ DOS CAMPOS':'MOJUI DOS CAMPOS',
        'MONTE ALEGRE':'MONTE ALEGRE',
        'MUANÁ':'MUANA',
        'NOVA ESPERANÇA DO PIRIÁ':'NOVA ESPERANCA DO PIRIA',
        'NOVA IPIXUNA':'NOVA IPIXUNA',
        'NOVA TIMBOTEUA':'NOVA TIMBOTEUA',
        'NOVO PROGRESSO':'NOVO PROGRESSO',
        'NOVO REPARTIMENTO':'NOVO REPARTIMENTO',
        'ÓBIDOS':'OBIDOS',
        'OEIRAS DO PARÁ':'OEIRAS DO PARA',
        'ORIXIMINÁ':'ORIXIMINA',
        'OURÉM':'OUREM',
        'OURILÂNDIA DO NORTE':'OURILANDIA DO NORTE',
        'PACAJÁ':'PACAJA',
        'PALESTINA DO PARÁ':'PALESTINA DO PARA',
        'PARAGOMINAS':'PARAGOMINAS',
        'PARAUAPEBAS':'PARAUAPEBAS',
        "PAU D'ARCO":"PAU D'ARCO",
        'PEIXE-BOI':'PEIXE-BOI',
        'PIÇARRA':'PICARRA',
        'PLACAS':'PLACAS',
        'PONTA DE PEDRAS':'PONTA DE PEDRAS',
        'PORTEL':'PORTEL',
        'PORTO DE MOZ':'PORTO DE MOZ',
        'PRAINHA':'PRAINHA',
        'PRIMAVERA':'PRIMAVERA',
        'QUATIPURU':'QUATIPURU',
        'REDENÇÃO':'REDENCAO',
        'RIO MARIA':'RIO MARIA',
        'RONDON DO PARÁ':'RONDON DO PARA',
        'RURÓPOLIS':'RUROPOLIS',
        'SALINÓPOLIS':'SALINOPOLIS',
        'SALVATERRA':'SALVATERRA',
        'SANTA BÁRBARA DO PARÁ':'SANTA BARBARA DO PARA',
        'SANTA CRUZ DO ARARI':'SANTA CRUZ DO ARARI',
        'SANTA IZABEL DO PARÁ':'SANTA ISABEL DO PARA',
        'SANTA LUZIA DO PARÁ':'SANTA LUZIA DO PARA',
        'SANTA MARIA DAS BARREIRAS':'SANTA MARIA DAS BARREIRAS',
        'SANTA MARIA DO PARÁ':'SANTA MARIA DO PARA',
        'SANTANA DO ARAGUAIA':'SANTANA DO ARAGUAIA',
        'SANTARÉM':'SANTAREM',
        'SANTARÉM NOVO':'SANTAREM NOVO',
        'SANTO ANTÔNIO DO TAUÁ':'SANTO ANTONIO DO TAUA',
        'SÃO CAETANO DE ODIVELAS':'SAO CAETANO DE ODIVELAS',
        'SÃO DOMINGOS DO ARAGUAIA':'SAO DOMINGOS DO ARAGUAIA',
        'SÃO DOMINGOS DO CAPIM':'SAO DOMINGOS DO CAPIM',
        'SÃO FÉLIX DO XINGU':'SAO FELIX DO XINGU',
        'SÃO FRANCISCO DO PARÁ':'SAO FRANCISCO DO PARA',
        'SÃO GERALDO DO ARAGUAIA':'SAO GERALDO DO ARAGUAIA',
        'SÃO JOÃO DA PONTA':'SAO JOAO DA PONTA',
        'SÃO JOÃO DE PIRABAS':'SAO JOAO DE PIRABAS',
        'SÃO JOÃO DO ARAGUAIA':'SAO JOAO DO ARAGUAIA',
        'SÃO SEBASTIÃO DA BOA VISTA':'SAO SEBASTIAO DA BOA VISTA',
        'SAPUCAIA':'SAPUCAIA',
        'SENADOR JOSÉ PORFÍRIO':'SENADOR JOSE PORFIRIO',
        'SOURE':'SOURE',
        'TAILÂNDIA':'TAILANDIA',
        'TERRA ALTA':'TERRA ALTA',
        'TERRA SANTA':'TERRA SANTA',
        'TOMÉ-AÇU':'TOME-ACU',
        'TRACUATEUA':'TRACUATEUA',
        'TRAIRÃO':'TRAIRAO',
        'TUCUMÃ':'TUCUMA',
        'TUCURUÍ':'TUCURUI',
        'ULIANÓPOLIS':'ULIANOPOLIS',
        'URUARÁ':'URUARA',
        'VIGIA':'VIGIA',
        'VISEU':'VISEU',
        'VITÓRIA DO XINGU':'VITORIA DO XINGU',
        'XINGUARA':'XINGUARA'
    }

    WKID = SRC = {'GCS_SIRGAS_2000':4674,
        'GCS_SIRGAS' 							:4170,
        'GCS_WGS_1984' 							:4326,
        'GCS_South_American_1969' 				:4618,
        'GCS_SAD_1969_96' 						:5527,
        'SAD_1969_UTM_Zone_21S' 				:29191,
        'SAD_1969_UTM_Zone_22S' 				:29192,
        'SAD_1969_UTM_Zone_23S' 				:29193,
        'SAD_1969_96_UTM_Zone_21S' 				:5531,
        'SAD_1969_96_UTM_Zone_22S' 				:5858,
        'SAD_1969_96_UTM_Zone_23S' 				:5533,
        'SIRGAS_2000_UTM_Zone_21S' 				:31981,
        'SIRGAS_2000_UTM_Zone_22S' 				:31982,
        'SIRGAS_2000_UTM_Zone_23S' 				:31983,
        'South_America_Lambert_Conformal_Conic' :102015,
        }

    OPERACOES_TABELA_DE_ATRIBUTOS = {0:{'OBJECTID':['LONG', 9, 0, 0]},
        1 :{ 'id'			:[ 'LONG' 		, 9, 0, 0 	]},
        2 :{ 'interessad'	:[ 'TEXT' 		, 0, 0, 254 ]},
        3 :{ 'imovel'		:[ 'TEXT' 		, 0, 0, 254 ]},
        4 :{ 'ano'			:[ 'LONG' 		, 9, 0, 0 	]},
        5 :{ 'processo'		:[ 'LONG' 		, 9, 0, 0 	]},
        6 :{ 'municipio'	:[ 'TEXT' 		, 0, 0, 254 ]},
        7 :{ 'parcela'		:[ 'TEXT' 		, 0, 0, 254 ]},
        8 :{ 'situacao'		:[ 'TEXT' 		, 0, 0, 254 ]},
        9 :{ 'georref'		:[ 'TEXT' 		, 0, 0, 254 ]},
        10:{ 'data'			:[ 'DATE' 		, 0, 0, 0 	]},
        11:{ 'complement'	:[ 'TEXT' 		, 0, 0, 254 ]},
        12:{ 'created_us'	:[ 'TEXT' 		, 0, 0, 254 ]},
        13:{ 'created_da'	:[ 'DATE' 		, 0, 0, 0 	]},
        14:{ 'last_edite'	:[ 'DATE' 		, 0, 0, 0 	]},
        15:{ 'last_edi_1'	:[ 'DATE' 		, 0, 0, 0 	]},
        16:{ 'Shape_Leng'	:[ 'DOUBLE' 	, 0, 0, 0 	]},
        17:{ 'Shape_Area'	:[ 'DOUBLE' 	, 0, 0, 0 	]},
        }

    UNICODES_LOWERCASE = ['\xc3\xa1',
        '\xc3\xa9','\xc3\xad',
        '\xc3\xb3','\xc3\xba',
        '\xc3\xa3','\xc3\xb5',
        '\xc3\xa2','\xc3\xaa',
        '\xc3\xae','\xc3\xb4',
        '\xc3\xbb','\xc3\xa7',
        ]

    UNICODES_UPPERCASE = ['\xc3\x81',
        '\xc3\x89','\xc3\x8d',
        '\xc3\x93','\xc3\x9a',
        '\xc3\x83','\xc3\x95',
        '\xc3\x82','\xc3\x8a',
        '\xc3\x8e','\xc3\x94',
        '\xc3\x9b','\xc3\x87',
        ]

    DEFINITION_QUERY_SITUACAO = {
        1:"{}nome = \'{}\'",
        2:"{}\"nmMun\" <> \'{}\'",
        3:"{}\"nmMun\" = \'{}\'",
        }

    NOME_CAMADA  = {
        'carta indice':"CARTA_INDICE_IBGE_DSG",
        'zee':"ZEE_2010",
        'mzee':"MZEE_2008",
        'author':'Djalma Filho',
        }


    def __init__(self):
        self.INFO_GUIA = self.carregar_info_guia

    @staticmethod
    def carregar_info_guia():
        print("Carregando Info Guia.")
        with open('INFORMACOES_GUIA.txt', 'r') as f:
            return  f.read().split(';')





def gms_para_dg(valor, casas=15):
    grau, minuto, segundo, direcao =  re.split('[°\'"]', valor)
    gdc = (float(grau) + float(minuto)/60 + float(segundo)/(60*60)) * (-1 if direcao in ['W', 'S', 'O'] else 1)
    return round(gdc, casas)

def gd_para_gms(valor, casas=15):
    """transforma as coordenadas de grau decimal para grau minuto

    Args:
        valor (_type_): _description_
        casas (int, optional): _description_. Defaults to 15.
    """
    def NEWS(v):
        if -60 < v < -46:
            return "W"
        if -10 < v < 3:
            if v > 0:
                return "N"
            if v < 0:
                return "S"
            if v == 0:
                return ""
    
    # Verifcação trocar de sinal
    sinal = ""
    if valor < 0:
        valor = abs(valor)
        sinal = "-"
    ################## AQUI NAAAAAAAAAAAAAAAO ANIMAL
    graus, r = int(valor), valor-int(valor)
    minutos, r2 = int(r*60), r*60-int(r*60) 
    segundos = round(r2*60, casas)
    resultado = '{}{}°{}\'{:.06f}\" {}'.format(sinal,graus, minutos, segundos, NEWS(valor))
    print(resultado)
    return resultado

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
        


def salvar_projeto(mxd, caminho, nome):
        """Salva o projeto."""

        if nome.endswith('.mxd'):
            salvar = os.path.join(caminho, nome)
        else:
            salvar = os.path.join(caminho, nome + '.mxd')

        mxd.saveACopy(salvar)


def texto_formatado(valores_carta_indice, pre_texto=" ", mostrar=False):
    """Retorna o texto que sera utilizada no layout."""

    texto = pre_texto
    vci = valores_carta_indice

    if len(vci) >= 2:
        for v in vci:
            if v != vci[-1] and v != vci[-2]:
                texto += v + ", "
            if v == vci[-2]:
                texto += v + " e "
            if v == vci[-1]:
                texto += v
    else:
        for v in vci:
            texto += v

    return texto


def string_to_map(mxd, string_da_camada):
    """Retorna o map correspondente a string."""

    if isinstance(string_da_camada, str):
        print("convertendo str to <map>")
        for i in arcpy.mapping.ListLayers(mxd):
            if i.name == string_da_camada:
                string_da_camada = i
                return string_da_camada
    else:
        return string_da_camada


def limpar_selecao(camada):
    """Retira a Selecao feita sobre uma determinada camada"""

    arcpy.SelectLayerByAttribute_management(camada,"CLEAR_SELECTION")


def att_situacao(mxd, municipios='nenhum', *args):
    """Atualiza o mapa de situacao de acordo com as 
    entradas fornecidas (1 ou mais):
    att_situacao('BELÉM','ACARÁ',...)"""

    municipio = tuple([municipios]) + args
    EXP = ["{}".format(i) for i in range(1, 4)]
    fz = 1.084556648631034
    df = False
    mxd = mxd 
    cmds = arcpy.mapping.ListLayers(mxd)
    cdi = [cmd for exp in EXP for cmd in cmds if cmd.description[:1] == exp]
    
    if municipio[0] == 'nenhum':
        e1 = e2 = e3 = ""
        for i, (c, exp) in enumerate(zip(cdi, [e1, e2, e3])):
            c.definitionQuery = exp
        arcpy.RefreshActiveView()
        return

    if not df:
        df = arcpy.mapping.ListDataFrames(mxd)[-1]

    if municipio and isinstance(municipio, tuple):
        lm = []
        for m in municipio:
            m = m.upper()
            for u, U in zip(uni, UNI):
                m = m.replace(u,U)
            lm.append(m)
        for i, v in enumerate(lm):
            if i == 0:
                e1 = P[1].format("", v)
                e2 = P[2].format("", v)
                e3 = P[3].format("", v)
                continue
            e1 += P[1].format(" OR ", v)
            e2 += P[2].format(" AND ",v)
            e3 += P[3].format(" OR ", v)

    if municipio and isinstance(municipio, str):
        municipio = municipio.upper()
        for u, U in zip(uni, UNI):
            municipio = municipio.replace(u,U)
            m = municipio

        e1 = P[1].format("",m)
        e2 = P[2].format("",m)
        e3 = P[3].format("",m)
    
    for i, (c, exp) in enumerate(zip(cdi, [e1, e2, e3])):
        c.definitionQuery = exp
        if i == 2:
            z = c.getSelectedExtent()

    df.extent = z
    df.scale *= fz


def intersecao(camada_alvo, camada_dica, tipo="INTERSECT"):
    """Pega a camada_dica e seleciona as feicoes na camada alvo,
    retornando o valor na tabela de atributos, para oo atributo especificado"""

    arcpy.SelectLayerByLocation_management(
        camada_dica,
        camada_alvo,
        "INTERSECT",
        )


def zoom_camada(mxd, camada, data_frame):
    """Aplica um zoom numa escala media e numero inteiro."""

    cmds = arcpy.mapping.ListLayers(mxd)
    for i in cmds:
        if i.name == camada.name:
            camada = i

    obj_zoom = camada.getSelectedExtent()
    data_frame.extent = obj_zoom

    # Numbers Trick
    fator = len(str(data_frame.scale).split('.')[0])-1
    z = '1'+'0'*fator
    escala = data_frame.scale/int(z)

    # Exception
    if escala > 2:
        escala = (round(escala,0)*3)*int(z)
        z2 = z + '0'
        escala = round(escala/int(z2),0)*int(z2)
        data_frame.scale = escala
        arcpy.RefreshActiveView()
        return 1

    # Final 
    escala = (round(escala,0)*3)*int(z)
    data_frame.scale = escala
    arcpy.RefreshActiveView()
    return 2


def get_atributo_tda(camada_interesse, ref_cmd, atributo, mostrar=False):
    """Retorna o valor da tabela de atributos da intersecao de camadas"""

    camada_interesse = (camada_interesse)
    camada_alvo = string_to_map(mxd, CMD[ref_cmd])
    intersecao(
        camada_alvo=camada_alvo,camada_dica=camada_interesse
        )
    return get_valor_tda(camada_interesse=camada_alvo, atributo=atributo)


def get_valor_tda(camada_interesse, atributo,):
    """Retorna uma lista com o valor de cada linha no atributo selecionada."""

    cursor = arcpy.SearchCursor(
                dataset=string_to_map(mxd, camada_interesse)
                )
    return [i.getValue(atributo) for i in cursor]


def get_carta_indice(camada_interesse, ref_cmd ='carta indice', atributo ='cint', mostrar=False):
    """Retorna uma lista com os valores das Cartas Indices."""

    return get_atributo_tda(camada_interesse, ref_cmd, atributo, mostrar)


def get_zee(camada_interesse, ref_cmd ='zee', atributo ='zona', mostrar=False):
    """Retorna uma lista com os valores do ZEE."""

    return get_atributo_tda(camada_interesse, ref_cmd, atributo, mostrar)


def get_mzee(camada_interesse, ref_cmd ='mzee', atributo ='grupo', mostrar=False):
    """Retorna uma lista com os valores do MZEE."""

    return get_atributo_tda(camada_interesse, ref_cmd, atributo, mostrar)


def zoom(mxd, camada, data_frame):
    """Aplica um zoom numa escala media e numero inteiro."""

    cmds = arcpy.mapping.ListLayers(mxd)
    for i in cmds:
        if i.name == camada.name:
            camada = i

    obj_zoom = camada.getSelectedExtent()
    data_frame.extent = obj_zoom

    # Numbers Trick
    fator = len(str(data_frame.scale).split('.')[0])-1
    z = '1'+'0'*fator
    escala = data_frame.scale/int(z)

    # Exception
    if escala > 2:
        escala = (round(escala,0)*3)*int(z)
        z2 = z + '0'
        escala = round(escala/int(z2),0)*int(z2)
        data_frame.scale = escala
        arcpy.RefreshActiveView()
        return [1, camada]

    # Final 
    escala = (round(escala,0)*3)*int(z)
    data_frame.scale = escala
    arcpy.RefreshActiveView()
    print("Escala Selecionada: {}".format(escala))
    return [2, camada]


def aplicar_simbologia(nome_camada, camada_a_aplicar):
    """ Pega a camada desejada copia sua simbologia na camada a aplicar."""

    for layer in arcpy.mapping.ListLayers(arcpy.mapping.MapDocument(caminho_mxd)):
        if layer.name == nome_camada:
            simb = layer
    arcpy.ApplySymbologyFromLayer_management(camada_a_aplicar, simb)


def copiar_shapes(camada_a_ser_copiada, camada_alvo):
    print("copiando os valores")
    camada_alvo = arcpy.da.InsertCursor(camada_alvo, ["SHAPE@"])
    with arcpy.da.SearchCursor(camada_a_ser_copiada, ["SHAPE@"]) as cursor:
        for shape in cursor:
            camada_alvo.insertRow(shape)  
            print(shape)
    print("Atualizando")
    arcpy.RefreshActiveView()


def criar_buffer(camada, distancia_metros=300):
    pasta = 'C:\\Users\\{0}\\arcgis_temp'.format(getpass.getuser())
    camada_saida = os.path.join(pasta, "buffer")
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print("Pasta Criada")
    else:
        print("Pasta ja existe, removendo..")
        try:
            shutil.rmtree(pasta)
            os.mkdir(pasta)
        except Exception as e:
            print_vermelho("Nao foi possivel realizar remocao e criacao")
            print_vermelho(str(e))
            print("\n\tContinuando Processos....\n")
            
        print("Pasta Criada")

    distancia = str(distancia_metros) + " Meters"
    arcpy.Buffer_analysis(camada, camada_saida, distancia)
    
    pasta = 'C:\\Users\\{0}\\arcgis_temp'.format(getpass.getuser())
    caminho_busca = os.path.join(pasta, "buffer.shp")
    buffer = arcpy.mapping.Layer(caminho_busca)
    arcpy.mapping.AddLayer(df, buffer, "TOP")
    print("Buffer Criado com sucesso!")
    return buffer


def apagar_buffer(buffer):
    mxd = arcpy.mapping.MapDocument(caminho_mxd)
    principal = arcpy.mapping.ListDataFrames(mxd)[0]
    layers = arcpy.mapping.ListLayers(mxd)
    print("Removendo: ",layers[0].name)
    arcpy.mapping.RemoveLayer(principal, layers[0])


def limpa_tda(camada_alvo):
    arcpy.DeleteRows_management(camada_alvo)


def area_limitacao(nome_camada, distancia_metros=300):
    print("Criando Buffer")
    buffer = criar_buffer(camada=nome_camada, distancia_metros=300)
    try:
        limpa_tda(camada_alvo=r"LEGENDA\AREA DE LIMITACAO")
    except:
        print("LimpaTDA falhou, continuando...")

    arg1 = r'C:\Users\dflfilho\arcgis_temp\buffer.shp'
    arg2 = string_to_map(arcpy.mapping.MapDocument(caminho_mxd),"AREA DE LIMITACAO")
    
    print("Args de area de limitacao!")
    print(arg1)
    print(arg2)
    
    print("COPIANDO AS TABELAS DE TRIBUTOS!")
    copiar_shapes(
        camada_a_ser_copiada=arg1,
        camada_alvo=arg2,
        )
    print("APAGANDO BUFFER DO PROJETO!!!!")
    apagar_buffer(buffer)


def print_vermelho(texto="..."):
    """Printa em vermelho no IDLE."""

    sys.stdout.shell.write(texto,"COMMENT")


def _get_informacoes_valores(camada):
    caminho = os.path.dirname(camada.dataSource)
    arqs = os.listdir(caminho)
    for arq in arqs:
        if fnmatch.fnmatch(arq, '*.txt'):
            if arq.lower().startswith("infor"):
                print("Carregando {}".format(arq))
                txt = os.path.join(caminho, arq)
                with open(txt, 'r') as f:
                    _info = f.read().split(';')
                    info = map(lambda x: x.strip(), _info)
            else:
                pass
    return info, caminho


class Geometria:

    """Geometria(caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar)
    
    Inseri um conjunto de Coordenadas apartir de um arquivo .txt
    em um Shape.
    """

    def __init__(self, caminho_coordenadas, caminho_shape, tipo_geometria, epsg, plotar=False):
        self.caminho_coordenadas = caminho_coordenadas
        self.caminho_shape = caminho_shape
        self.tipo_geometria = tipo_geometria
        self.epsg = epsg

        if plotar:
            self.plotar()

    @staticmethod
    def _lerArquivo(caminho_arquivo):
        """Le o arquivos com as coordenadas em formato x,y.

        Args:
            caminho_arquivo (str): caminho contendo o arquivo .txt.

        Returns:
            str: String contendo as coordenadas pseudo-formatadas
        """
        with open(caminho_arquivo, 'r') as f:
            coordenadas = f.read()
            return coordenadas

    @staticmethod
    def _criarGeometriaVazia(caminho_salvar, tipo_geometria, EPSG=4674):
        """Cria uma geometria do tipo POINT vazio.

        Args:
            caminho_salvar (str): caminho no qual o .shp sera salvo
            tipo_geometria (str): "POINT", "POLYLINE" ou "POLYGON".
            EPSG (int, optional): Projecao do Shape. Padrao 4674 SIRGAS 2000.

        Returns:
            str: caminho no qual o .shp foi salvo
        """
        arcpy.CreateFeatureclass_management(
            spatial_reference=arcpy.SpatialReference(EPSG),
            out_path=os.path.dirname(caminho_salvar),
            out_name=os.path.basename(caminho_salvar),
            geometry_type=tipo_geometria,
        )
        return caminho_salvar

    def _plotarCoordenadas(self, coordenadas, shape):
        """Formata as coordenadas e ensira pra cada ponto uma linha na TDA do .shp

        Args:
            coordenadas (str): coordenadas pseudo-formatadas
            shape (str): Caminho do .shp que sera inserida coordenadas
        """
        def _ponto():
            cc = coordenadas.split('\n')
            cc.pop()
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
                cursor.insertRow([p])

        def _poligono():
            cc = coordenadas.split('\n')
            cc.pop()
            lista = []
            for i in cc:
                xey = i.split(',')
                x, y = float(xey[0]), float(xey[1])
                p = arcpy.Point(x,y)
                lista.append(p)
            array = arcpy.Array(items=lista)
            poligono = arcpy.Polygon(array)
            cursor = arcpy.da.InsertCursor(shape, ["SHAPE@"])
            cursor.insertRow([poligono])

        if self.tipo_geometria == "POINT":
            _ponto()
        if self.tipo_geometria == "POLYGON":
            _poligono()
            
    def plotar(self):
        """Faz os procedimentos necessarios."""
        
        coordenadas = self._lerArquivo(
            caminho_arquivo=self.caminho_coordenadas)

        shape = self._criarGeometriaVazia(
            caminho_salvar=self.caminho_shape,
            tipo_geometria=self.tipo_geometria,
            EPSG=self.epsg)
        
        
        self._plotarCoordenadas(
            coordenadas=coordenadas,
            shape=shape)


################
#              #
#  CONSTANTES  #
#              #
################

# comentario inutil

conts = Constantes()
DM = conts.NOME_MUNICIPIOS
SRC = conts.SRC
OTDA = conts.OPERACOES_TABELA_DE_ATRIBUTOS
uni = conts.UNICODES_LOWERCASE
UNI = conts.UNICODES_UPPERCASE
P = conts.DEFINITION_QUERY_SITUACAO
CMD = conts.NOME_CAMADA
INFO_GUIA = conts.INFO_GUIA

# Caminho Padrao do arquivo MXD
paths = {
    "mxd":"C:\\01_DJALMA_ESTAGIARIO\\PROCESSOS\\PASTA\\ProjetoArcMap.mxd",
    "raquel":"C:\\01_DJALMA_ESTAGIARIO\\PROCESSOS\\PASTA\\ProjetoArcMapRaquel1.mxd",

}
caminho_mxd = paths['raquel']
