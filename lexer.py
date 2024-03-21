from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Tulostus päätteeseen:
        
        self.lexer.add('PRINT', r'tulosta')

        # Tulostuksen avaus ja sulkeminen
        
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Käännösyksikön päätös

        self.lexer.add('SEMI_COLON', r'\;')

        # Summa ja erotus:

        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')

        # Numero:

        self.lexer.add('NUMBER', r'\d+')

        # Tyhjä tila (whitespace) jätetään huomiotta:

        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()