from colorama import Fore

class Wordle:

    NUMBER_OF_ATTEMPTS=6
    WORD_LENGTH=5
    SOLVED_BEFORE_ALL_ATTEPMTS=False

    WARNING_COLOR=Fore.RED
    IN_WORD_COLOR=Fore.YELLOW
    IN_POSITION_COLOR=Fore.GREEN
    DEFAULT_COLOR=Fore.RESET
    CORRECT_WORD_COLOR=Fore.GREEN


    def __init__(self,secret_word:str):

        self.word=""
        self.secret_word=secret_word.upper()
        self.attepmts=0
        self.words_attempted=["","","","","",""]


    @property
    def can_attempt(self):
        return self.attepmts < self.NUMBER_OF_ATTEMPTS and self.isSolved == False

    @property
    def isSolved(self):
        return self.word == self.secret_word

    def attempt(self,word:str):

        self.word=word.upper()

        if self.validate(self.word):

            self.words_attempted[self.attepmts]=self.word
            self.attepmts+=1

            if self.isSolved:
                self.displayWordsGuessed()
                self.SOLVED_BEFORE_ALL_ATTEPMTS=True
                self.displayMessage("You have Guessed the Word Correctly in {} attempts.".format(self.attepmts),self.CORRECT_WORD_COLOR)
            
            else:
                self.displayWordsGuessed()

                
        else:
            print("Not a Valid Word")

    
    def validate(self,word:str):
        return word.isalpha() and len(word)== self.WORD_LENGTH

    
    def displayWordsGuessed(self):
        
        for word in self.words_attempted:
            if word is not '':
                print("{}".format(self.checkResult(word)))
            else:
                print("-  "*self.WORD_LENGTH)

    
    def displayLetter(self,letter:str,color:Fore):
        
        return color + letter + self.DEFAULT_COLOR
        

    def displayMessage(self,message:str,color:Fore,end='\n'):
        
        print("{}{}{}".format(color,message,self.DEFAULT_COLOR),end=end)


    def checkResult(self,word:str):
        
        if not self.isSolved:
            word_with_color=[]
            for i in range(len(word)):

                if  word[i] in self.secret_word[i]:
                    word_with_color.append(self.displayLetter("{}".format(word[i]),self.IN_POSITION_COLOR))
                
                elif word[i] in self.secret_word:
                    word_with_color.append(self.displayLetter("{}".format(word[i]),self.IN_WORD_COLOR))

                else:
                    word_with_color.append(self.displayLetter("{}".format(word[i]),self.WARNING_COLOR))
            
            
            return "  ".join(word_with_color)





