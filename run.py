
from nnf import Var, true, false
from lib204 import Encoding
import random

#initalizes dictionaries of values for each attribute of a card in SET
card_colour = {}
card_shape = {}
card_number = {}
card_shading = {}

#initalizes the variables for the models, they need to be declared true or false in the actual model
for i in [1, 2, 3]:
  for j in ["red", "purple", "green"]:
    card_colour[(i,j)] = Var("(%d,%s)" % (i,j))
 
for i in [1, 2, 3]:
  for j in ["oval", "diamond", "squiggle"]:
    card_shape[(i,j)] = Var("(%d,%s)" % (i,j))
 
for i in [1, 2, 3]:
  for j in [1, 2, 3]:
    card_number[(i,j)] = Var("(%d,%s)" % (i,j))
 
for i in [1, 2, 3]:
  for j in ["hollow", "shaded", "lined"]:
    card_shading[(i,j)] = Var("(%d,%s)" % (i,j))

#initalizes conditions to win
sameShape = Var("sameShape")
sameColour = Var("sameColour")
sameShading = Var("sameShading")
sameNumber = Var("sameNumber")
 
allDiffShape = Var("diffShape")
allDiffColour = Var("diffColour")
allDiffShading = Var("diffShading")
allDiffNumber = Var("diffNumber")
 

#Old constraint initalization 
#winningSet = Var("winningSet")



# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def set_theory():
    E = Encoding()
    
    #initalizes that only one of each attribute type can be true per card
    for i in [1,2,3]:
       E.add_constraint(card_colour[i,"red"] | card_colour[i,"purple"] | card_colour[i,"green"]) 
       E.add_constraint(card_shape[i,"oval"] | card_shape[i,"diamond"] | card_shape[i,"squiggle"])
       E.add_constraint(card_shading[i,"hollow"] | card_shading[i,"shaded"] | card_shading[i,"lined"])
       E.add_constraint(card_number[i,1] | card_number[i,2] | card_number[i,3])
   
    #sameShape implies that each card has the same shape attribute value
    E.add_constraint(sameShape.negate() |  (
      (card_shape[1,"oval"] & card_shape[2,"oval"] & card_shape[3,"oval"]) 	|
      (card_shape[1,"diamond"] & card_shape[2,"diamond"] & card_shape[3,"diamond"]) 	|
      (card_shape[1,"squiggle"] & card_shape[2,"squiggle"] & card_shape[3,"squiggle"])
      ))

    #sameColour implies that each card has the same colour attribute value
    E.add_constraint(sameColour.negate() |  (
     (card_colour[1,"red"] & card_colour[2,"red"] & card_colour[3,"red"]) 	|
     (card_colour[1,"green"] & card_colour[2,"green"] & card_colour[3,"green"]) 	|
     (card_colour[1,"purple"] & card_colour[2,"purple"] & card_colour[3,"purple"])
     ))

    #sameShading implies that each card has the same shading attribute value
    E.add_constraint(sameShading.negate() |  (
      (card_shading[1,"hollow"] & card_shading[2,"hollow"] & card_shading[3,"hollow"]) 	|
      (card_shading[1,"shaded"] & card_shading[2,"shaded"] & card_shading[3,"shaded"]) 	|
      (card_shading[1,"lined"] & card_shading[2,"lined"] & card_shading[3,"lined"])
      ))

    #sameNumber implies that each card has the same number attribute value
    E.add_constraint(sameNumber.negate() |  (
      (card_number[1,1] & card_number[2,1] & card_number[3,1]) 	|
      (card_number[1,2] & card_number[2,2] & card_number[3,2]) 	|
      (card_number[1,3] & card_number[2,3] & card_number[3,3])
      ))


    #allDiffShape implies that every card has a different shape attribute value
    E.add_constraint(allDiffShape.negate() |  (
  	(card_shape[1,"oval"] & card_shape[2,"diamond"] & card_shape[3,"squiggle"]) |
    (card_shape[1,"oval"] & card_shape[2,"squiggle"] & card_shape[3,"diamond"])  |
    (card_shape[1,"squiggle"] & card_shape[2,"oval"] & card_shape[3,"diamond"])  |
    (card_shape[1,"squiggle"] & card_shape[2,"diamond"] & card_shape[3,"oval"])  |
    (card_shape[1,"diamond"] & card_shape[2,"oval"] & card_shape[3,"squiggle"])  |
    (card_shape[1,"diamond"] & card_shape[2,"squiggle"] & card_shape[3,"oval"])  
    ))
 
    #allDiffColour implies that every card has a different colour attribute value
    E.add_constraint(allDiffColour.negate() | (
    (card_colour[1,"red"] & card_colour[2,"purple"] & card_colour[3,"green"]) |
    (card_colour[1,"red"] & card_colour[2,"green"] & card_colour[3,"purple"]) |
    (card_colour[1,"purple"] & card_colour[2,"red"] & card_colour[3,"green"]) |
    (card_colour[1,"green"] & card_colour[2,"purple"] & card_colour[3,"red"]) |
    (card_colour[1,"purple"] & card_colour[2,"green"] & card_colour[3,"red"]) |
    (card_colour[1,"green"] & card_colour[2,"red"] & card_colour[3,"purple"]) 
    ))
 
    #allDiffShading implies that every card has a different shading attribute value
    E.add_constraint(allDiffShading.negate() |  (
    (card_shading[1,"hollow"] & card_shading[2,"shaded"] & card_shading[3,"lined"]) |
    (card_shading[1,"hollow"] & card_shading[2,"lined"] & card_shading[3,"shaded"])  |
    (card_shading[1,"lined"] & card_shading[2,"hollow"] & card_shading[3,"shaded"])  |
    (card_shading[1,"lined"] & card_shading[2,"shaded"] & card_shading[3,"hollow"])  |
    (card_shading[1,"shaded"] & card_shading[2,"hollow"] & card_shading[3,"lined"])  |
    (card_shading[1,"shaded"] & card_shading[2,"lined"] & card_shading[3,"hollow"])  
    ))
 
    #allDiffNumber implies that every card has a different number attribute value
    E.add_constraint(allDiffNumber.negate() |  (
  	(card_number[1,1] & card_number[2,2] & card_number[3,3]) |
    (card_number[1,1] & card_number[2,3] & card_number[3,2]) |
    (card_number[1,2] & card_number[2,1] & card_number[3,3]) |
    (card_number[1,2] & card_number[2,3] & card_number[3,1]) |
    (card_number[1,3] & card_number[2,1] & card_number[3,2]) |
    (card_number[1,3] & card_number[2,2] & card_number[3,1]) 
    ))

    #To be a winning state, then the following constraints need to be in place
    E.add_constraint(((sameShape | allDiffShape) & (sameShading | allDiffShading) & (sameColour | allDiffColour) & (sameNumber| allDiffNumber)))
 
    return E


def setVarFalse():
  """ This function sets every variable to false."""
  for i in [1,2,3]:
    for j in ["red", "purple", "green"]:
      card_colour[(i,j)] = false
    for j in ["oval", "diamond", "squiggle"]:
      card_shape[(i,j)] = false
    for j in [1, 2, 3]:
      card_number[(i,j)] = false
    for j in ["hollow", "shaded", "lined"]:
      card_shading[(i,j)] = false


def testGroupOf3(cardGroup):
  """ This function first sets all the variables to false, then it sets the variables that correspond to each card's attributes to true. Then it returns wether or not the model is satisfiable.
  cardGroup - list of 3 dictionaries
  returns boolean (if the model T is satisfiable)
  """
  #sets all the variables to false
  setVarFalse()
 
  #sets the variables that correspond to each card's attributes to true
  for i in [1,2,3]:
    card_colour[(i,cardGroup[i-1][1])] = true
    card_shape[(i,cardGroup[i-1][2])] = true
    card_number[(i,cardGroup[i-1][3])] = true
    card_shading[(i,cardGroup[i-1][4])] = true

  #creates the model
  T = set_theory()
  #determines if the model is satisfiable
  return T.is_satisfiable()


def groupsIn12Cards(show):
  """ This function creates 12 different cards and checks how many valid sets there are in them.
  returns the number of valid sets
  """
  #initalizes list where the 12 cards will be
  listofCards = []
  if(show == "yes"):
    print("List of 12 random cards: ")
  # show = input("Do you want to print the list of cards and sets? 'yes' or 'no' (Suggested no for larger iterations)")

  #creates 12 different cards 
  i = 1
  while(len(listofCards) <12):
    r1 = randomCard()
    if(r1 not in listofCards):
      listofCards.append(r1)
      if(show == "yes"):
        printCards(i, r1)
      i += 1

  #finds the number of valid sets with the 12 cards
  count = 0;
  validSet = [] #keeps track of valid sets
  validSetCards = [] #keeps track of which cards make the valid set
  #these iterate through every possible set of 3 cards
  for x in range(12):
    for y in range(x+1,12):
      for z in range(y+1,12):
        sat = testGroupOf3([listofCards[x], listofCards[y], listofCards[z]])
        if(sat == True):
          count = count + 1
          validSet.append([listofCards[x], listofCards[y], listofCards[z]])
          validSetCards.append([x,y, z])
  print("--------------------------------")

  print("There are", count, " valid sets.")
  for i in range(count):
    if(show == "yes"):
      print("Valid set:", i+1)
    for j in range(3):
      if(show == "yes"):
        printCards(validSetCards[i][j], validSet[i][j])
  print("--------------------------------")
  return count

def userSetGroupsIn12Cards(show):
  """ This function ask the user to create 12 different cards and checks how many valid sets there are in them.
  returns the number of valid sets
  """
  #initalizes list where the 12 cards will be
  listofCards = []
  if(show == "yes"):
    print("List of 12 random cards: ")
  # show = input("Do you want to print the list of cards and sets? 'yes' or 'no' (Suggested no for larger iterations)")

  #user created cards
  for i in range(12):
    print("Card: " + str(i+1))
    c = input(" Colour of card " +str(i+1)+ " (only 'purple' 'red' or 'green'): ")
    s = input(" Shape of card " +str(i+1)+ " (only 'oval' 'diamond' or 'squiggle'): ")
    n = input(" Number of shapes on card "+(i+1)+ " (only '1' '2' or '3'): ")
    h = input(" Shading of card "+str(i+1)+ " (only 'hollow' 'shaded' or 'lined'): ")
    card = {1:c, 2: s, 3: (int)(n), 4: h}
    listofCards.append(card)

  #creates 12 different cards 
  # i = 1
  # while(len(listofCards) <12):
  #   r1 = randomCard()
  #   if(r1 not in listofCards):
  #     listofCards.append(r1)
  #     if(show == "yes"):
  #       printCards(i, r1)
  #     i += 1

  #finds the number of valid sets with the 12 cards
  count = 0;
  validSet = [] #keeps track of valid sets
  validSetCards = [] #keeps track of which cards make the valid set
  #these iterate through every possible set of 3 cards
  for x in range(12):
    for y in range(x+1,12):
      for z in range(y+1,12):
        sat = testGroupOf3([listofCards[x], listofCards[y], listofCards[z]])
        if(sat == True):
          count = count + 1
          validSet.append([listofCards[x], listofCards[y], listofCards[z]])
          validSetCards.append([x,y, z])
  print("--------------------------------")

  
  print("There are", count, " valid sets.")
  for i in range(count):
    if(show == "yes"):
      print("Valid set:", i+1)
    for j in range(3):
      if(show == "yes"):
        printCards(validSetCards[i][j], validSet[i][j])
  print("--------------------------------")
  return count



def find3rdCard(cardGroup):
  """ This function gets a group of 2 cards, finds the 3rd card to complete the set and then checks to see if the 3 cards make a valid set. 
  cardGroup - list of 2 dictionaries
  returns boolean (if the model is satisfiable or not)
  """
  #set all the variables to false
  setVarFalse()

  print("The 2 cards are:")
  printCards(1,cardGroup[0])
  printCards(2,cardGroup[1])
  print("The final card is: ")
  finalCard = manual3rdCard(cardGroup) #finds the 3rd card
  printCards(3, finalCard)

  #creates a list of the cards
  tempcardGroup = [cardGroup[0],cardGroup[1],finalCard]

  #initalizes the variables for each cards' attributes's values
  for i in [1,2,3]:
    card_colour[(i,tempcardGroup[i-1][1])] = true
    card_shape[(i,tempcardGroup[i-1][2])] = true
    card_number[(i,tempcardGroup[i-1][3])] = true
    card_shading[(i,tempcardGroup[i-1][4])] = true

  T = set_theory()
  return T.is_satisfiable()


def manual3rdCard(cardpair):
  """ This function finds the 3rd cards for the corresponding 2 cards in the cardpair.
  cardpair - list of 2 dictionaries
  returns a card (dictionary)
  """
  colours = ["purple", "red", "green"]
  shapes = ["squiggle", "oval", "diamond"]
  numbers = [1, 2, 3]
  shadings = ["hollow", "shaded", "lined"]
  #checks if the third card will need the same attributes
  scolour = (cardpair[1][1] == cardpair[0][1])
  sshape = (cardpair[1][2] == cardpair[0][2])
  snumber = (cardpair[1][3] == cardpair[0][3])
  sshading = (cardpair[1][4] == cardpair[0][4])
  
  #assigns an attribute based on the previous results
  if (scolour):
    colour = cardpair[1][1]
  else:
    for i in range(3):
      if (colours[i] != cardpair[0][1]):
        if(colours[i] != cardpair[1][1]):
          colour = colours[i]
          break
  if (sshape):
    shape = cardpair[1][2]
  else:
    for i in range(3):
      #print(shapes[i], cardpair[0][2], cardpair[1][2])
      #if(shapes[i] != cardpair[0][2] & shapes[i] != cardpair[1][2]):
      if(shapes[i] != cardpair[0][2]):
        if(shapes[i] != cardpair[1][2]):
          shape = shapes[i]
          break
  if (snumber):
    number = cardpair[1][3]
  else:
    for i in range(3):
      if (numbers[i] != cardpair[0][3]):
        if(numbers[i] != cardpair[1][3]):
          number = numbers[i]
          break
  if (sshading):
    shading = cardpair[1][4]
  else:
    for i in range(3):
      if (shadings[i] != cardpair[0][4]):
        if(shadings[i] != cardpair[1][4]):
          shading = shadings[i]
          break
  
  #creates a card with the attributes
  card = {1:colour,
	  2:shape,
	  3:number,
	  4:shading}
  #printCards(3, card)
  return card


def randomCard():
  """ This function creates a random card, with random attributes
  and return the card (dictionary)
  """
  colours = ["purple", "red", "green"]
  shape = ["squiggle", "oval", "diamond"]
  number = [1, 2, 3]
  shading = ["hollow", "shaded", "lined"]
  card = {1:colours[random.randint(0,2)],
          2:shape[random.randint(0,2)]  ,
          3:number[random.randint(0,2)], 
          4:shading[random.randint(0,2)]}
  return card


def printCards(i, card):
  """ This function prints a card in a readable format.
  """
  print(" Card "+ str(i)+ " :", card[3], card[4], card[1], card[2]+ "s.")



if __name__ == "__main__":
  print("Welcome to group 67: \"SET\" Theory.")

  model = input("Choose a model to explore: \nModel 1 - Given 3 cards, are they a valid set? \nModel 2 - Given 12 cards, how many valid sets are there? \nModel 3 - Given 2 cards, what 3rd card completes a valid set? \nTo exit the program type 'exit': \n Enter a number (as an int): ")
  print("--------------------------------")

  #continues until exit is entered
  while(model != "exit"):

    if(model == "1"):
      print("Model 1: Valid Sets:")
      model1 = input(" Enter 1 for 3 random cards. \n Enter 2 for 3 preset cards\n Enter 3 to set 3 cards. ")
      print("--------------------------------")
      #initalizes 1 list for each sub model
      cardGroup = []

      if(model1 == "1"):
        print("Model 1.1: 3 random cards")

        # Creates a list of 3 different random cards
        #i = 1
        while(len(cardGroup) <3):
          r1 = randomCard()
          if(r1 not in cardGroup):
            cardGroup.append(r1)
          #i += 1

      elif(model1 == "2"):
        print("Model 1.2: 3 preset cards")
        
        card1 = {1:"purple", 2: "squiggle", 3: 3, 4: "lined"}
        card2 = {1:"purple", 2: "oval", 3: 3, 4: "lined"}
        card3 = {1:"purple", 2: "diamond", 3: 3, 4: "lined"}
        
        #cards = [card1, card2, card3]    

        cardGroup = [card1, card2, card3]
        # printCards(1, card1)
        # printCards(2, card2)
        # printCards(3, card3)

      elif(model1 == "3"):
        print("Model 1.3: 3 user set cards")
        for i in range(3):
          print("Card: " + str(i+1))
          c = input(" Colour of card " +str(i+1)+ " (only 'purple' 'red' or 'green'): ")
          s = input(" Shape of card " +str(i+1)+ " (only 'oval' 'diamond' or 'squiggle'): ")
          n = input(" Number of shapes on card "+str(i+1)+ " (only '1' '2' or '3'): ")
          h = input(" Shading of card "+str(i+1)+ " (only 'hollow' 'shaded' or 'lined'): ")
          card = {1:c, 2: s, 3: int(n), 4: h}
          cardGroup.append(card)
          # printCards(i+1, card)
          #print(cardGroup)
        
      else:
        break

      #Print all the cards
      for i in range(3):
        printCards(i+1, cardGroup[i])

      #Tests to see if the cards in "cardGroup" make a valid set
      test = testGroupOf3(cardGroup)
      if(test == True):
        print("These cards are a set.")
      else:
        print("These cards are not a set.")

    elif(model == "2"):
      print("Model 2: How many sets are in 12 cards:")
      model1 = input(" Enter 1 to test 1 group of 12 cards. \n Enter 2 to find the average of n groups of 12 cards. \n Enter 3 to manuallty set 12 cards.")
      print("--------------------------------")

      if(model1 == "1"):
        print("Model 2.1: 1 group of 12 cards")
        c1 = groupsIn12Cards("yes")
        print(" The number of valid sets is", c1)

      elif(model1 == "2"):
        print("Model 2.2: n groups of 12 cards")
        cardsets = input("How many 12 card sets do you want? (Expect a wait for larger numbers): ")

        show = input("Do you want to print the list of cards and sets? 'yes' or 'no' (Suggested no for larger iterations): ")
        print("--------------------------------")
        #finds the avg number of sets for n cards
        sumNumOfSets = 0
        for i in range(int(cardsets)):
          print("Iteration: "+ str(i+1))
          sets = groupsIn12Cards(show)
          if(isinstance(sets, int)):
            sumNumOfSets += sets
        avg = sumNumOfSets/int(cardsets)
        print(" The average number of sets in", cardsets, "groups of 12 cards is:", avg)

      elif(model1 == "3"):
        print("Model 2.3: 12 user set cards")
        
        c1 = userSetGroupsIn12Cards("yes")


      else:
        break
        

    elif(model == "3"):
      print("Model 3: Find the 3rd card ")
      model1 = input(" Enter 1 for 2 random cards. \n Enter 2 for 2 preset cards\n Enter 3 to set 2 cards. ")
      print("--------------------------------")

      #initalizes list for cards for model 3
      cardGroup = []

      if(model1 == "1"):
        print("Model 3.1: 2 random cards")

        #creates 2 different cards
        i = 1
        while(len(cardGroup) <2):
          r1 = randomCard()
          if(r1 not in cardGroup):
            cardGroup.append(r1)
          i += 1


      elif(model1 == "2"):
        print("Model 3.2: 2 preset cards")
        card1 = {1:"purple", 2: "squiggle", 3: 3, 4: "lined"}
        card2 = {1:"purple", 2: "oval", 3: 3, 4: "lined"}
        cardGroup = [card1, card2]

      elif(model1 == "3"):
        print("Model 3.3: 2 user set cards")

        #user created cards
        for i in range(2):
          print("Card: " + str(i+1))
          c = input(" Colour of card " +str(i+1)+ " (only 'purple' 'red' or 'green'): ")
          s = input(" Shape of card " +str(i+1)+ " (only 'oval' 'diamond' or 'squiggle'): ")
          n = input(" Number of shapes on card "+str(i+1)+ " (only '1' '2' or '3'): ")
          h = input(" Shading of card "+str(i+1)+ " (only 'hollow' 'shaded' or 'lined'): ")
          card = {1:c, 2: s, 3: int(n), 4: h}
          cardGroup.append(card)
          
      else:
        break

      #finds the 3rd card 
      test = find3rdCard(cardGroup)
      if(test == True):
        print("These cards are a set.")
      else:
        print("These cards are not a set.")
    print("--------------------------------")


    model = input("Choose a model to explore: \nModel 1 - Given 3 cards, are they a valid set? \nModel 2 - Given 12 cards, how many valid sets are there? \nModel 3 - Given 2 cards, what 3rd card completes a valid set? \nTo exit the program type 'exit': \n Enter a number (as an int): ")
    print("--------------------------------")

  print("Thank you! Sincerely Group 67!")