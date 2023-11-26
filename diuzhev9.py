import random

class NumberGenerator:
    @staticmethod
    def generate_number():
        return random.randint(1, 100)

class Game:
    def __init__(self, number_generator):
        self.secret_number = number_generator.generate_number()

    def play(self):
        print("Вгадайте число від 1 до 100")
        attempts = 0

        while True:
            guess = int(input("Ваш варіант: "))
            attempts += 1

            if guess == self.secret_number:
                print(f"Ви вгадали! Число {self.secret_number}. Кількість спроб: {attempts}")
                break
            elif guess < self.secret_number:
                print("Загадане число більше. Спробуйте ще раз.")
            else:
                print("Загадане число менше. Спробуйте ще раз.")

if __name__ == "__main__":
    number_generator = NumberGenerator()
    game = Game(number_generator)
    game.play()