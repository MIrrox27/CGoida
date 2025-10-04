#
# CGoidaTokens.py

from enum import Enum


# Перечисление всех типов токенов в нашем языке программирования
class CGoidaTokenType(Enum):
    # ЛИТЕРАЛЫ (константные значения)
    NUMBER = 'NUMBER'  # Целое число: 42, 100, -5
    STRING = 'STRING'  # Строка в кавычках: "привет", "мир"
    FLOAT = 'FLOAT'  # Десятичное число: 3.14, 2.5, 0.5
    BOOL = 'BOOL'  # Логическое значение: true, false

    # КЛЮЧЕВЫЕ СЛОВА (зарезервированные слова языка)
    FUN = 'FUN'  # Объявление функции: fun
    CLASS = 'CLASS'  # Объявление класса: class
    ENUM = 'ENUM'  # Объявление перечисления: enum
    IMPORT = 'IMPORT'  # Импорт модулей: import
    CG = 'CG'  # Объявление переменной: cg (от "переменная")
    IF = 'IF'  # Условный оператор: if
    ELSE = 'ELSE'  # Условный оператор: else
    WHILE = 'WHILE'  # Цикл while: while
    FOR = "FOR"  # Цикл for: for
    VIVOD = 'VIVOD'  # Вывод на печать: vivod

    # ОПЕРАТОРЫ (математические и логические операции)
    PLUS = 'PLUS'  # Сложение: +
    MINUS = 'MINUS'  # Вычитание: -
    MULTIPLY = 'MULTIPLY'  # Умножение: *
    DIVIDE = 'DIVIDE'  # Деление: /
    ASSIGN = 'ASSIGN'  # Присваивание: =
    EQUALS = 'EQUALS'  # Равенство: ==
    NOT_EQUALS = 'NOT_EQUALS'  # Неравенство: !=
    LESS = 'LESS'  # Меньше: <
    GREATER = 'GREATER'  # Больше: >
    MOD = 'MOD'# %

    # РАЗДЕЛИТЕЛИ (пунктуация и скобки)
    LPAREN = 'LPAREN'  # Левая круглая скобка: (
    RPAREN = 'RPAREN'  # Правая круглая скобка: )
    LBRACE = 'LBRACE'  # Левая фигурная скобка: {
    RBRACE = 'RBRACE'  # Правая фигурная скобка: }
    SEMICOLON = 'SEMICOLON'  # Точка с запятой: ;
    COMMA = 'COMMA'  # Запятая: ,

    # СПЕЦИАЛЬНЫЕ ТОКЕНЫ
    EOF = 'EOF'  # Конец файла (End Of File)
    IDENTIFIER = 'IDENTIFIER'  # Идентификатор (имя переменной/функции)


# Класс для представления отдельного токена
class CGoidaToken:
    def __init__(self, type: CGoidaTokenType, value: any = None, line: int = 1):
        self.type = type  # Тип токена из перечисления TokenType
        self.value = value  # Значение токена (для чисел, строк, идентификаторов)
        self.line = line  # Номер строки, где найден токен (для отладки ошибок)

    def __str__(self):
        # Красивое строковое представление токена для отладки
        if self.value is not None:
            return f"Token({self.type}, {repr(self.value)}, line: {self.line})"
        return f"Token({self.type}, line: {self.line})"

    def __repr__(self):
        # Техническое строковое представление
        return self.__str__()