#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Her Saniye Yanlış Atasözü Üreten Makine
Bu kod gerçekten çalışır. Her çalıştırdığında yeni bir saçmalık üretir.
Copilot ile konuştuk, o da şaşırdı.
"""

import random
import time

# Gizli siyasi gönderme: bazen çok derin, çok saklı
# (bir değişkenin içinde, kimse görmez)
gizli_mesaj = "bazen en iyi politika hiç politika yapmamaktır ama bunu söylemek de politikadır"  # saklı kalsın

def yanlis_atasozu_uret():
    baslangiclar = [
        "Acele işe",
        "Damla damla",
        "Kör kör",
        "Bir elin nesi var",
        "Komşu komşunun",
        "Akıllı düşman",
        "Sabır taşı",
        "Damlaya damlaya",
        "Köpek bile",
        "Yalancının mumu"
    ]
    
    sonlar = [
        "şeytan karışır ama bazen melek de karışır",
        "göl olur ama içine bir de kurbağa düşer",
        "körü bulur ama sonra ikisi de kaybolur",
        "iki elin sesi var ama üçüncü el nerede",
        "külüne muhtaç olur ama külü de bitmiştir",
        "cahil dosttan iyidir ama ikisi de aynı kişidir",
        "çatlar ama sonra yapışkan bantla düzelir",
        "göl olur ama göl çok tuzludur",
        "kuyruğunu sallar ama kuyruk başka köpeğindir",
        "yatsıya kadar yanar ama elektrik faturası gelir"
    ]
    
    return random.choice(baslangiclar) + " " + random.choice(sonlar) + "."

def main():
    print("\n=== HER SANİYE YANLIŞ ATASÖZÜ ÜRETEN MAKİNE ===")
    print("Başlatılıyor... (Ctrl+C ile durdurabilirsiniz, ama durdurmayın)")
    print("-" * 50)
    
    try:
        while True:
            atasozu = yanlis_atasozu_uret()
            print(f"[{time.strftime('%H:%M:%S')}] {atasozu}")
            time.sleep(1)  # her saniye, söz verdiğimiz gibi
    except KeyboardInterrupt:
        print("\nMakine durduruldu. Ama atasözleri hala yanlış.")
        print("Gizli mesajı merak ediyorsanız: kaynak koduna bakın, orada bir yerde saklı.")

if __name__ == "__main__":
    main()
