tanya_age = int(input("Введите возраст Тани: "))
mitya_age = int(input("Введите возраст Мити: "))
middle_age = (tanya_age + mitya_age) / 2
print("Их средний возраст: " + str(middle_age))
difference_tanya = (tanya_age - middle_age)
difference_mitya = (mitya_age - middle_age)
print("Возраст Тани отличается от среднего значения на: " + str(abs(difference_tanya)))
print("Возраст Мити отличается от среднего значения на: " + str(abs(difference_mitya)))

