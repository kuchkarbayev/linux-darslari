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
