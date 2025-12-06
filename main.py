# 1-mashq
docs = input("Hujjat topshirildimi? (ha/yo'q): ").lower()
interview = input("Suhbatdan o'tdimi? (ha/yo'q): ").lower()
test = input("Testdan o'tdimi? (ha/yo'q): ").lower()

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")
