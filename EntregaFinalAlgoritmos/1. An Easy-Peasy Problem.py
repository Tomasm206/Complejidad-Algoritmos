class Box:
    MAX_HEIGHT = 41

    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def get_volume(self):
        return self.height * self.length * self.width

    def is_lower_than_max_height(self):
        return self.height < Box.MAX_HEIGHT

def main():
    height, length, width = map(int, input().split())
    box = Box(height, length, width)
    print(box.get_volume())
    print("YES" if box.is_lower_than_max_height() else "NO")

if __name__ == "__main__":
    main()
