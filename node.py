class ExpressionError(Exception):
    pass

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def solve(self):
        if self.left is None and self.right is None:
            return self.value

        if self.value == 'u-':
            return -self.left.solve()

        a = self.left.solve()
        b = self.right.solve()

        if self.value == '+':
            return a + b
        if self.value == '-':
            return a - b
        if self.value == '*':
            return a * b
        if self.value == '/':
            if b == 0:
                raise ExpressionError("Деление на ноль")
            return a // b
        if self.value == '^':
            return a ** b

        raise ExpressionError("Неизвестный оператор")

    def infix(self):
        if self.left is None and self.right is None:
            return str(self.value)
        if self.value == 'u-':
            return f"(u-{self.left.infix()})"
        return f"({self.left.infix()} {self.value} {self.right.infix()})"

    def prefix(self):
        if self.left is None and self.right is None:
            return str(self.value)
        if self.value == 'u-':
            return f"u- {self.left.prefix()}"
        return f"{self.value} {self.left.prefix()} {self.right.prefix()}"

    def postfix(self):
        if self.left is None and self.right is None:
            return str(self.value)
        if self.value == 'u-':
            return f"{self.left.postfix()} u-"
        return f"{self.left.postfix()} {self.right.postfix()} {self.value}"

    def print_tree(self, level=0, name="Корень: "):
        print(" " * (level * 4) + name + str(self.value))
        if self.left:
            self.left.print_tree(level + 1, "L: ")
        if self.right:
            self.right.print_tree(level + 1, "R: ")