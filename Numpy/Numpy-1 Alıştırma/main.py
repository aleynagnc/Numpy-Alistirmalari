#Numpy-1 Alıştırma Ödevi
import numpy as np

#1) Manuel değerleri el ile girerek 3 boyutlu bir array oluşturup bir değişkene atayın. Ardından 3 boyutlu olup olmadığına bakmak için dimension'ını kontrol edin
arr3d= np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(arr3d)
boyut= arr3d.ndim
print(boyut)

#2) 34, 40, 46, 52... 112 şeklinde devam eden 1 boyutlu bir array oluşturun.
arr1d= np.arange(34,113,6)
print(arr1d)

#3) 50-500 arasında lineer artış gösteren 91 tane tam sayıdan oluşan bir array oluşturun.(dtype'ı int olsun)
arrlin = np.linspace(50,500,91, dtype=int)
print(arrlin)

#4) 100(10**2) ile 10000(10**5) arasında logaritmik artış gösteren 8 sayıdan oluşan bir array oluşturun.
arrlog= np.logspace(2, 5, 8 )
print(arrlog)

#5) 0-8 tam arasındaki ardışık tam sayılardan oluşan(0 ve 8 dahil toplam 9 değer) 3x3 shape'inde bir matris oluşturun.
arr2d= np.arange(0,9).reshape(3,3)
shp = arr2d.shape
print(arr2d)
print(shp)

#6) 6x6 formatında bir sıfır matrisi oluşturun. (dtype'ı int olsun)
matrx = np.zeros((6,6), dtype=int)
print(matrx)

#7) 4x4 formatında bir bir matrisi oluşturun. (dtype'ı int olsun)
matrx1 = np.ones((4,4), dtype=int)
print(matrx1)

#8) 8x8 formatında bir birim matris oluşturun. (Sadece sol köşegeni 1 geri kalan değerleri 0 olan matris'e birim matris deniyor.) (dtype'ı int olsun)
birimtrx= np.eye(8, dtype=int) 
print(birimtrx)

#9) 5x5 formatında bir köşegen matrisi oluşturun (Sadece sol üstten sağ alta doğru olan köşegendeki değerleri 3 olsun diğer bütün değerleri 0) (Bunu henüz görmediniz ama birim matrise benziyor, sadece köşegen değerleri 1 değil 3 olacak. Bir şeyler düşünün)
kosgnmtrx = np.eye(5, dtype=int)*3
print(kosgnmtrx)

#10) np.random modülünden uygun fonksiyonu kullanarak 0-1 arasında toplam 6 tane değerden oluşan 1 boyutlu bir array oluşturun.
rndm = np.random.rand(6)
print(rndm)

#11) np.random modülünden uygun fonksiyonu kullanarak 50-100 arasındaki(50 ve 100 dahil) tam sayılardan 10 tanesiyle oluşan (5,2) shape'inde bir array oluşturun. Ardından bu arrayin shape'ini kontrol edin.
arr = np.random.randint(50,101,10).reshape(5,2)
print(arr)
x = arr.shape
print(x)

#12) np.random modülünden uygun fonksiyonu kullanarak 100-1000(1000 dahil değil) arasındaki tam sayılardan rastgele 50 tanesinden oluşan (2,5,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in dimension'ını(boyutunu) ve shape'ini kontrol edin.
arry = np.random.randint(100,1000,50).reshape(2,5,5)
print(arry)
boyut2 = arry.ndim
print(boyut2)
shape2 = arry.shape
print(shape2)

#13) np.random modülünden uygun fonksiyonu kullanarak 0-100(0 ve 100 dahil) arasındaki tam sayılardan 10 tane seçerek bir array oluşturun. Bu array'in maximum, mininmum değerlerine ve bu değerlerin indexlerine bakın.
rndmarr = np.random.randint(0,101,10)
print(rndmarr)
rndmarrmax = rndmarr.max()
print(rndmarrmax)
rndmarrmaxindex = rndmarr.argmax()
print(rndmarrmaxindex)
rndmarrmin = rndmarr.min()
print(rndmarrmin)
rndmarrminindex = rndmarr.argmin()
print(rndmarrminindex)

#14) np.random modülünden uygun fonksiyonu kullanarak 300-500(300 ve 500 dahil) arasındaki tam sayılardan 20 tane seçerek (2,2,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in içindeki 20 tam sayı arasından maximum ve minimum değerleri manuel olarak tespit edin ve indexleme yaparak çekmeye çalışın.
rndm1 = np.random.randint(300,501,20).reshape(2,2,5)
print(rndm1)
indeks = rndm1[1][1][4]
print(indeks)

#15) 0-50(50 dahil) arasındaki ardışık tam sayılardan oluşan bir array oluşturun. Ardından bu arrayin 20. ve 35. indexleri arasındaki değerleri 500'e eşitleyin ve yeni oluşan array'i ekrana yazdırarak broadcasting işleminin yapılıp yapılmadığını test edin.
arr1 = np.arange(0,51,1)
print(arr1)
arr1[20:36] = 500
print(arr1)