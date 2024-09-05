import threading
import time

total_enemies = 100

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies_remaining = total_enemies
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies_remaining > 0:
            time.sleep(1)
            self.days += 1
            self.enemies_remaining -= self.power
            if self.enemies_remaining < 0:
                self.enemies_remaining = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies_remaining} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней!")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
