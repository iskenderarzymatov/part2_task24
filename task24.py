text = input("Введите слово или текст: ")
list_text = list(text)
new_list_text = []                      # создаем список
for i in list_text:
    if i == " " or i == "\t":
        continue
    else:
        new_list_text.append(i)         # в список добавляем все символы кроме пробелов
print(new_list_text)

nop = 0
while len(new_list_text) > 1:                       # создаем цикл работает пока длина списка больше 1
    if new_list_text[0] == new_list_text[-1]:       # сравниваем крайние элементы если они равны
        del new_list_text[0]                        # удаляем
        del new_list_text[-1]                       # их
        continue
    else:
        print("Не палиндром.")
        nop += 1
        break
if nop == 0:                                        # печатаем "Палиндром" только если не печатали "Не палиндром"
    print("Палиндром")