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

def MatrixSum(entry_matrix,entry_matrix2):
    matrix1 = np.array(entry_matrix, copy=True)
    if len(matrix1)!=len(entry_matrix2) or len(matrix1[0])!=len(entry_matrix2[0]):
        raise expecteions.Matrix_SizeİsNotEqual("Matrices must be MxM MxM type for sum")
    else:
        for row_counter in len(matrix1):
            for index_counter in range(0,len(matrix1[0])):
                matrix1=matrix1[row_counter][index_counter]+entry_matrix2[row_counter][index_counter]
        return matrix1

def skaler_çarpım(giren_matris,sabit_sayı):
    matris= np.array(giren_matris, copy=True)
    for satır in matris:
        for sayı in satır:
            sayı=sayı*sabit_sayı
    return matris

def MatrixMultiliper(matrix1,matrix2):
    if len(matrix1)!=len(matrix2[0]):
        raise expecteions.MatrixİsNotSuitable("Matrices is must be mxn nxm type")
    else:
        total=0.0
        temp_row=[]
        resultMatrix=[]
        for row in range(len(matrix1)):            
            for counter in range(len(matrix2[0])): 
                for column in range(len(matrix2)):
                    multi = matrix1[row][column] * matrix2[column][counter]
                    total += multi
                temp_row.append(float(total))
                total=0.0
            resultMatrix.append(temp_row)
            temp_row=[]
        return resultMatrix
                
def PowerOfMatrix(m,power):
    if power<2:
        raise expecteions.PowerMustBeMin2("Power must be minumum value of 2")
    if len(m)!=len(m[0]):
        raise expecteions.MatrixİsNotSquere("Matrix must be squre type for this calculation")
    else:
        sonuç=MatrixMultiliper(m,m)
        for counter in range(power-2):
            sonuç=MatrixMultiliper(sonuç,m)
        return sonuç

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
            self.GaussEliminitionDet()
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

    def GaussEliminitionDet(self,threshold=1e-9):
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

def RankOfMatrix(matrix,threshold=1e-9):
    m=np.array(matrix, copy=True)
    pivot=0.0
    multiplier=0.0
    for counter in range(len(m)):
        pivot=m[counter][counter]
        if abs(pivot)<threshold:
            max=0.0
            change_index=0
            for counter2 in range(counter+1,len(m)):
                if max<abs(m[counter2][counter]):

                    max=abs(m[counter2][counter])
                    change_index=counter2
            m[counter],m[change_index]=m[change_index],m[counter]
        pivot=m[counter][counter]
        for row_counter in range(counter+1,len(m)):
            multiplier=m[row_counter][counter]/pivot
            for number_index in range(len(m[row_counter])):
                m[row_counter][number_index]=m[row_counter][number_index]-(multiplier*m[counter][number_index])
    zero_counter=0
    rank=0
    for row in m:
        for numbers in row:
            if abs(numbers)<threshold:
                zero_counter+=1
        if zero_counter!=len(row):
            rank+=1
        zero_counter=0
    return rank

def RREF_Matrix(matrix,threshold=1e-9):
        np.set_printoptions(suppress=True, precision=4, threshold=100, linewidth=120)
        m=np.array(matrix, copy=True)
        pivot=0.0
        multiplier=0.0
        swap_history=[]# its for future algoritms
        secure=0
        if len(m[0])<len(m):
            secure=len(m[0])
        else:
            secure=len(m)
        for counter in range(secure):
            pivot=m[counter][counter]
            if abs(pivot)<threshold:
                max=0.0
                change_index=0
                for counter2 in range(counter+1,len(m)):
                    if max<abs(m[counter2][counter]):
                        max=abs(m[counter2][counter])
                        change_index=counter2
                        swap_history.append(counter) #its for future algoritms
                        swap_history.append(change_index) # its for future algoritms
                temp = m[counter].copy()
                m[counter] = m[change_index].copy()
                m[change_index] = temp
            pivot=m[counter][counter]
            for row_counter in range(counter+1,len(m)):
                multiplier=m[row_counter][counter]/pivot
                for number_index in range(len(m[row_counter])):
                    m[row_counter][number_index]=m[row_counter][number_index]-(multiplier*m[counter][number_index])

        for row_index in range(0,secure):
            for colmun in range(0,len(m[0])):
                m[row_index][colmun]=m[row_index][colmun]/m[row_index][row_index]
            if row_index>len(m[0]):
                break

        multiplier=0.0
        for counter in range(secure - 1, 0, -1):
            for row_index in range(counter - 1, -1, -1):
                multiplier = m[row_index][counter]
                for i in range(len(m[0])):
                    m[row_index][i] = m[row_index][i] - (multiplier * m[counter][i])
        m[abs(m) < threshold] = 0.0
        print(swap_history)
        return m
