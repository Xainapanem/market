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
                    change_product()

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

def main_menu():
    if len(all_products) > 0:
        cr_table()
    print("МЕНЮ\n1 - Добавить товар\n2 - Изменить характеристики товара\n3 - Удалить товар\n")
    var = int(input())
    if var == 1:
        Product.add_product()
    if var == 2:
        if len(all_products) != 0:
            Product.change_product()
        else:
            print("В каталоге отсутствуют товары!")
            Product.main_menu()
    if var == 3:
        if len(all_products) != 0:
            Product.delete_product()
        else:
            print("В каталоге отсутствуют товары!")
            main_menu()
    else:
        print("Введено неверное значение!")
        main_menu()

def cr_table():
    print('-'*75)
    print("Артикул", "Название", "Стоимость", "Количество", '|', sep=' ' * 10)
    print('-'*75)
    for i in all_products:
        print(str(i.article) + ' ' * (7 - len(str(i.article)) + 9), i.name + ' ' * (8 - len(str(i.name)) + 9),
              str(i.cost) + ' ' * (9 - len(str(i.cost)) + 9), str(i.number) + ' ' * (10 - len(str(i.number)) + 9), '|')
        print('-'*75)

all_products = []
main_menu()
