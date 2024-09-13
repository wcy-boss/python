name = "pkg Hello"

def say():
    print("pkg Hello world!")
    
class Nice:
    
    def __init__(self) -> None:
        self.name = "pkg Hello Nice"
        
    def __str__(self) -> str:
        return self.name