ashcaimport random
import datetime

#levels 0-6 (changed for coder speak) for flashcards, double the gap between reviews for each level, there is a looping 64-day schedule 
  #lvl 0: every 1 day (always do level 1 at the end)
  #lvl 1: every 2 days
  #lvl 2: every 4 days
  #lvl 3: every 8 days
  #lvl 4: every 16 days
  #lvl 5: every 32 days
  #lvl 6: every 64 days 
  #graduation: put into a graduation list seperate from the leitnerbox
#datetime setting or click to progress to next "day" setting
#tags as list 
  #incorrect and correct, tell which tags had the most incorrect answers (weakness areas) 
    #if incorrect, back to level 1
    #if correct, go up a level

#more complex: images, sound, notes
#from text file, easily quickly create rudimentary leitner box
#make it a user-friendly website, mobile-compatible (neocities?)

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

class Leitnerbox():
#makes a fresh leitnerbox (how do you save leitner boxes and not recreate them every time?)
#maybe one day i will implement a thing i can do to convert leitner box -> text file so you can save progress
#should i make them sets?

#for now, use manual progression (click next to move on to next day)
  def __init__(self,name,day):
    self.name = name
    self.day = day
    self.boxtags = set()
    self.level0 = []
    self.level1 = []
    self.level2 = []
    self.level3 = []
    self.level4 = []
    self.level5 = []
    self.level6 = []
    self.box = [self.level0,self.level1,self.level2,self.level3,self.level4,self.level5,self.level6]
    self.graduated = []
  
  def addnewcards(self,cards):
    for i in cards:
      #update tags
      for tag in i.tags:
        if not tag in self.boxtags:
          self.boxtags.add(tag)
      #assigns cards to levels
      self.box[i.level].append(i)
      
  #global not-in-play: counting tags, how many cards in each level
  def overviewlevel(self):
    print("Level 0 has " + str(len(self.box[0])) + " cards")
    print("Level 1 has " + str(len(self.box[1])) + " cards")
    print("Level 2 has " + str(len(self.box[2])) + " cards")
    print("Level 3 has " + str(len(self.box[3])) + " cards")
    print("Level 4 has " + str(len(self.box[4])) + " cards")
    print("Level 5 has " + str(len(self.box[5])) + " cards")
    print("Level 6 has " + str(len(self.box[6])) + " cards")
  
  def overviewtags(self):
    #for each unique tag
    for tag in self.boxtags:
      count = 0 
      #for each level
      for levelindex in range(len(self.box)):
        #for each card in each level
        for cardindex in range(len(self.box[levelindex])):
          if tag in self.box[levelindex][cardindex].tags:
            count += 1
      print(self.name + " has " + str(count) + " cards tagged " + tag)
        

  
  def play(self):
    levelstoplay = []
    if int(self.day % 64) == 0:
      levelstoplay.append(self.level6)
    if int(self.day % 32) == 0:
      levelstoplay.append(self.level5)
    if int(self.day % 16) == 0:
      levelstoplay.append(self.level4)
    if int(self.day % 8) == 0:
      levelstoplay.append(self.level3)
    if int(self.day % 4) == 0:
      levelstoplay.append(self.level2)
    if int(self.day) % 2 == 0:
      levelstoplay.append(self.level1)
    levelstoplay.append(self.level0)

    for level in levelstoplay:
      levelnumber = 0
      for i in range(len(self.box)):
        if level == self.box[i]:
          levelnumber = i
      print("=== LEVEL " + str(levelnumber) + " ===")
      correct = []
      incorrect = []
      random.shuffle(level)
      while len(level) > 0:
        for card in level:
          check = card.iscorrect()
          if check == True:
            print("Correct! This card advanced a level!")
            correct.append(card)
            #advance level
            if card.level < 6:
              self.box[card.level].remove(card)
              self.box[card.level+1].append(card)
              card.level += 1
            if card.level == 6:
              print("Congrats! This card has graduated!")
              self.graduated.append(card)
          elif check == False:
            print("Incorrect! This card goes back to Level 0. The actual answer was " + card.answer)
            print("card level before: " + str(card.level))
            incorrect.append(card)
            self.box[card.level].remove(card)
            card.level = 0
            print("this should be zero: " + str(card.level))
            self.box[0].append(card)
##global after-play: how many of what tags did you get incorrect (problem points), how many correct/incorrect
    print("You completed Day " + str(self.day) +"!")
    self.day += 1
    print("Overall, you got " + str(len(correct)) + " cards correct and " + str(len(incorrect)) + " cards incorrect")
    tagoverview = input("Do you want to see your tag overview? If so, input y. ")
    if tagoverview == "y":
      for i in self.boxtags:
        correctcount = 0
        incorrectcount = 0
        for correctcard in correct:
          if i in correctcard.tags:
            correctcount += 1
        for incorrectcard in incorrect:
          if i in incorrectcard.tags:
            incorrectcount += 1
        print("For cards tagged with " + str(i) +":")
        print(str(correctcount) + " correct")
        print(str(incorrectcount) + " incorrect")
        print()




wulun = Flashcard("无论","no matter what",["adverb","twowords"])
mofei = Flashcard("莫非","could it be that",["rhetorical","twowords"])
jingran = Flashcard("竟然","surprisingly",["adverb","twowords"])
yaoburen = Flashcard("要不然","otherwise",["conjugation","threewords"])
chufei = Flashcard("除非","unless",["conjugation","twowords"])

chinese = Leitnerbox("chinese",1)
chinese.addnewcards([wulun,mofei,jingran,yaoburen,chufei])
chinese.overviewlevel()
#chinese.overviewtags()

start = input("Press Enter to play your Leitner Box! ")
chinese.play()
while True:
  askcontinue = input("Do you want to continue? ")
  if askcontinue == "y":
    print("Great! You move on to Day " + str(chinese.day))
    chinese.overviewlevel()
    chinese.play()
  elif askcontinue == "n":
    break
  else:
    print("Please answer y or n.")
    