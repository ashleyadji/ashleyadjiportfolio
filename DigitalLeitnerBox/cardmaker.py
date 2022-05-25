class Flashcard():

  #when creating a new flashcard, this is what you need:
  def __init__(self,prompt,answer,tags):
    self.prompt = prompt
    self.answer = answer
    self.tags = tags
    self.level = 0

  #checks: did the player answer correctly?
  #why does it do it twice
  def iscorrect(self):
    #input from player
    x = input(" " + self.prompt + " ")
    if x == self.answer:
      return True
    else:
      return False

#create flashcards from text file, google docs, etc etc
#seperate cards with *
#on a website it would probably be different