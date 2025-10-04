#!/bin/bash

# 2-dars uyga vazifasi: "Meta Script"
# 1. generated_script.sh faylini yaratish

cat << 'EOF' > generated_script.sh
#!/bin/bash

# 1. myile.txt yaratamiz va unga matlarni qo'shib olamiz

echo "Bu birinchi qator" > myfile.txt
echo "Bu ikkinchi qator" >> myfile.txt
echo "Bu error log bor qator" >> myfile.txt

#2. "Error" larni qidirish (grep va piping bilan)
echo "=== ERROR loglar ==="
grep "error" myfile.txt |sort

#3.Errorlarni  sorted_file.txt ga yozish
sort myfile.txt >>  sorted_file.txt

#3. sorted_file.txt ga o'qish ruxsatini beramiz
chmod 444 sorted_file.txt
EOF

#2. generated_script.sh scriptiga run qilish huquqini beramiz
chmod 777 generated_script.sh

#3. generated_script.sh ni run qilamiz
./generated_script.sh

#4. Teskshiramiz narijani

if [ -e "myfile.txt" ] && [ -e "sorted_file.txt" ]; then
	echo "Fayillar yaratildi"
else
	echo "Fayillar yaratilmagan."
fi
