import numpy as np
from numpy.random import randn
from numpy import random
def matris_yapıcı():
    satır_sayısı=random.randint(1,20)
    sütun_sayısı=random.randint(1,20)
    matris=randn(satır_sayısı,sütun_sayısı)
    for satır_no in range(0,len(matris)):
        for eleman_no in range(0,len(matris[0])):
            random_number=random.randint(-5,10)
            matris[satır_no][eleman_no]=random_number
    return matris

def karasel_matris_yapıcı(boyut):
    sayı_no=boyut
    satır_sayısı=sayı_no
    sütun_sayısı=sayı_no
    matris=randn(satır_sayısı,sütun_sayısı)
    for satır_no in range(0,len(matris)):
        for eleman_no in range(0,len(matris[0])):
            random_number=random.randint(-5,10)
            matris[satır_no][eleman_no]=random_number
    return matris


