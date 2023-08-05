def common_elements(set1, set2):
    common = set1 & set2  # Находим общие элементы множеств
    sorted_common = sorted(common) # Сортируем в порядке возрастания 
    return sorted_common

def main():
    n = int(input("Введите количество элементов первого множества: "))
    m = int(input("Введите количество элементов второго множества: "))
    
    set1 = set()
    set2 = set()
    
    for _ in range(n):
        element = int(input("Введите элемент первого множества: "))
        set1.add(element)
    
    for _ in range(m):
        element = int(input("Введите элемент второго множества: "))
        set2.add(element)
    
    result = common_elements(set1, set2)
    
    print("Общие элементы в порядке возрастания без повторений:", result)

if __name__ == "__main__":
    main()
