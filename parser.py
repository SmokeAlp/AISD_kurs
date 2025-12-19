from node import Node, ExpressionError


class Parser:
    def __init__(self, expr_parts):
        self.expr_parts = expr_parts
        self.pos = 0

    def current(self):
        if self.pos < len(self.expr_parts):
            return self.expr_parts[self.pos]
        else:
            return None

    def get_part(self, expected=None):
        part = self.current()
        if expected and part != expected:
            raise ExpressionError(f"Ожидалось {expected}, получено {part}")
        self.pos += 1
        return part

    def parse(self):
        node = self.parse_fourth()
        if self.current() is not None:
            raise ExpressionError("Лишние символы в конце выражения")
        return node

    def parse_fourth(self):
        node = self.parse_third()
        while self.current() in ('+', '-'):
            op = self.get_part()
            node = Node(op, node, self.parse_third())
        return node

    def parse_third(self):
        node = self.parse_second()
        while self.current() in ('*', '/'):
            op = self.get_part()
            node = Node(op, node, self.parse_second())
        return node

    def parse_second(self):
        node = self.parse_first()
        if self.current() == '^':
            self.get_part('^')
            node = Node('^', node, self.parse_second())
        return node

    def parse_first(self):
        part = self.current()

        if part == '-':
            self.get_part('-')
            return Node('u-', self.parse_second())

        if type(part) == int:
            self.get_part()
            return Node(part)

        if part == '(':
            self.get_part('(')
            node = self.parse_fourth()
            self.get_part(')')
            return node

        raise ExpressionError(f"Неожиданная часть выражения: {part}")