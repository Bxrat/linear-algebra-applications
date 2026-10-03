import numpy as np

def asal_köşegen_çıkarıcı(giren_matris):
    matris = np.array(giren_matris, copy=True)

    if len(matris[0]) != len(matris):
        #print("Köeşgen özelliği aranması için matrisin karasel olması gerekli.")
        #print("Lütfen matrisin karesel matris olup olmadığını kontrol edin")
        return 0

    imleç = 0
    for satır in matris:
        for sayaç in range(0, imleç):
            satır[sayaç] = 0
        for sayaç in range(imleç + 1, len(satır)):
            satır[sayaç] = 0
        imleç = imleç + 1
        if imleç > len(satır):
            break

    return matris


def yedek_köşegen_çıkarıcı(giren_matris):
    matris = np.array(giren_matris, copy=True)

    if len(matris[0]) != len(matris):
        #print("Köeşgen özelliği aranması için matrisin karasel olması gerekli.")
        #print("Lütfen matrisin karesel matris olup olmadığını kontrol edin")
        return 0

    imleç = len(matris[0]) - 1
    for satır in matris:
        for sayaç in range(imleç-1, -1, -1):
            satır[sayaç] = 0
        for sayaç in range(imleç + 1, len(satır)):
            satır[sayaç] = 0
        imleç = imleç - 1
        if imleç > len(satır):
            break

    return matris

def matris_izi_hesaplayıcı(giren_matris):
    matris = np.array(giren_matris, copy=True)
    matris=asal_köşegen_çıkarıcı(matris)
    imleç=0
    for satır in matris:
        for sayaç in range(0, imleç):
            satır[sayaç] = 0
        for sayaç in range(imleç + 1, len(satır)):
            satır[sayaç] = 0
        imleç = imleç + 1
        if imleç > len(satır):
            break
    matris_izi=0
    for satır in matris:
        for sayı in satır:
            if sayı!=0:
                matris_izi=matris_izi+sayı
            else:
                continue
    return int(matris_izi)
    