from parser import Parser
from reader import read


expression = 0
while True:
    expression = input("Введите выражение для решения или 0 для выхода: ")
    if expression == "0": break
    tokens = read(expression)
    parser = Parser(tokens)
    tree = parser.parse()

    print("Дерево выражения:")
    tree.print_tree()

    print("\nФормы записи:")
    print("Инфиксная :", tree.infix())
    print("Префиксная:", tree.prefix())
    print("Постфиксная:", tree.postfix())

    print("\nРезультат вычисления:", tree.solve())