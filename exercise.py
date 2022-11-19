class Exercise:

    def __init__(self,name,type,description,intensity, quantity):
        self.name = name
        self.type = type
        self.description = description
        self.intensity = intensity
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

    def get_intensity(self):
        return self.intensity

    def get_quantity(self):
        return self.quantity