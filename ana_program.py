import test_yazılımı as test
import matris_ozellıklerı as özellik

for sayaç in range(0, 1):
    ana_matris = test.karasel_matris_yapıcı()
    temp_matris = ana_matris.copy()

    print(f"{ana_matris}" + "\n")

    köşegen = özellik.asal_köşegen_çıkarıcı(ana_matris)
    yedek_köşegen = özellik.yedek_köşegen_çıkarıcı(temp_matris)

    print(f"{köşegen}" + "\n")
    print(f"{yedek_köşegen}" + "\n")
    matris_değeri=özellik.matris_izi_hesaplayıcı(ana_matris)
    print(matris_değeri)