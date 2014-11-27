class InputBoxes():
    def __init__(self, name, label, value, cost, description):
        self.name = name
        self.label = label
        self.value = value
        self.cost = cost
        self.description = description

class DropDownBoxes():
    def __init__(self, name, text, value, cost, id):
        self.name = name
        self.text = text
        self.value = value
        self.cost = cost
        self.id = id

class MonthlyRads():
    def __init__(self, name, text, value):
        self.name = name
        self.text = text
        self.value = value

