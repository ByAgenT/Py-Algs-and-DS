

class Calculator(object):

    def get_priority(self, item):
        if item == '+' or item == '-':
            return 2
        elif item == '*' or item == '/':
            return 4

    def get_rpn(self, expression):
        operator_stack = []
        expression_stack = []
        for item in expression:
            if item.lstrip('-').replace('.', '', 1).isdigit():
                expression_stack.append(item)
            else:
                while operator_stack:
                    if (self.get_priority(item) <=
                            self.get_priority(operator_stack[-1])):
                        expression_stack.append(operator_stack.pop())
                    else:
                        operator_stack.append(item)
                        break
                else:
                    operator_stack.append(item)
        while operator_stack:
            expression_stack.append(operator_stack.pop())
        return expression_stack

    def solve_rpn(self, rpn):
        stack = []
        for item in rpn:
            if item.lstrip('-').replace('.', '', 1).isdigit():
                stack.append(item)
            else:
                if item == '+':
                    x, y = stack.pop(), stack.pop()
                    stack.append(float(x) + float(y))
                if item == '-':
                    x, y = stack.pop(), stack.pop()
                    stack.append(float(y) - float(x))
                if item == '*':
                    x, y = stack.pop(), stack.pop()
                    stack.append(float(x) * float(y))
                if item == '/':
                    x, y = stack.pop(), stack.pop()
                    stack.append(float(y) / float(x))
        s = "{:.4f}".format(float(stack.pop()))
        return float(s)

    def evaluate(self, query):
        # print("I will evaluate ", string)
        expression = query.split(" ")
        rpn = self.get_rpn(expression)
        return self.solve_rpn(rpn)


def main():
    QUERY = '2 + 5 - 6 * 2'
    c = Calculator()
    print(c.evaluate(QUERY))


if __name__ == '__main__':
    main()

