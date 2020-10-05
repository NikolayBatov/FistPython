def create_user(fist_name, last_name, year_birth, live_city, email, phone_number):
    print(f"{fist_name} {last_name} {year_birth} {live_city} {email} {phone_number}")


fist_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
year_birth = input("Введите год рождения: ")
live_city = input("Введите город проживания: ")
email = input("Введите email: ")
phone_number = input("Введите номер телефона: ")

create_user(fist_name=fist_name,
            last_name=last_name,
            year_birth=year_birth,
            live_city=live_city,
            email=email,
            phone_number=phone_number)
