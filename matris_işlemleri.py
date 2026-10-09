import numpy as np

def matris_sayı_çarpıcı(giren_matris,sabit_sayı):
    matris = np.array(giren_matris, copy=True)
    for satır in matris:
        for indis in range(0,len(satır)):
            satır[indis]=satır[indis]*sabit_sayı
    return matris

def transpoz(giren_matris):
    matris = np.array(giren_matris, copy=True)
    geçiçi_satır=[]
    transpozu_alınmış_matris=[]
    for indis_sayacı in range(0,len(matris[0])):    
        for satır in matris:
            geçiçi_satır.extend(satır[indis_sayacı])
        transpozu_alınmış_matris.append(geçiçi_satır)
        geçiçi_satır=[]

    return transpozu_alınmış_matris

def matris_toplayıcı(giren_matris1,giren_matris2):
    matris1 = np.array(giren_matris1, copy=True)
    matris2 = np.array(giren_matris2, copy=True)
    geçiçi_satır=[]
    yeni_matris=[]
    for satır1,satır2 in zip(matris1,matris2):
        for indis_sayacı in range(0,len(satır1)):
            geçiçi_satır.extend(satır1[indis_sayacı]+satır2[indis_sayacı])
        yeni_matris.append(geçiçi_satır)
        geçiçi_satır=[]
        
            