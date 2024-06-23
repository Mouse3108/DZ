# Создайте приложение для эмуляции работа киоска по продаже хот-догов.
# Приложение должно иметь следующую функциональность:
# 1. Пользователь может выбрать из трёх стандартных рецептов хот-дога или создать свой рецепт.
# 2. Пользователь может выбирать добавлять ли майонез, горчицу, кетчуп,
# топинги (сладкий лук, халапеньо, чили, соленный огурец и т.д.).
# 3. Информацию о заказанном хот-доге нужно отображать на экран и сохранять в файл.
# 4. Если пользователь заказывает от трёх хот-догов нужно предусмотреть скидку.
# Скидка зависит от количества хот-догов.
# 5. Расчет может производиться как наличными, так и картой.
# 6. Необходимо иметь возможность просмотреть количество проданных хот-догов, выручку, прибыль.
# 7. Необходимо иметь возможность просмотреть информацию о наличии компонентов для создания хот-дога.
# 8. Если компоненты для создания хот-догов заканчиваются нужно вывести информационное сообщение
# о тех компонентах, которые требуется приобрести.
# 9. Классы приложения должны быть построены с учетом принципов SOLID и паттернов проектирования.

from DZcontroller import Controller


def main():
    app = Controller()
    app.run()


if __name__ == '__main__':
    main()
