class ExpressionError(Exception):
    pass


def read(expression):
    expr_parts = []
    i = 0
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue

        if expression[i].isdigit():
            num = ""
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            expr_parts.append(int(num))
            continue

        if expression[i] in "+-*/^()":
            expr_parts.append(expression[i])
            i += 1
            continue

        raise ExpressionError(f"Некорректный символ: {expression[i]}")
    return expr_parts