print( )
import math
import enum




class Lexer:

    position = 0


    def __init__(self,text) -> None:
        self.text = text


    def to_lex(self, text) -> None:
        self.text = text


    def next_token(self):



        if self.position >= len(self.text):
            return SyntaxToken(Token.EndFileToken, self.position, "EndFile", 1)
        


        if self.current().isdigit():      
            start = self.position
            while self.current().isdigit():
                self.next()
            self.lenght = self.position - start
            self.txt = self.text[start:(start+self.lenght)]  
            return SyntaxToken(Token.NumberToken, start, self.txt, 1)
        


        if self.current() == "+": 
            return SyntaxToken(Token.PlusToken, self.next(), "+", 1)    
        


        return SyntaxToken(Token.BadToken, self.next(), "aaaa", 1)



    def current(self) -> None:
        if self.position >= len(self.text):
            return "\0"
        return self.text[self.position]



    def next(self) -> None:
        self.position += 1






class Token(enum.Enum):
    NumberToken = int
    PlusToken = "+"
    BadToken= "bad t"
    EndFileToken= "FINAL"
    Empty = ""





class SyntaxToken:
    def __init__(self,kind,position, text, value) -> None:
        self.kind = kind
        self.position = position
        self.text = text
        self.value = value


     
print( )

f = Lexer("1+23232+3")
  
for a in range(6):
    #print(f.current())
    #print(f.position, "position")
    t = f.next_token()
    print(t.text, "text range")
    print(t.kind)
    print( )




 








    
