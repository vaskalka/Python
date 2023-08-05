def max_collected_berries(berries):
    n = len(berries)
    max_collected = 0
    
    for i in range(n):
        collected = berries[i] + (berries[i - 1] if i > 0 else 0) + (berries[(i + 1) % n] if i < n - 1 else 0)
        max_collected = max(max_collected, collected)
    
    return max_collected

def main():
    try:
        berries = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))

        result = max_collected_berries(berries)
        print("Максимальное число ягод, которое может собрать собирающий модуль:", result)
    
    except ValueError:
        print("Ошибка: введите целые числа, разделенные пробелами.")

if __name__ == "__main__":
    main()
