hemA_say = hemB_say = top_hasta_say = 0
agır_say = orta_say = hafif_say = 0
pro_hemA_say = pro_hemB_say = 0
binlik_flakon_say = besyuzluk_flakon_say = ikiyuzellilik_flakon_say = 0
tüm_hasta_aylık_top_ilac = 0
top_aylık_ilac_tutarı = 0
in_hemA_say = in_hemB_say = 0
pro_orta_say = 0
plazma_hemA_say = rekom_hemA_say = plazma_hemB_say = rekom_hemB_say = 0
plazma_faktor8_mik = plazma_faktor9_mik = rekom_faktor8_mik = rekom_faktor9_mik = 0
top_binlik_f_say = top_besyuzluk_f_say = top_ikiyuzellilik_f_say = 0
max_ilac_tutarı=max_ilac_tutarı2=max_ilac_tutarı3=0
max_ilac_mik=max_ilac_mik2=max_ilac_mik3=0
aylık_binlik_flakon_say=aylık_besyuzluk_flakon_say=aylık_ikiyuzellilik_flakon_say=0
p_hemA_faktor8_1000lik_flakon_say = p_hemA_faktor8_500lük_flakon_say = p_hemA_faktor8_250lik_flakon_say = 0
r_hemA_faktor8_1000lik_flakon_say = r_hemA_faktor8_500lük_flakon_say = r_hemA_faktor8_250lik_flakon_say = 0
p_hemB_faktor9_1000lik_flakon_say = p_hemB_faktor9_500lük_flakon_say = p_hemB_faktor9_250lik_flakon_say = 0
r_hemB_faktor9_1000lik_flakon_say = r_hemB_faktor9_500lük_flakon_say = r_hemB_faktor9_250lik_flakon_say = 0

while True: #Python'da koşul sona yazılamadığı için sonsuz döngü yapıldı.

    kimlik_no = input("Hastanın TC kimlik numarasını giriniz:")
    ad_soyad = input("Hastanın adını ve soyadını giriniz:")
    top_hasta_say += 1
    tip = input("Hastanın hemofili tipini(A/a/B/b) giriniz:")
    while tip not in ['A', 'a', 'B', 'b']: #A,a,B,b harflerinden farklı bir giriş sağlanmaması için liste ve in kullanıldı.
        print("Hatalı giriş yaptınız.(A/a/B/b) harflerinden birini seçmelisiniz!")
        tip = input("Hastanın hemofili tipini (A/a/B/b) tekrar giriniz:")

    if (tip == "A" or tip == "a"):
        hemA_say += 1
    if (tip == "B" or tip == "b"):
        hemB_say += 1

    faktor_miktarı = float(input("Faktör miktarını giriniz(0-50):"))
    while (not 0 <= faktor_miktarı < 50):
        print("Hatalı giriş yaptınız.0 ile 50 arasında bir değer girmelisiniz!")
        faktor_miktarı = float(input("Faktör miktarını tekrar giriniz:"))

    antikor_miktari = float(input("Kandaki antikor miktarını(ünite cinsinden) giriniz:"))

    while (antikor_miktari < 0):
        print("Hatalı giriş yaptınız.Antikor miktarı pozitif bir değer olmalı!")
        antikor_miktari = float(input("Kandaki antikor miktarını(ünite cinsinden) giriniz:"))

    if (1 <= faktor_miktarı < 5):
        kanama_say = int(input("Son 1 yılda meydana gelen kanama sayısını giriniz: "))
        while (kanama_say < 0):
            print("Hatalı giriş yaptınız.Kanama sayısı pozitif bir değer olmalı!")
            kanama_say = int(input("Son 1 yılda meydana gelen kanama sayısını tekrar giriniz: "))

    if ((tip == "A" or tip == "a") and (antikor_miktari > 5)):
        in_hemA_say += 1
    if ((tip == "B" or tip == "b") and (antikor_miktari > 5)):
        in_hemB_say += 1

    if (antikor_miktari < 5):
        if (0 < faktor_miktarı < 1 or (1 <= faktor_miktarı < 5 and kanama_say > 3)):
            kilo = float(input("Hastanın kilosunu (KG cinsinden) giriniz:"))
            while (kilo < 0):
                print("Hatalı giriş yaptınız.Kilo pozitif bir değer olmalı!")
                kilo = float(input("Hastanın kilosunu (KG cinsinden)tekrar giriniz:"))

            ilac_türü = input("Hastanın kullanacağı faktör ilacın türünü giriniz (P/p/R/r):")
            while ilac_türü not in ['P', 'p', 'R', 'r']:
                print("Hatalı giriş yaptınız.(P/p/R/r) harflerinden birini seçmelisiniz")
                ilac_türü = input("Hastanın kullanacağı faktör ilacın türünü tekrar giriniz (P/p/R/r):")

    baslık = "*** Hastanın Bilgileri ***"
    print("-" * len(baslık), sep='') #Başlıktaki karakter sayısı kadar '-' karakteri koyabilmek için len() kullandık.
    print(baslık, "\n", "-" * len(baslık), sep='')
    print("Hastanın TC kimlik numarası:", kimlik_no)
    print("Hastanın adı soyadı:", ad_soyad)
    print("Hastalığın tipi:", tip)

    if (0 < faktor_miktarı < 1):
        siddet = "Ağır"
        print("Hastalığın şiddeti", siddet)
        agır_say += 1

    elif (1 <= faktor_miktarı < 5):
        siddet = "Orta"
        print("Hastalığın şiddeti", siddet)
        orta_say += 1

    elif (5 <= faktor_miktarı < 50):
        siddet = "Hafif"
        print("Hastalığın şiddeti", siddet)
        hafif_say += 1

    if (antikor_miktari < 5) and (0 < faktor_miktarı < 1 or (1 <= faktor_miktarı < 5 and kanama_say > 3)):
        print("Hastaya profilaksi tedavisi uygulanacak!", "\n")

        if (ilac_türü == "P" or ilac_türü == "p"):
            ilac_türü_adı = "Plazma Kaynaklı"
            ucret = 1.25

        if (ilac_türü == "R" or ilac_türü == "r"):
            ilac_türü_adı = "Rekombinant"
            ucret = 1.5

        if (tip == "A" or tip == "a"):
            tip_adı = "Faktör-8"
            ilac_say = 3
            artıs = 2
            pro_hemA_say += 1

        elif (tip == "B" or tip == "b"):
            tip_adı = "Faktör-9"
            ilac_say = 2
            artıs = 1
            pro_hemB_say += 1

        print("Kullanacağı faktör ilacı:", ilac_türü_adı, tip_adı, sep=' ')
        print("Haftada kaç sefer ilaç kullanacağı:", ilac_say)
        min_ilac_miktar = (40 - faktor_miktarı) * kilo / artıs
        print("Bir seferde kullanması gereken minumum ilaç miktarı:", format(min_ilac_miktar, ".2f"),"ünite")
        binlik_flakon_say = int(min_ilac_miktar / 1000) #Minumum ilaç miktarını alıp flakon sayısını hesaplamak için
        kalan_miktar = min_ilac_miktar % 1000           #Mod işlemini ve if else yapısını kullandık.

        if (kalan_miktar > 750):
            binlik_flakon_say += 1
            top_binlik_f_say += binlik_flakon_say

        elif (kalan_miktar > 500):
            besyuzluk_flakon_say = 1
            ikiyuzellilik_flakon_say = 1
            top_binlik_f_say += besyuzluk_flakon_say
            top_ikiyuzellilik_f_say += ikiyuzellilik_flakon_say

        elif (kalan_miktar > 250):
            besyuzluk_flakon_say = 1
            top_binlik_f_say += besyuzluk_flakon_say

        else:
            ikiyuzellilik_flakon_say = 1
            top_ikiyuzellilik_f_say += ikiyuzellilik_flakon_say

        kullanılacak_ilac = binlik_flakon_say * 1000 + besyuzluk_flakon_say * 500 + ikiyuzellilik_flakon_say * 250

        print("Hastanın bir seferde kullanacağı ilaç miktarı:",kullanılacak_ilac,"ünite")
        print("Hastanın kullanacağı flakon çeşit ve sayıları:")
        if (binlik_flakon_say >= 1):
            print(" 1000'lik flakon sayısı:", binlik_flakon_say)
        if (besyuzluk_flakon_say >= 1):
            print(" 500'luk flakon sayısı:", besyuzluk_flakon_say)
        if (ikiyuzellilik_flakon_say >= 1):
            print(" 250'lilik flakon sayısı:", ikiyuzellilik_flakon_say)

        aylık_top_ilac = int(4 * (ilac_say) * (kullanılacak_ilac))
        print("4 haftalık toplam ilaç miktari:", aylık_top_ilac, "ünite")

        tüm_hasta_aylık_top_ilac += aylık_top_ilac

        if (binlik_flakon_say >= 1):
            aylık_binlik_flakon_say = 4 * (ilac_say * binlik_flakon_say)
            print("4 haftalık 1000'lik flakon sayısı:", aylık_binlik_flakon_say)
        if (besyuzluk_flakon_say >= 1):
            aylık_besyuzluk_flakon_say = 4 * (ilac_say * besyuzluk_flakon_say)
            print("4 haftalık 500'lük flakon sayısı:", aylık_besyuzluk_flakon_say)
        if (ikiyuzellilik_flakon_say >= 1):
            aylık_ikiyuzellilik_flakon_say = 4 * (ilac_say * ikiyuzellilik_flakon_say)
            print("4 haftalık 250'lik flakon sayısı:", aylık_ikiyuzellilik_flakon_say)

        aylık_ilac_tutarı = ((ucret * ilac_say) * (kullanılacak_ilac))*4
        top_aylık_ilac_tutarı += aylık_ilac_tutarı

        print("4 haftalık ilaç tutarı:", format(aylık_ilac_tutarı, ".2f"), "TL","\n")

        if (siddet == "Ağır" and antikor_miktari < 5):
            pro_orta_say += 1

        if ((tip == "A" or tip == "a") and (ilac_türü == "P" or ilac_türü == "p")):
            plazma_hemA_say += 1
            plazma_faktor8_mik += aylık_top_ilac
            p_hemA_faktor8_1000lik_flakon_say += aylık_binlik_flakon_say
            p_hemA_faktor8_500lük_flakon_say += aylık_besyuzluk_flakon_say
            p_hemA_faktor8_250lik_flakon_say += aylık_ikiyuzellilik_flakon_say

        if ((tip == "A" or tip == "a") and (ilac_türü == "R" or ilac_türü == "r")):
            rekom_hemA_say += 1
            rekom_faktor8_mik += aylık_top_ilac
            r_hemA_faktor8_1000lik_flakon_say += aylık_binlik_flakon_say
            r_hemA_faktor8_500lük_flakon_say += aylık_besyuzluk_flakon_say
            r_hemA_faktor8_250lik_flakon_say += aylık_ikiyuzellilik_flakon_say

        if ((tip == "B" or tip == "b") and (ilac_türü == "P" or ilac_türü == "p")):
            plazma_hemB_say += 1
            plazma_faktor9_mik += aylık_top_ilac
            p_hemB_faktor9_1000lik_flakon_say += aylık_binlik_flakon_say
            p_hemB_faktor9_500lük_flakon_say += aylık_besyuzluk_flakon_say
            p_hemB_faktor9_250lik_flakon_say += aylık_ikiyuzellilik_flakon_say

        if ((tip == "B" or tip == "b") and (ilac_türü == "R" or ilac_türü == "r")):
            rekom_hemB_say += 1
            rekom_faktor9_mik += aylık_top_ilac
            r_hemB_faktor9_1000lik_flakon_say += aylık_binlik_flakon_say
            r_hemB_faktor9_500lük_flakon_say += aylık_besyuzluk_flakon_say
            r_hemB_faktor9_250lik_flakon_say += aylık_ikiyuzellilik_flakon_say

        if (tip == "A" or tip == "a"):
            if (aylık_top_ilac > max_ilac_mik):
                max_ilac_mik = aylık_top_ilac
                max_tc = kimlik_no
                max_ad_soyad = ad_soyad
                max_siddet = siddet
                max_kilo = kilo
                max_ilac_türü = ilac_türü_adı
                max_ilac_tutarı= aylık_ilac_tutarı

        if (tip == "B" or tip == "b"):
            if (aylık_top_ilac > max_ilac_mik2):
                max_ilac_mik2 = aylık_top_ilac
                max_tc2 = kimlik_no
                max_ad_soyad2 = ad_soyad
                max_siddet2 = siddet
                max_kilo2 = kilo
                max_ilac_türü2 = ilac_türü_adı
                max_ilac_tutarı2 = aylık_ilac_tutarı

        if (aylık_ilac_tutarı > max_ilac_tutarı3):
            max_ilac_tutarı3= aylık_ilac_tutarı
            max_tc3 = kimlik_no
            max_ad_soyad3 = ad_soyad
            max_tip= tip_adı
            max_siddet3 = siddet
            max_kilo3 = kilo
            max_ilac_türü3 = ilac_türü_adı
            max_ilac_mik3 = aylık_top_ilac

    else:
        print("Hastaya profilaksi tedavisi uygulanmayacak!", "\n")

    devam = input("Başka hasta var mı(e/E/h/H)?:")
    while devam not in ['e', 'E', 'h', 'H']:
        print("Hatalı giriş yaptınız.(e/E/h/H) harflerinden birini girmelisiniz!")
        devam = input("Başka hasta var mı(e/E/h/H)?:")

    if devam == 'h' or devam == 'H':
        break   #Devam h veya H harfine eşit olunca programı sonlandırıp istatikleri yazdırmak için break kullandık

baslık2 = "*** İ S T A T İ K S E L   B İ L G İ L E R ***"
print("-" * len(baslık2), sep='')
print(baslık2, "\n", "-" * len(baslık2), sep='', end="\n")
print("Toplam hemofili-A hasta sayısı:", hemA_say)
print("Toplam hemofili-B hasta sayısı:", hemB_say)
print("Toplam hasta sayısı:", top_hasta_say, "\n")

print("Hastalığın şiddeti ağır olan hastaların yüzdesi:", "%", format((agır_say / top_hasta_say) * 100, ".2f"))
print("Hastalığın şiddeti orta olan hastaların yüzdesi:", "%", format((orta_say / top_hasta_say) * 100, ".2f"))
print("Hastalığın şiddeti hafif olan hastaların yüzdesi:", "%", format((hafif_say / top_hasta_say) * 100, ".2f"), "\n")

print("Hemofili A hastalarındaki inhibitör varlığı yüzdeleri:", "%", format((in_hemA_say / hemA_say) * 100, ".2f"))
print("Hemofili B hastalarındaki inhibitör varlığı yüzdeleri:", "%", format((in_hemB_say / hemB_say) * 100, ".2f"),
      "\n")

print("Profilaksi uygulanan hemA sayısı:", pro_hemA_say)
print("Profilaksi uygulanan hemA yuzdesi:", "%", format((pro_hemA_say / top_hasta_say) * 100, ".2f"))
print("Profilaksi uygulanan hemB sayısı:", pro_hemB_say)
print("Profilaksi uygulanan hemB yuzdesi:", "%", format((pro_hemB_say / top_hasta_say) * 100, ".2f"), "\n")

print("Hastalığının şiddeti orta olan hemofili hastaları içinde, profilaksi uygulanan hastaların yüzdesi:",
      format((pro_orta_say / orta_say) * 100, ".2f"), "\n")

print("Profilaksi uygulanan Hemofili-A hastaları içinde, plazma kaynaklı faktör ilacı kullanan hastaların yüzdesi:",
      "%", format((plazma_hemA_say / hemA_say) * 100, ".2f"))
print("Profilaksi uygulanan Hemofili-A hastaları içinde,rekombinant faktör ilacı kullanan hastaların yüzdesi:", "%",
      format((rekom_hemA_say / hemA_say) * 100, ".2f"))
print("Profilaksi uygulanan Hemofili-B hastaları içinde,plazman kaynaklı faktör ilacı kullanan hastaların yüzdesi:",
      "%", format((plazma_hemB_say / hemA_say) * 100, ".2f"))
print(
    "Profilaksi uygulanan Hemofili-B hastaları içinde, rekombinant kaynaklı faktör ilacı kullanan hastaların yüzdesi:",
    "%", format((rekom_hemB_say / hemA_say) * 100, ".2f"), "\n")

print("Profilaksi uygulaması için tedarik edilmesi gereken 4 haftalık toplam:","\n",
      "Plazma Kaynaklı Faktör-8 ilacı miktarı:",plazma_faktor8_mik, "ünite", "\n",
      "Toplam 1000'lik flakon sayısı:", p_hemA_faktor8_1000lik_flakon_say, "\n",
      "Toplam 500'lük flakon sayısı:", p_hemA_faktor8_500lük_flakon_say, "\n",
      "Toplam 250'lik flakon sayısı:", p_hemA_faktor8_250lik_flakon_say, "\n",
      sep=" ")

print("Profilaksi uygulaması için tedarik edilmesi gereken 4 haftalık toplam:","\n",
      "Plazma Kaynaklı Faktör-9 ilacı miktarı:",plazma_faktor9_mik, "ünite", "\n",
      "Toplam 1000'lik flakon sayısı:", p_hemB_faktor9_1000lik_flakon_say, "\n",
      "Toplam 500'lük flakon sayısı:", p_hemB_faktor9_500lük_flakon_say, "\n",
      "Toplam 250'lik flakon sayısı:", p_hemB_faktor9_250lik_flakon_say, "\n",
      sep=" ")

print("Profilaksi uygulaması için tedarik edilmesi gereken 4 haftalık toplam:","\n",
      "Rekombinant Faktör-8 ilacı miktarı:",rekom_faktor8_mik, "ünite", "\n",
      "Toplam 1000'lik flakon sayısı:", r_hemA_faktor8_1000lik_flakon_say, "\n",
      "Toplam 500'lük flakon sayısı:", r_hemA_faktor8_500lük_flakon_say, "\n",
      "Toplam 250'lik flakon sayısı:", r_hemA_faktor8_250lik_flakon_say, "\n",
      sep=" ")

print("Profilaksi uygulaması için tedarik edilmesi gereken 4 haftalık toplam:","\n",
      "Rekombinant Faktör-9 ilacı miktarları:",rekom_faktor9_mik, "ünite", "\n",
      "Toplam 1000'lik flakon sayısı:", r_hemB_faktor9_1000lik_flakon_say, "\n",
      "Toplam 500'lük flakon sayısı:", r_hemB_faktor9_500lük_flakon_say, "\n",
      "Toplam 250'lik flakon sayısı:", r_hemB_faktor9_500lük_flakon_say, "\n",
      sep=" ")

print("SGK’nın karşıladığı", "\n",
      "4 haftalık ilac tutarı:", format(top_aylık_ilac_tutarı,".2f"), "TL", "\n",
      "1 yıllık faktör ilacı tutarı:",format((top_aylık_ilac_tutarı * 12),".2f"), "TL", "\n",
      sep=" ")

print("SGK’nın profilaksi uygulaması kapsamında ortalama olarak 1 hasta için karşıladığı", "\n",
      "Yıllık toplam ilaç miktarı :", format((tüm_hasta_aylık_top_ilac * 12) / top_hasta_say,".2f"), "ünite", "\n",
      "Tutarı:",format((top_aylık_ilac_tutarı * 12) / top_hasta_say,".2f"),"TL","\n",
      sep=" ")

print("4 haftalık ilaç kullanım miktarı en çok olan Hemofili-A hastasının:", "\n",
      "TC kimlik numarası:", max_tc, "\n",
      "Ad ve soyadı: ", max_ad_soyad, "\n",
      "Hastalık şiddeti:", max_siddet, "\n",
      "Kilosu:", max_kilo, "KG", "\n",
      "Kullandığı ilaç türü (plazma kaynaklı/rekombinant):", max_ilac_türü, "\n",
      "4 haftalık toplam ilaç kullanım miktarı:", max_ilac_mik, "ünite", "\n",
      "4 haftalık toplam ilaç tutarı:", max_ilac_tutarı, "TL", "\n",
      sep=" ")

print("4 haftalık ilaç kullanım miktarı en çok olan Hemofili-B hastasının:", "\n",
      "TC kimlik numarası:", max_tc2, "\n",
      "Adı ve soyadı:", max_ad_soyad2, "\n",
      "Hastalığının şiddeti", max_siddet2, "\n",
      "Kilosu", max_kilo2,"KG","\n",
      "Kullandığı ilaç türü (plazma kaynaklı/rekombinant): ", max_ilac_türü2, "\n",
      "4 haftalık toplam ilaç kullanım miktarı:", max_ilac_mik2, "ünite", "\n",
      "4 haftalık toplam ilaç tutarı :", max_ilac_tutarı2, "TL", "\n",
      sep=" ")

print("4 haftalık ilaç tutarı en çok olan hastanın:", "\n",
      "TC kimlik numarası:", max_tc3, "\n",
      "Adı soyadı:", max_ad_soyad3, "\n",
      "Hastalığının tipi:", max_tip, "\n",
      "Şiddeti:", max_siddet3, "\n",
      "Kilosu:", max_kilo3, "KG""\n",
      "Kullandığı ilaç türü:", max_ilac_türü3, "\n",
      "4 haftalık toplam ilaç kullanım miktarı:", max_ilac_mik3, "ünite", "\n",
      "4 haftalık toplam ilaç tutarı:", max_ilac_tutarı3, "TL", "\n",
      sep=" ")