import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        # Инициализация списка товаров и словарей с ценами и налогами
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def get_total_price(self):
        """Считает общую стоимость товаров без учета скидки"""
        total = 0
        for item in self.__name_items:
            total += self.__item_price[item]
        return total

    def get_total_tax(self):
        """Считает общую сумму налога"""
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    def check_amount(self):
        """Считает итоговую сумму с учетом скидки 10% при покупке >10 товаров"""
        total = self.get_total_price()
        if self.__number_items > 10:
            total = total * 0.9
        return total

    def twenty_percent_tax_calculation(self):
        """Расчет налога для товаров с 20% ставкой"""
        twenty_percent_tax = []
        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        
        total = 0
        for item in twenty_percent_tax:
            total += self.__item_price[item]
            
        if self.__number_items > 10:
            total = total * 0.9
        return total * 0.2

    def ten_percent_tax_calculation(self):
        """Расчет налога для товаров с 10% ставкой"""
        ten_percent_tax = []
        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                
        total = 0
        for item in ten_percent_tax:
            total += self.__item_price[item]
            
        if self.__number_items > 10:
            total = total * 0.9
        return total * 0.1  

    def get_total_with_tax(self):
        """Возвращает итоговую сумму с налогом (использует check_amount вместо несуществующего get_total_price)"""
        return self.check_amount() + self.total_tax()

    def print_receipt(self):
        print("Чек:")
        for item in self.__name_items:
            print(f"{item}: {self.__item_price[item]} руб.")
        print(f"Итого без налога: {self.check_amount()} руб.")
        print(f"Налог: {self.total_tax()} руб.")
        print(f"Итого к оплате: {self.get_total_with_tax()} руб.")

    def get_current_date(self):
        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) >= 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self.__name_items.remove(name)
        self.__number_items -= 1

    @staticmethod
    def get_telephone_number(telephone_number):
        if not str(telephone_number).isdigit():
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'