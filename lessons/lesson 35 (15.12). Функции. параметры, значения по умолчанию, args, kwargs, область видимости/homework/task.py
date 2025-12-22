def calculate_discount(price, percent):
    discount_amount = price * percent / 100
    return price - discount_amount


def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100


def format_currency(amount, currency_code):
    return f"{amount:.1f} {currency_code}"


discounted_price = calculate_discount(1000, 15)      # Результат: 850.0
tax_amount = calculate_tax(discounted_price, 20)     # Результат: 170.0
formatted_total = format_currency(discounted_price + tax_amount, "RUB")  # Результат: "1020.0 RUB"


def create_profile(name, age=18, hobbies=None, settings=None):
    if hobbies is None:
        hobbies = []
    if settings is None:
        settings = {"theme": "light"}
    return {
        "name": name,
        "age": age,
        "hobbies": hobbies,
        "settings": settings
    }



profile_maxim = create_profile("Максим", age=25)
print(profile_maxim)  # {"name": "Максим", "age": 25, "hobbies": [], "settings": {"theme": "light"}}

profile_ann = create_profile(
    "Анна",
    hobbies=["чтение", "бег"],
    settings={"theme": "dark", "notifications": False}
)
print(profile_ann)  # {"name": "Анна", "age": 18, "hobbies": ["чтение", "бег"], "settings": {"theme": "dark", "notifications": False}}


def aggregate_data(*args, **kwargs):
    total_sum = sum(args)
    count = len(args)
    result = {"sum": total_sum, "count": count}
    result.update(kwargs)
    return result


result = aggregate_data(10, 20, 30, unit="кг", source="весы")
print(result)  # {"sum": 60, "count": 3, "unit": "кг", "source": "весы"}

measurements = [100, 200, 150]
meta = {"unit": "мл", "experiment": "A"}
result = aggregate_data(*measurements, **meta)
print(result)  # {"sum": 450, "count": 3, "unit": "мл", "experiment": "A"}


def make_counter(name):
    def init_counter():
        count = [0] 
        
        def counter():
            count[0] += 1
            return (name, count[0])
        return counter
    return init_counter


create_counter_A = make_counter("Счетчик A")
create_counter_B = make_counter("Счетчик B")

counterA = create_counter_A()
counterB = create_counter_B()

print(counterA())  # ("Счетчик A", 1)
print(counterA())  # ("Счетчик A", 2)
print(counterB())  # ("Счетчик B", 1)
print(counterA())  # ("Счетчик A", 3)


