class Card(object):
    def __init__(self, c, t, v):
        self.color = c
        self.type = t
        self.value = v

    def evaluate_card(self, open_c, open_v):
        return self.color == open_c or self.value == open_v or self.type == 'wild'
