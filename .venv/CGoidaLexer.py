

from CGoidaTokens import CGoidaTokenType

class CGoidaLexer:
    def __init__(self, text: str):
        self.text = text # сам код который мы передаем в наш интерпритатор
        self.position = 0 # позиция "курсора" в тексте порядковый номер символа
        self.line = 1 # линия (строка в которой мы находимся) (по типу координаты Y)
        self.current_char = self.text[0] if self.text else None # символ, который мы сейчас обрабатываем. Т. е если символ text не равен None то мы присваиваем self.current_char значение этого символа, иначе self.current_char = None

    def error(self):
        pass

    def advance(self):
        if self.current_char == "\n":
            self.line += 1              # если current_char равен символу перехода строки, то мы опускаемся вниз
        self.position += 1              # так как мы прошли символ перехода строки, надо переместиться на новый символ

        if self.position >= len(self.text):                 # если наша позиция в тексе выходит за его рамки (текста)
            self.current_char = None                        # то символ который мы обрабатываем равен None
        else:
            self.current_char = self.text[self.position]    # иначе self.символ_для_обработки = self.код[позиция_в_коде]

    def peekPosition(self, lookhead: int = 1):
        peek_position = self.position + lookhead
        if peek_position >= len(self.text):
            return None
        return self.text[peek_position]

if __name__ == "__main__":
    # Создаем лексер для простого кода
    lexer = CGoidaLexer("x = 5")
    print(lexer.current_char)  # 'x'
    lexer.advance()
    print(lexer.current_char)  # ' '
    print(lexer.peekPosition())  # '='