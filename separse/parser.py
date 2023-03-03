class Parser:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")

    def parse(self, *args) -> int | float:
        pass
