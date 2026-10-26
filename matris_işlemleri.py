import numpy as np
import expecteions
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

def skaler_çarpım(giren_matris,sabit_sayı):
    matris= np.array(giren_matris, copy=True)
    for satır in matris:
        for sayı in satır:
            sayı=sayı*sabit_sayı
    return matris

def matris_çarpıcı(giren_matris1,giren_matris2):
    matris1= np.array(giren_matris1, copy=True)
    matris2= np.array(giren_matris2, copy=True)
    çarpılmış_matris=[]
    geçiçi_satır=[]
    if len(matris1)!=len(matris2[0]):
        raise expecteions.MatrixİsNotEqual("Matrices is must be mxn nxm type")
    else:
        matris2=transpoz(matris2)
        for satır in matris1:
            pass

class CalcDeterminant:
    def __init__(self,matrix):
        self.temp_matrix=np.array(matrix,copy=True)
        if len(self.temp_matrix)!=len(self.temp_matrix[0]):
            raise expecteions.MatrixİsNotSquere("Matrix must be squre type for this calculation")
        if len(self.temp_matrix)==3 and len(self.temp_matrix[0])==3:
            self.result=self.SarrusRule()
        elif len(self.temp_matrix)==2 and len(self.temp_matrix[0])==2:
            m=self.temp_matrix
            self.result=m[0][0]*m[1][1]-m[0][1]*m[1][0]
        elif len(self.temp_matrix)==1 and len(self.temp_matrix[0])==1:
            self.result=self.temp_matrix[0][0]
        else:
            self.GaussEliminition()
    def SarrusRule(self):
        det =0 
        PositiveSide=0
        NegativeSide=0
        a=self.temp_matrix
        PositiveSide=(a[0][0]*a[1][1]*a[2][2])+(a[1][0]*a[2][1]*a[0][2])+(a[2][0]*a[0][1]*a[1][2])
        NegativeSide=(a[0][2]*a[1][1]*a[2][0])+(a[1][2]*a[2][1]*a[0][0])+(a[2][2]*a[0][1]*a[1][0])
        det=PositiveSide-NegativeSide
        return det
    def CountZeros(self,threshold=1e-9):
        # İT is not done yet ı am working on it
        zeros=0
        max_value=0
        max_index=0
        for index,row in enumerate(self.temp_matrix):
            for number in row:
                if abs(number)<threshold:
                    zeros=zeros+1
            if max_value<zeros:
                max_value=zeros
                max_index=index
            if zeros==len(self.temp_matrix[0]):
                max_index=index
            zeros=0
        max__column_value=0
        for index,row in enumerate(self.temp_matrix):
            for number in row:
                if abs(number)<threshold:
                    zeros=zeros+1
            if max_column_value<zeros:
                max_value=zeros
                max_index=index
            if zeros==len(self.temp_matrix[0]):
                max_index=index
            zeros=0
        if max_value==0:
            return [0,0]
        return max_index

    def LaplaceRule(self):
        #i am working on it
        pass

    def GaussEliminition(self,threshold=1e-9):
        m=np.array(self.temp_matrix, copy=True)
        pivot=0.0
        multiplier=0.0
        det_multiplier=1
        for counter in range(len(m)):
            pivot=m[counter][counter]
            if abs(pivot)<threshold:
                det_multiplier=det_multiplier*-1
                max=0.0
                change_index=0
                temp_row=[]
                for counter2 in range(counter+1,len(m)):
                    if max<abs(m[counter2][counter]):
                        # i am working on what if max==0 stiuation
                        max=abs(m[counter2][counter])
                        change_index=counter2
                m[counter],m[change_index]=m[change_index],m[counter]
            pivot=m[counter][counter]
            for row_counter in range(counter+1,len(m)):
                multiplier=m[row_counter][counter]/pivot
                for number_index in range(len(m[row_counter])):
                    m[row_counter][number_index]=m[row_counter][number_index]-(multiplier*m[counter][number_index])
        det = 1.0
        for i in range(len(m)):
            det *= m[i][i]

        return det * det_multiplier
            
