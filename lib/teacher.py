#!/usr/bin/env python



from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)
        else:
            return "I have no knowledge to share."
