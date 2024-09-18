class stringReverser:
    def __init__(self,input_string) -> None:
        self.input_string=input_string
    def reverse_words(self):
        words=self.input_string.split()
        reversed_words=words[::-1]
        return ''.join(reversed_words)
    
if __name__=="__main__":
    input_string="This is python"
    reverser=stringReverser(input_string)
    print("original string:",input_string)
    print("Reversed string:",reverser.reverse_words())