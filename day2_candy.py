candies = [{"name": "Mongolian Candy", "price_mnt": 100, "stock": 1}, 
            {"name": "Russian Candy", "price_mnt": 200, "stock": 20}, 
            {"name": "Chinese Candy", "price_mnt": 300, "stock": 30}, 
            {"name": "Japanese Candy", "price_mnt": 400, "stock": 40}, 
            {"name": "Korean Candy", "price_mnt": 500, "stock": 50}
]
def check_stock(candy):
    if candy["stock"] < 8:
        return "reorder"
    elif candy["stock"] <= 50:
        return "ok"
    else:
        return "too much"

for candy in candies:
    print(candy["name"], check_stock(candy))
counts = {"reorder": 0, "ok": 0, "too much": 0}
for candy in candies:
    label = check_stock(candy)
    counts[label] = counts[label] + 1
print(counts)