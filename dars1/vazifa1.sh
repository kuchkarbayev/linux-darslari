#!/bin/bash
# ================================================
echo "==== Linux darslar | Uyga vazifa 1 ===="

# ================================================

echo "==== 1-topshiriq: Operatsion tizim va distributiv haqida to‘liq ma’lumot ===="


# Bu buyruq operatsion tizim yadrosi va arxitekturasi haqida umumiy ma'lumot beradi.
# -a parametri (all) barcha mavjud ma'lumotlarni chiqaradi:
#  kernel nomi, host nomi, kernel versiyasi, kompilyatsiya sanasi,
#  mashina arxitekturasi va boshqalar...
uname -a

# Bu buyruq Linux distributivi haqida ma'lumot beradi.
# -a parametri (all) distributiv nomi, versiyasi, kod nomi va ishlab chiqaruvchini chiqaradi.
lsb_release -a

# ================================================


# ================================================

echo "==== 2-topshiriq: Hozirgi foydalanuvchi nomini chiqarish ===="
# whoami buyrug'i tizimga login qilgan foydalanuvchi nomini chiqaradi
whoami
# yoki xuddi shu natijani o'zgaruvchi orqali olish mumkin:
# $USER - bu tizim tomonidan avtomatik beriladigan muhit o'zgaruvchisi
echo $USER 

# ================================================


# ================================================

echo "==== 3-topshiriq: SKIP ===="
# 3. `ls` buyrug'i haqidagi dokumentatsiyani 3 xil ko'rinishda chiqaring:
# 1-usul: man sahifasi
# "man ls" - buyrug'i "manual page"ni ochadi.
# U yerda ls haqida to'liq ma'lumot, parametrlar, misollar bor.
#man ls

# 2-usul: info sahifasi
# "info ls" - buyrug'i GNU info hujjatini ochadi.
# Bu yerda qo'shimcha izohlar va interaktiv tarzda ko'rsatmalar beriladi.
#info ls

# 3-usul: --help opsiyasi
# "ls --help" - buyrug'i qisqa yordam chiqaradi.
# Asosiy flag va opsiyalarni tez ko'rib chiqish uchun qulay.
#ls --help

# ================================================


# ================================================

echo "==== 4-topshiriq: yangi papka yaratish va unga o‘tish ===="
# 4. "uygavazifa" nomli yangi papka yarating.
# Keyin shu papkaga o‘ting va qolgan ishlarni shu yerda davom ettiring.

# mkdir - buyrug'i yangi papka yaratadi
# "uygavazifa" - yaratiladigan papka nomi
mkdir uygavazifa

# "uygavazifa" papkasiga kirish
# cd-buyrug'i katalogni o'zgartiradi (change directory)
cd uygavazifa
# hozirgi joylashuvni tekshirish uchun:
# (print working directory)
pwd  

# ================================================


# ================================================

echo "==== 5-topshiriq: uchta matnli fayl yaratish ===="
# 5. Papka ichida uchta matnli fayl yarating.
#    - Yordam: matn yozish uchun `echo "matn" > faylnomi.txt` yoki `echo "matn" >> faylnomi.txt` dan foydalanishingiz mumkin.
#    - 1-fayl: o‘zingiz haqida bir necha qatorli qisqa matn yozing
#    - 2-fayl: sevimli kitobingiz yoki film nomini yozing
#    - 3-fayl: bugungi sanani yozing. `date` buyrug'idan foydalaning sanani ko'rsatish uchun.

echo "Ismim Ahrorbek, QA siftida Raqamli transport markazida faoliyat yuritaman" > 1-fayl.txt
echo "Sevimli kitobim Asqad Muhtorning Chinor romani. Sevimli filimim esa Yuldirzlar jangi (Star wars)" > 2-fayl.txt

# date buyrug'i o'zi natija chiqaradi, shuning uchun uni to'g'ridan-to'g'ri faylga yo'naltirish (>) kifoya qiladi
# Lekin agar izohli sana yozish uchun echo bilan ishlatish, date buyrug'ining natijasini qo'shib yuborishingiz kerak bo'ladi
echo "Bugungi sana: $(date)" > 3-fayl.txt

# ================================================


# ================================================

echo "==== 6-topshiriq: papkadagi fayllarni ko‘rsatish ===="
# 6. Papkada qanday fayllar mavjudligini ko‘rsating.
# ls buyrug'i katalog ichidagi fayllar va papkalarni ro'yxatlab ko'rsatadi
ls
# 1-fayl.txt  2-fayl.txt  3-fayl.txt
# qo'shimcha: fayllar haqida batafsil ma'lumot (hajmi, sana, huquqlar) uchun:
ls -l
# .  ..  1-fayl.txt  2-fayl.txt  3-fayl.txt
# qo'shimcha: yashirin fayllarni ham ko'rsatish uchun:
ls -a
# total 12
# -rw-rw-r-- 1 akhrorbek akhrorbek 74 Oct  2 08:14 1-fayl.txt
# -rw-rw-r-- 1 akhrorbek akhrorbek 97 Oct  2 08:17 2-fayl.txt
# -rw-rw-r-- 1 akhrorbek akhrorbek 43 Oct  2 08:20 3-fayl.txt

# ================================================


# ================================================

echo "==== 7-topshiriq: fayldan nusxa olish ===="
# 7. Birinchi faylni nusxa ko'chiring va yangi 'new_file.txt' nom bering.
# cp buyrug'i faylni nusxa ko'chiradi
# cp [manba_fayl] [yangi_fayl]
cp 1-fayl.txt new_file.txt

# ================================================


# ================================================

echo "==== 8-topshiriq: fayl nomini o‘zgartirish ===="
# 8. Ikkinchi fayl nomini 'renamed_file.txt' nomga o'zgartiring.
# mv buyrug'i faylni ko'chirish yoki nomini o'zgartirish uchun ishlatiladi
# Sintaksis: mv eski_fayl yangi_fayl
mv 2-fayl.txt renamed_file.txt

# ================================================


# ================================================

echo "==== 9-topshiriq: faylni o‘chirish va yo‘qligini tekshirish ===="
# 9. Uchinchi faylni o'chirib tashlang va yo'qligini isbotlang.
# rm buyrug'i faylni o'chiradi
# -v (verbose) nima amal bajarilganini ekranga chiqaradi
rm -v 3-fayl.txt
#removed '3-fayl.txt'
# Endi fayllarni qayta ko'rsatib, fayl o'chganini isbotlaymiz
ls -l
# total 12
# -rw-rw-r-- 1 akhrorbek akhrorbek 74 Oct  2 08:14 1-fayl.txt
# -rw-rw-r-- 1 akhrorbek akhrorbek 74 Oct  2 08:28 new_file.txt
# -rw-rw-r-- 1 akhrorbek akhrorbek 97 Oct  2 08:17 renamed_file.txt
# ================================================


# ================================================

echo "==== 10-topshiriq: faylni oddiy va teskari chiqarish (o'qish) ===="
# 10. Birinchi fayldagi matnni oddiy ko'rinishda va teskari ko'rinishda ekranga chiqaring.
# 1-faylga 2-satr qo'shib oldim 
# >> eski matnni saqlab, yangisini oxiriga qo'shadi.
echo "10 topshiriq uchun" >> 1-fayl.txt

# Faylni oddiy ko'rinishda chiqarish
cat 1-fayl.txt
# Ismim Ahrorbek, QA siftida Raqamli transport markazida faoliyat yuritaman
# 10 topshiriq uchun

# Faylni teskari ko'rinishda chiqarish
tac men.txt
# 10 topshiriq uchun
# Ismim Ahrorbek, QA siftida Raqamli transport markazida faoliyat yuritaman

# ================================================



# ================================================

echo "==== 11-topshiriq: papkas yaratish va o‘chirish ===="
# 11. "sinov" nomli yangi papka yarating, keyin uni o'chirib tashlang.
# papka yaratamiz
mkdir sinov

# hech qanday ogohlantirishsiz o'chirib tashlaydi
# -r (recursive) papkani ichidagi barcha fayllar va ichki papkalar bilan birga o'chiradi.
# -f (force) xatoliklar va ogohlantirishlarni ko'rsatmasdan, majburan o'chiradi.
rm -rf -v sinov

# xavfsizroq varianti -i har bir faylni o'chirishdan oldin so'raydi     
rm -rvi sinov 

# rm: remove directory 'sinov'? yes
# removed directory 'sinov'

# ================================================



# ================================================

echo "==== 12-topshiriq: papkalar ustida amallar ===="
# 12. Topshiriq:
#     - "katta" nomli papka yarating.
#     - uning ichida "kichik" nomli papka yarating.
#     - "kichik" papka ichiga yangi bo'sh fayl yarating
#     - butun "katta" papkani boshqa joyga nusxalab o‘tkazing.
#     - keyin asl "katta" papkani ichidagi barcha narsasi bilan birga butunlay o‘chirib tashlang.
#     - oxirida nusxa olingan joyda papka va fayl mavjudligini tekshiring.

# "katta" nomli papka yaratamiz
mkdir katta

# "katta" ichida "kichik" papka yaratamiz
mkdir katta/kichik

# "kichik" ichida yangi bo'sh fayl yaratamiz
touch katta/kichik/bosh_fayl.txt

# cp - nusxa olish buyrug'i
# -r - rekursiv (ichidagi barcha papka va fayllarni ham oladi)
# ~/uygavazifa/katta - asl papkaning to'liq yo‘li
# ~/1-dars/ - nusxa tushadigan manzil
cp -r ~/uygavazifa/katta ~/1-dars/

rm -rf -v ~/uygavazifa/katta

# removed '/home/akhrorbek/uygavazifa/katta/kichik/bosh_fayl.txt'
# removed directory '/home/akhrorbek/uygavazifa/katta/kichik'
# removed directory '/home/akhrorbek/uygavazifa/katta

# nusxa olingan joyda papka va fayl mavjudligini tekshirish
# ls - papkadagi fayllarni ko'rsatadi.
# -R - rekursiv, ya'ni ichki papka va fayllarni ham ko'rsatadi.
# ~/1-dars/katta - nusxa olingan papka manzili.
ls -R ~/1-dars/katta

# Natija:
# /home/akhrorbek/1-dars/katta:
# kichik

# /home/akhrorbek/1-dars/katta/kichik:
# bosh_fayl.txt

# ================================================


# ================================================

echo "==== ✅ Barcha topshiriqlar muvaffaqiyatli bajarildi! ===="

# ================================================
