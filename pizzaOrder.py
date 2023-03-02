class Pizza():
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost
        
    def get_description(self):
        return self.__description
    
    def get_cost(self):
        return self.__cost

# Pizza Türleri Alt Sınıfları - start
class Clasic(Pizza):
    def __init__(self, description="Klasik Pizza", cost = 50):
        super().__init__(description,cost)

class Margherita(Pizza):
    def __init__(self, description = "Margherita Peynirli Pizza", cost = 60):
        super().__init__(description,cost)

class Turkish(Pizza):
    def __init__(self, description = "Türk Usulu Pizza", cost = 70):
        super().__init__(description,cost)  

class Simple(Pizza):
    def __init__(self, description = "Sade Pizza", cost = 55):
        super().__init__(description,cost)  

# Pizza Türleri Alt Sınıfları - end

# Sos Türleri Alt Sınıfları - start
class Decorator(Pizza):
    def __init__(self, description, cost):
        super().__init__(description, cost)


class Olive(Decorator):
    def __init__(self, description  = "Zeytinli sos", cost = 10):
        super().__init__(description, cost)

class Mushroom(Decorator):
    def __init__(self, description="Mantarlı sos", cost=12):
        super().__init__(description, cost)

class GoatCheese(Decorator):
    def __init__(self, description  = "Keçi peynirli sos", cost = 15):
        super().__init__(description, cost)

class Meat(Decorator):
    def __init__(self, description  = "Etli sos", cost = 25):
        super().__init__(description, cost)

class Onion(Decorator):
    def __init__(self, description  = "Soğanlı sos", cost = 5):
        super().__init__(description, cost)

class Corn(Decorator):
    def __init__(self, description  = "Mısırlı sos", cost = 8):
        super().__init__(description, cost)

# Sos Türleri Alt Sınıfları - end

