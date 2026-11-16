import datetime

class OnlineSalesRegisterCollector:

    def add_item(self, item_name):
    if item_name in self._item_price:
        self._name_items.append(item_name)
        self._number_items += 1
    else:
        raise ValueError(f"Товара {item_name} нет в наличии")

    def remove_item(self, item_name):
        if item_name in self.name_items: # Обращаемся через геттер
            self.name_items.remove(item_name)
            self._number_items -= 1
        else:
            raise ValueError(f"Товара {item_name} нет в чеке")

    @property
    def name_items(self):
        return self._name_items 

    def number_items(self):
        return self._number_items

    @property
    def number_items(self):
        return self._number_items

    def get_total_price(self):
        total = 0
        for item in self._name_items:
            total += self._item_price[item]
        return total

    def get_total_with_tax(self):
        return self.get_total_price() + self.get_total_tax()

    def print_receipt(self):
        print("Чек:")
    for item in self._name_items:
        print(f"{item}: {self._item_price[item]} руб.")
        print(f"Итого без налога: {self.get_total_price()} руб.")
        print(f"Налог: {self.get_total_tax()} руб.")
        print(f"Итого к оплате: {self.get_total_with_tax()} руб.")

    def get_current_date(self):
        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M") 

    


