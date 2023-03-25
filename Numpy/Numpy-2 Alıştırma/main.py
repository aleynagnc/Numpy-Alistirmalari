import numpy as np

#1) 0-29 arası(29 dahil, toplam 30 tam sayı) tam sayılardan oluşan bir boyutlu bir array oluşturun ardından bu array'in shape'ini (15,2) şeklinde güncelleyip 2 boyutlu hale getirin.
arr=np.arange(30)
print(arr)
arrshape = arr.reshape(15,2)
print(arrshape)

#2) 60 adet rastgele tam sayı verilerinden oluşan bir boyutlu bir array oluşturun. Devamında bu array'i istediğiniz shapelerde 3 boyutlu hale getirin ve son durumda oluşan array'in boyutunu ve shape'ini kontrol edin.
arr2 = np.random.randint(0,100,60)
print(arr2)
arr2shape = arr2.reshape(4,5,-1)
print(arr2shape)
boyut = arr2shape.ndim
print(boyut)
shape = arr2shape.shape
print(shape)

#3) 20 elemanlı ve sadece rakamlardan oluşan iki boyutlu bir array oluşturun. Ardından bu array'i düzleştirin ve tek boyutlu hale getirin ve son durumda oluşan array'in boyutunu ve shape'ini kontrol edin.
arr2d= np.arange(20, dtype = int).reshape(4,5)
print(arr2d)
duzlestir = arr2d.reshape(-1)
print(duzlestir)
boyut2 = duzlestir.ndim
print(boyut2)
shape2 = duzlestir.shape
print(shape2)

#4) İstediğiniz herhangi elemanlardan oluşan 2 Boyutlu bir array oluşturun. Oluşturduğunuz bu 2 boyutlu array'in içindeki bütün elemanları hem yavaş yol olan for döngüsüyle hem de daha hızlı yol olan uygun NumPy metoduyla tek tek dönerek ekrana yazdırın.
arr2dd = np.random.randint(2,50,20).reshape(4,-1)
print(arr2dd)
for x in arr2dd:
    for y in x:
        print(y)
for x in np.nditer(arr2dd):
    print(x)       

#5) 5,10,15,20,25,30 değerlerinden oluşan bir boyutlu bir array ve 1,2,3,4,5,6 değerlerinden oluşan başka bir boyutlu bir array oluşturun. Bu arraylerinin elemanlarına kendi aralarında 4 işlem uygulayın. İki arrayinde 1.indexindekiler toplansın/çıkartılsın/çarpılsın/bölünsün gibi.
arr3 = np.arange(5, 31, 5)
print(arr3)
arr4 = np.arange(1, 7)
print(arr4)
toplama = arr3 + arr4
print(toplama)
cikarma = arr3 - arr4
print(cikarma)
carpma = arr3 * arr4
print(carpma)
bolme = arr3 / arr4
print(bolme)

#6) 0-100 arası rastgele 10 tam sayıdan oluşan bir array oluşturun ve oluşturulan arrayin sum/mean/max/var/std değerlerini inceleyin.
arr5 = np.random.randint(0,100,10)
print(arr5)
print(arr5.sum())
print(arr5.mean())
print(arr5.max())
print(arr5.var())
print(arr.std())

#7) 0-20 arası(20 dahil değil) tam sayılardan oluşan ve 500-530(530 dahil) arası tam sayılardan oluşan 2 array oluşturun. Ardından bu iki array'i concatenate ederek ekrana yazdırın.
arr6 = np.arange(0,20)
print(arr6)
arr7 = np.arange(500,531)
print(arr7)
concat = np.concatenate([arr6,arr7])
print(concat)

#8) 15-50(50 dahil) arası tam sayılardan oluşan bir array oluşturun. Daha sonra 10-100 arası(100 dahil) tam sayılardan oluşan 2.bir array oluşturun. Bu 2 arrayi concatanate ederek 3.bir array oluşturun ve bu array'in 25.index ile 50.index'i(50 dahil) arasındaki değerlerini 888 yapın.
arr8 = np.arange(15,51)
print(arr8)
arr9 = np.arange(10,101)
print(arr9)
concant2 = np.concatenate([arr8,arr9])
print(concant2)
concant2[25:51]=888
print(concant2)

#9) 0-40(40 dahil değil) arası değerlerden oluşan (8,5) shape'inde 2 boyutlu bir array ve  320-360(360 dahil değil) değerlerinden oluşan (8,5) shape'inde 2 boyutlubaşka bir array oluşturun. Devamında bu iki array'i hem axis = 0'da hem de axis = 1'de concatenate ederek farkı karşılaştırın.
arr10 = np.arange(40).reshape(8,5)
print(arr10)
arr11= np.arange(320,360).reshape(8,5)
print(arr11)
concat3 = np.concatenate([arr10,arr11],axis=0)
print(concat3)
concat4 = np.concatenate([arr10,arr11],axis=1)
print(concat4)

#10) 9.Soruda oluşturduğunuz 2 array'i axis = 2'de concatenate etmeye çalışın. Ardından axis = 2'de stacklemeye(yığınlamaya) çalışın. İkisi arasındaki farkı karşılaştırın.
'''concat5 = np.concatenate([arr10,arr11],axis =2)
print(concat5)
stack1 = np.stack([arr10,arr11], axis=2)
print(stack1)'''

#11) [1, 20, 25, 4, 4, 5, 4, 4, 1, 6, 9, 12, 1, 5] değerlerinden oluşan bir boyutlu bir array oluşturun. Devamında bu array'in içinde değeri 5'e eşit olan değerlerin indexleri bulun.
arr12 = np.array([1, 20, 25, 4, 4, 5, 4, 4, 1, 6, 9, 12, 1, 5])
indeks = np.where(arr12 == 5)
print(indeks)

#12) Yukarıda oluşturduğunuz array içinde değeri çift olan değerlerin indexlerini bulun.
indeks2 = np.where(arr12%2==0)
print(indeks2)

#13) Yukarıda oluşturduğunuz array içinde değeri 4'den büyük olan değerlerin indexlerini bulun.
indeks3 = np.where(arr12 > 4)
print(indeks3)

#14) Yukarıda oluşturduğunuz array içinde değeri 5'e tam bölünen değerlerin indexlerini bulun.
indeks4 = np.where(arr12%5==0)
print(indeks4)

#15) 85-100(100 dahil) arasından rastgele 1 tam sayı seçin
rast = np.random.randint(85,101,1)
print(rast)

#16) İki basamaklı tam sayılar arasından rastgele sayılar seçerek (3,3) shape'inde bir array oluşturun.
arr13 = np.random.randint(0,100,9).reshape(3,3)
print(arr13)

#17) 35-60 arasındaki tam sayılardan bir array oluşturun, ardından bu array içinden rastgele 1 tam sayı seçin.
rast2 = np.arange(35,61)
print(rast2)
arr14 = np.random.choice(rast2,1)
print(arr14)

#18) Sadece [3, 8, 10, 53] değerlerinden oluşan (2,5) shape'inde 2 boyutlu bir array oluşturun.
arr15 = np.random.choice([3,8,10,53], size=(2,5))
print(arr15)
