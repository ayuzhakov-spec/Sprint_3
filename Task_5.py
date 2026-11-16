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

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) >= 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self._item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self._name_items.append(name)
        self._number_items += 1

    def delete_item_from_check(self, name):
        if name not in self._name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self._name_items.remove(name)
        self._number_items -= 1

    def check_amount(self):
        total = []

        for item in self._name_items:
            total.append(self._item_price[item])
        
        final_sum = sum(total)
        
        if self._number_items > 10: 
            return final_sum * 0.9
        
        return final_sum

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []  
        total = []               

        for item in self._name_items:
            if item in self._tax_rate and self._tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self._item_price[item])

        final_sum = sum(total)
        if self._number_items > 10:
            final_sum = final_sum * 0.9

        return final_sum * 0.2
