from rply import ParserGenerator
from ast import Kokonaisluku, Summa, Erotus, Tulosta_päätteeseen

class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # Luettelo parserin hyväksymistä merkeistä (token)
            ['PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON', 'SUM', 'SUB', 'NUMBER']
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Tulosta_päätteeseen(self.builder, self.module, self.printf, p[2])
        
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'SUM':
                return Summa(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Erotus(self.builder, self.module, left, right)
        
        @self.pg.production('expression : NUMBER')
        def number(p):
            return Kokonaisluku(self.builder, self.module, p[0].value)
        
        @self.pg.error
        def error_handle(token):
            raise ValueError(token)
        
    def get_parser(self):
        return self.pg.build()