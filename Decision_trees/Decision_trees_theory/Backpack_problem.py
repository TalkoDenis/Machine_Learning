def maximize_profit(items, max_weight):
    # Сортируем вещи по убыванию цены за килограмм
    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    
    total_weight = 0
    total_profit = 0
    selected_items = []
    
    for item in sorted_items:
        if total_weight + item[1] <= max_weight:
            # Если текущая вещь помещается, добавляем ее к выбранным
            selected_items.append(item)
            total_weight += item[1]
            total_profit += item[2]
    
    return selected_items, total_weight, total_profit

# Пример использования
# Вещь / вес в килограммах / стоимость
items = [("Вещь 1", 10, 60), ("Вещь 2", 20, 100), ("Вещь 3", 30, 120)]
max_weight = 50

selected_items, total_weight, total_profit = maximize_profit(items, max_weight)

print("Выбранные вещи:")
for item in selected_items:
    print(f"{item[0]} (Вес: {item[1]} кг, Стоимость: {item[2]} ДЕ)")

print(f"Общий вес выбранных вещей: {total_weight} кг")
print(f"Общая прибыль: {total_profit} ДЕ")