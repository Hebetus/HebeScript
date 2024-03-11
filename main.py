from lexer import Lexer

text_input = "tulosta(1 + 5 - 3);"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
