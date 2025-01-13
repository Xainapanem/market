from logging import exception


class Product:
    def __init__(self, article, name, cost, number):
        self.article = article
        self.name = name
        self.cost = cost
        self.number = number

    @staticmethod
    def add_product():
        print("Введите характеристики нового товара")
        flag = True
        while flag:
            flag = False
            article = int(input("Артикул:"))
            Product.check_num(article)
            for i in all_products:
                if article == i.article:
                    print("Товар с таким артикулом уже существует!")
                    flag = True
        name = input("Название:")
        cost = int(input("Стоимость:"))
        Product.check_num(cost)
        number = int(input("Количество:"))
        Product.check_num(number)
        new_product = Product(article, name, cost, number)
        all_products.append(new_product)
        main_menu()

    @staticmethod
    def change_product():
        change_pr_article = int(input("Введите артикул товара, характеристики которого хотите изменить:"))
        Product.check_num(change_pr_article)
        print(
            "Выберите какую характеристику товара вы хотите изменить:\n1 - Изменить артикул\n2 - Изменить название\n3 - Изменить количество\n4 - Изменить стоимость\n5 - Изменить все характеристики")
        var = int(input())
        for i in all_products:
            if change_pr_article == i.article:
                if var == 1:
                    flag = True
                    while flag:
                        flag = False
                        change_art = int(input("Изменить артикул " + str(i.article) + " на:"))
                        Product.check_num(change_art)
                        for i in all_products:
                            if change_art == i.article:
                                print("Товар с таким артикулом уже существует!")
                                flag = True
                        if not flag:
                            print("Артикул товара успешно изменен с", i.article, "на", change_art)
                            i.article = change_art

                elif var == 2:
                    change_name = input("Изменить имя товара с " + i.name + " на:")
                    print("Имя товара изменено с", i.name, "на", change_name)
                    i.name = change_name

                elif var == 3:
                    change_number = int(input("Изменить количество товара с" + str(i.number) + " на:"))
                    Product.check_num(change_number)
                    print("Количество товара изменено с", i.number, "на", change_number)
                    i.number = change_number

                elif var == 4:
                    change_cost = int(input("Изменить стоимость товара с " + str(i.cost) + " на:"))
                    Product.check_num(change_cost)
                    print("Стоимость товара изменена с", i.cost, "на", change_cost)
                    i.number = change_cost

                elif var == 5:
                    flag = True
                    while flag:
                        flag = False
                        change_art = int(input("Изменить артикул " + str(i.article) + " на:"))
                        Product.check_num(change_art)
                        for i in all_products:
                            if change_art == i.article:
                                print("Товар с таким артикулом уже существует!")
                                flag = True
                        if not flag:
                            print("Артикул товара успешно изменен с", i.article, "на", change_art)
                            i.article = change_art

                    change_name = input("Изменить имя товара с " + i.name + " на:")
                    print("Имя товара изменено с", i.name, "на", change_name)
                    i.name = change_name

                    change_number = int(input("Изменить количество товара с" + str(i.number) + " на:"))
                    Product.check_num(change_number)
                    print("Количество товара изменено с", i.number, "на", change_number)
                    i.number = change_number

                    change_cost = int(input("Изменить стоимость товара с " + str(i.cost) + " на:"))
                    Product.check_num(change_cost)
                    print("Стоимость товара изменена с", i.cost, "на", change_cost)
                    i.number = change_cost
                else:
                    print("Такой вариант отсутвует в списке!")
                    Product.change_product()

                break

        main_menu()

    @staticmethod
    def check_num(somenum):
        if somenum < 0:
            print("Введено несуществующее числовое значение!")
            return main_menu()

    @staticmethod
    def delete_product():
        del_prod_art = int(input("Введите артикул товара, который вы хотите удалить из каталога:"))
        for i in all_products:
            if del_prod_art == i.article:
                print("Товар с артикулом", del_prod_art, "удален.")
                all_products.remove(i)
                main_menu()
        print("Товара с таким артикулом не найдено!")
        main_menu()


def cr_table():
    max_len = 0
    flag = True
    for i in all_products:
        if len(i.name) >= 15 and len(i.name) > max_len:
            max_len = len(i.name)
            if flag:
                flag = False
        elif flag:
            maxi = max(len(str(i.article)), len(i.name), len(str(i.cost)), len(str(i.number)))
            if maxi > max_len:
                if maxi < 15:
                    max_len = maxi
                else:
                    max_len = 15

    print('-' * (max_len + 83))
    print("Артикул", "Название" + ' ' * max_len + "Стоимость", "Количество", '|', sep=' ' * 16)
    print('-' * (max_len + 83))

    for i in all_products:

        if len(str(i.article)) > 15:
            article = str(i.article)[0:15] + "..."
        else:
            article = str(i.article)

        if len(str(i.cost)) > 15:
            cost = str(i.cost)[0:15] + "..."
        else:
            cost = str(i.cost)

        if len(str(i.number)) > 15:
            number = str(i.number)[0:15] + "..."
        else:
            number = str(i.number)

        print(article + ' ' * (7 - len(article) + 15), i.name + ' ' * (8 - len(i.name) + max_len - 1),
              cost + ' ' * (9 - len(cost) + 15), number + ' ' * (10 - len(number) + 15), '|')
        print('-' * (max_len + 83))


def main_menu():
    if len(all_products) > 0:
        cr_table()
    print("МЕНЮ\n1 - Добавить товар\n2 - Изменить характеристики товара\n3 - Удалить товар\n4 - Экспорт/Импорт каталога\n5 - Выйти из программы")
    var = int(input())
    if var == 1:
        Product.add_product()
    elif var == 2:
        if len(all_products) != 0:
            Product.change_product()
        else:
            print("В каталоге отсутствуют товары!")
            Product.main_menu()
    elif var == 3:
        if len(all_products) != 0:
            Product.delete_product()
        else:
            print("В каталоге отсутствуют товары!")
            main_menu()
    elif var == 4:
        print("1 - Импортировать данные из файла\n2 - Экспортировать данные в файл")
        try:
            var_imex = int(input())
        except ValueError:
            print("Введено неверное значение!")
            main_menu()
        else:
            if var_imex == 1:
                file_import()
            elif var_imex == 2:
                file_export()
            else:
                print("Введено неверное значение!")
                main_menu()
    elif var == 5:
        return 0
    else:
        print("Введено неверное значение!")
        main_menu()


def file_import():
    with open("text.txt", 'r') as file:
        for line in file:
            doc_info = line
    if len(line) != 0:
        name = article = cost = number = ''
        now_decoding = 0
        for i in line:
            if i == '^':
                now_decoding = 1
            elif i == '<':
                now_decoding = 2
            elif i == '>':
                now_decoding = 3
            elif i == '|':
                now_decoding = 4
            elif i == '~':
                product = Product(name = name,  article = int(article), cost = int(cost), number = int(number))
                all_products.append(product)
                name = article = cost = number = ''
                now_decoding = 0

            if not(i == '^' or i == '<' or i == '>' or i == '|' or i == '~'):
                match now_decoding:
                    case 1:
                        name += i
                    case 2:
                        article += i
                    case 3:
                        cost += i
                    case 4:
                        number += i

    main_menu()
def file_export():
    with open("text.txt", 'w') as file:
        for i in all_products:
            file.write('^' + i.name + '<' + str(i.article) + '>' + str(i.cost) + '|' + str(i.number) + '~')
    main_menu()


all_products = []
main_menu()
