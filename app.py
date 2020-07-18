class Flowers:
    flowers = {
        "Begonias": 6,
        "Geraniums": 6,
        "Lobelia": 9,
        "Petunias": 9
    }

    def __init__(self, b, g, l, p, postcode):
        self.begonias = b
        self.geraniums = g
        self.lobelia = l
        self.petunias = p
        self.code = postcode
        self.total = b + g + l + p

    def calculate(self):
        total = 0
        total += (self.flowers["Begonias"] * self.begonias)
        total += (self.flowers["Geraniums"] * self.geraniums)
        total += (self.flowers["Lobelia"] * self.lobelia)
        total += (self.flowers["Petunias"] * self.petunias)

        return total, self.total

    def area_calculation(self):
        area = 0
        area += ((self.begonias * 6) * 30 * 30)
        area += ((self.geraniums * 6) * 30 * 30)
        area += ((self.lobelia * 9) * 15 * 15)
        area += ((self.petunias * 9) * 30 * 30)

        area = area / 1000

        return area

    def price_calculation(self):
        discount = 0
        price = 0
        price += (self.begonias + self.geraniums) * 4.25
        price += (self.lobelia + self.petunias) * 3.55

        if self.total >= 5:
            print("You have qualified for a 10%\ discount")
            print("")
            discount = 0.9

        discount_price = price * discount
        total_price = price - discount_price

        if self.code == "BD16":
            discount_price += 3
        elif self.code == "BD20" or self.code == "BD22":
            discount_price += 5
        else:
            discount_price += 4
        return round(price, 2), round(total_price, 2), round(discount_price, 2)


f1 = Flowers(
    int(input("Begonias (6 pack): ")),
    int(input("Geraniums (6 pack): ")),
    int(input("Lobelia (9 pack): ")),
    int(input("Petunias (9 pack): ")),
    input("What is the first part of your postcode (BD??):").upper()
)

print(
    f"{f1.calculate()[1]} packs of plants or {f1.calculate()[0]} individual plants. You have enough plants to cover {f1.area_calculation()} square metres."
)

print(
    f"Sub Total: £{f1.price_calculation()[0]}\nPrice (With Delivery): £{f1.price_calculation()[2]}")
