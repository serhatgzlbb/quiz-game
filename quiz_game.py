print("Genel Kültür Sınavına Hoşgeldin!")
playing = input("Sınava başlamak istiyor musun? ")
if playing.lower() != "evet":
    quit()
print("Haydi! Başlayalım:)")

score = 0

answer_1 = input("Sinekli Bakkal romanının yazarı kimdir? ")
if answer_1.lower() == "halide edip adıvar":
    print("Doğru!")
    score += 1
else:
    print("Yanlış!")

answer_2 = input("Mustafa Kemal Atatürk’ün nüfusa kayıtlı olduğu il hangisidir? ")
if answer_2.lower() == "gaziantep":
    print("Doğru!")
    score += 1
else:
    print("Yanlış!")

answer_3 = input("Magna Carta hangi ülkenin kralıyla yapılmış bir sözleşmedir? ")
if answer_3.lower() == "ingiltere":
    print("Doğru!")
    score += 1
else:
    print("Yanlış!")

answer_4 = input("ABD başkanlarından John Fitzgerald Kennedy’e suikast düzenleyerek öldüren kimdir? ")
if answer_4.lower() == "lee harvey oswald":
    print("Doğru!")
    score += 1
else:
    print("Yanlış!")

print(f"{score} soruya doğru cevap verdin!")
percentage_score = int((score / 4) * 100)
print(f"%{percentage_score} doğru cevapladın.")
