Tanya = int(input("Введите возраст Тани: "))
Mitya = int(input("Введите возраст Мити: "))
average_age = (Tanya + Mitya)/2
print("Их средний возраст: " + str(average_age))
difference_Tanya = (Tanya - average_age)
difference_Mitya = (Mitya - average_age)
print("Возраст Тани отличается от среднего значения на: " + str(abs(difference_Tanya)))
print("Возраст Мити отличается от среднего значения на: " + str(abs(difference_Mitya)))
