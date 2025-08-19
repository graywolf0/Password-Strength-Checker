# password_strength_checker.py
# Author: Graywolf0
# 📌 Educational Project - For Portfolio Use

import re

def check_password_strength(password):
    strength_points = 0

    # Uzunluk kontrolü
    if len(password) >= 8:
        strength_points += 1

    # Büyük harf kontrolü
    if re.search(r"[A-Z]", password):
        strength_points += 1

    # Küçük harf kontrolü
    if re.search(r"[a-z]", password):
        strength_points += 1

    # Sayı kontrolü
    if re.search(r"[0-9]", password):
        strength_points += 1

    # Özel karakter kontrolü
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    # Şifre sınıflandırma
    if strength_points <= 2:
        return "Weak 🔴"
    elif strength_points == 3 or strength_points == 4:
        return "Medium 🟡"
    else:
        return "Strong 🟢"


if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_password = input("Enter a password to check: ")
    result = check_password_strength(user_password)
    print(f"Password Strength: {result}")
