from dataclasses import dataclass


@dataclass
class LedColor:
    red: int
    green: int
    blue: int

    def __str__(self):
        return f"red: {self.red}, green: {self.green}, blue: {self.blue}"


if __name__ == "__main__":
    c = LedColor(150, 200, 30)
    print(c)
