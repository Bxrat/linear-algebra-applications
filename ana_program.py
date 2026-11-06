import test_yazılımı as test
import matris_işlemleri as işlem
import matris_ozellıklerı as özellik

for sayaç in range(0,100):
    ana_matris = test.matris_yapıcı()
    print(f"{ana_matris}"+"\n")
    sonuç=işlem.RREF_Matrix(ana_matris)
    print(sonuç)
    