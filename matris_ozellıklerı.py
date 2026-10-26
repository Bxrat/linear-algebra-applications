import numpy as np
import matris_işlemleri as process
import expecteions
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

def skaler_matris(matris):
    doğruluk=False
    for satır in matris:
        for sayı in satır:
            if sayı<0 and sayı>1:
                doğruluk=True
            else:
                doğruluk=False
    if doğruluk:
        print("Bu matris skaler matristir")
    else:
        print("Bu matris skaler matris değildir")
    return 0

def is_symmetrical(matrix):
    if len(matrix)!=len(matrix[0]):
        raise expecteions.MatrixİsNotSquere("Matrix must be squere type")
    else:
        for counter1 in range(len(matrix)):
            for counter2 in range(len(matrix[0])):
                if matrix[counter1][counter2]!=matrix[counter2][counter1]:
                    return "This matrix is not symetrical"
        return "This matrix is symetrical"

def anti_symetrical(matrix):
    if len(matrix)!=len(matrix[0]):
        raise expecteions.MatrixİsNotSquere("Matrix must be squere type for this process")
    else:
        for counter1 in range(len(matrix)):
            for counter2 in range(len(matrix)):
                if matrix[counter1][counter2]!= -matrix[counter2][counter1]:
                    return("This matrix is not anti symetrical")
                
        return("This matrix is anti symetrical")

def is_orthogonal(matrix):
    if len(matrix)!=len(matrix[0]):
       raise expecteions.MatrixİsNotSquere("Matrix must be squere type for this process")
    else:
        temp_matrix=np.array(matrix, copy=True)
        temp_matrix=process.transpoz(temp_matrix)
        temp_matrix=process.matris_çarpıcı(temp_matrix,matrix)
        for counter1 in range(matrix):
            for counter2 in range(matrix[0]):
                if matrix[counter1][counter2]<-1 or matrix[counter1][counter2]>1:
                    return "This matrix is not ortonal"
        return "This matrix is ortogonal"
    
def is_periodic(matrix):
    pass
    

