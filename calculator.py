def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

print("Калькулятор. Для выхода введите 'exit'")
while True:
    expr = input("\nВведите выражение (например, 5 + 3): ").strip()
    if expr.lower() == 'exit':
        break
    parts = expr.split()
    if len(parts) != 3:
        print("Неверный формат. Пример: 5 + 3")
        continue
    a_str, op, b_str = parts
    if op not in operations:
        print(f"Неизвестная операция '{op}'. Доступны: + - * /")
        continue
    try:
        a, b = float(a_str), float(b_str)
        result = operations[op](a, b)
        print(f"= {result:g}")
    except ValueError as e:
        print(f"Ошибка: {e}")
