# # TODO решите задачу
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        content = f.read()
    data = eval(content)
    total = sum(d["score"] * d["weight"] for d in data)

    return round(total, 3)

print(task())
