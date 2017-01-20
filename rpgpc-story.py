import os, sys

def main():
    me = Character(name='Wooby', description='Destroyer of worlds')
    #me.Greet()
    #me.Describe()
    #me.AnnounceBirthday()

    ex1 = Exerpt(name='start of story', choices=['choice 1', 'maybe you should choose this one'])
    #TODO Fix this
    ex2 = Exerpt()
    ex2.AddChoice(Choice(name='The blatantly obvious choice', linkedExerpt=ex1))
    ex2.AddChoice(Choice('not a good choice'))

    ex1.Prompt()
    ex2.Prompt()

    for choice in ex2.choices:
        try:
            choice.ShowResult
        except:
            print('some error')
            pass

class Character():
    def __init__(self, name, birthdate='Unknown', description='Indescribable'):
        self.name = name
        self.birthdate = birthdate
        self.description = description
    def Greet(self):
        print('Hello there. My name is ' + self.name + '.')
    def Describe(self):
        print(self.name + ' can only be described as...')
        print(self.description)
    def AnnounceBirthday(self):
        print('My birthday is ' + self.birthdate + '!')
class Story():
    def __init__(self, title):
        self.title = title
        self.exerpts = []
    def AddExerpt(self, exerpt):
        self.exerpts.append(exerpt)
class Exerpt():
    exerptId = 0

    def __init__(self, name=None, text='unwritten', choices=[]):
        if name is None:
            self.name = self.GenerateExerptName()
        else:
            self.name = name
        self.text = text
        self.choices = choices

    def AddChoice(self, choice):
        self.choices.append(choice)

    def GenerateExerptName(self):
        exerptName = 'exerpt_' + str(self.exerptId)
        self.exerptId += 1
        return exerptName

    def Prompt(self):
        print('Exerpt titled: ' + self.name)
        print(self.text)
        print(self.choices)

    def Preview(self):
        print('Exerpt titled: ' + self.name)
        print(self.text)

class Choice():
    def __init__(self, name, linkedExerpt=None):
        self.name = name
        self.linkedExerpt = linkedExerpt

    def LinkExerpt(self, exerpt):
        self.linkedExerpt = exerpt

    def ShowResult(self):
        if self.linkedExerpt is None:
            print('Unlinked Exerpt. Choice named ' + self.name + ' goes nowhere...')
        else:
            try:
                self.linkedExerpt.Preview()
            except:
                print('Something went wrong previewing the result of the choice...')
                pass


if __name__ == "__main__": main()
