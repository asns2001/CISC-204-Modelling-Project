
from nnf import Var, true, false
from lib204 import Encoding
import random



card_colour = {}
card_shape = {}
card_number = {}
card_shading = {}

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

sameShape = Var("sameShape")
sameColour = Var("sameColour")
sameShading = Var("sameShading")
sameNumber = Var("sameNumber")
 
allDiffShape = Var("diffShape")
allDiffColour = Var("diffColour")
allDiffShading = Var("diffShading")
allDiffNumber = Var("diffNumber")
 
winningSet = Var("winningSet")





#
# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    E = Encoding()
    
    for i in [1,2,3]:
       E.add_constraint(card_colour[i,"red"] | card_colour[i,"purple"] | card_colour[i,"green"]) #should we hard code this?
       E.add_constraint(card_shape[i,"oval"] | card_shape[i,"diamond"] | card_shape[i,"squiggle"])
       E.add_constraint(card_shading[i,"hollow"] | card_shading[i,"shaded"] | card_shading[i,"lined"])
       E.add_constraint(card_number[i,1] | card_number[i,2] | card_number[i,3])
   
    E.add_constraint(sameShape.negate() |  (
      (card_shape[1,"oval"] & card_shape[2,"oval"] & card_shape[3,"oval"]) 	|
      (card_shape[1,"diamond"] & card_shape[2,"diamond"] & card_shape[3,"diamond"]) 	|
      (card_shape[1,"squiggle"] & card_shape[2,"squiggle"] & card_shape[3,"squiggle"])
      ))

    E.add_constraint(sameColour.negate() |  (
     (card_colour[1,"red"] & card_colour[2,"red"] & card_colour[3,"red"]) 	|
     (card_colour[1,"green"] & card_colour[2,"green"] & card_colour[3,"green"]) 	|
     (card_colour[1,"purple"] & card_colour[2,"purple"] & card_colour[3,"purple"])
     ))

    E.add_constraint(sameShading.negate() |  (
      (card_shading[1,"hollow"] & card_shading[2,"hollow"] & card_shading[3,"hollow"]) 	|
      (card_shading[1,"shaded"] & card_shading[2,"shaded"] & card_shading[3,"shaded"]) 	|
      (card_shading[1,"lined"] & card_shading[2,"lined"] & card_shading[3,"lined"])
      ))

    E.add_constraint(sameNumber.negate() |  (
      (card_number[1,1] & card_number[2,1] & card_number[3,1]) 	|
      (card_number[1,2] & card_number[2,2] & card_number[3,2]) 	|
      (card_number[1,3] & card_number[2,3] & card_number[3,3])
      ))

    E.add_constraint(allDiffShape.negate() |  (
  	(card_shape[1,"oval"] & card_shape[2,"diamond"] & card_shape[3,"squiggle"]) |
    (card_shape[1,"oval"] & card_shape[2,"squiggle"] & card_shape[3,"diamond"])  |
    (card_shape[1,"squiggle"] & card_shape[2,"oval"] & card_shape[3,"diamond"])  |
    (card_shape[1,"squiggle"] & card_shape[2,"diamond"] & card_shape[3,"oval"])  |
    (card_shape[1,"diamond"] & card_shape[2,"oval"] & card_shape[3,"squiggle"])  |
    (card_shape[1,"diamond"] & card_shape[2,"squiggle"] & card_shape[3,"oval"])  
    ))
 
 
    E.add_constraint(allDiffColour.negate() | (
    (card_colour[1,"red"] & card_colour[2,"purple"] & card_colour[3,"green"]) |
    (card_colour[1,"red"] & card_colour[2,"green"] & card_colour[3,"purple"]) |
    (card_colour[1,"purple"] & card_colour[2,"red"] & card_colour[3,"green"]) |
    (card_colour[1,"green"] & card_colour[2,"purple"] & card_colour[3,"red"]) |
    (card_colour[1,"purple"] & card_colour[2,"green"] & card_colour[3,"red"]) |
    (card_colour[1,"green"] & card_colour[2,"red"] & card_colour[3,"purple"]) 
    ))
 
 
 
    E.add_constraint(allDiffShading.negate() |  (
    (card_shading[1,"hollow"] & card_shading[2,"shaded"] & card_shading[3,"lined"]) |
    (card_shading[1,"hollow"] & card_shading[2,"lined"] & card_shading[3,"shaded"])  |
    (card_shading[1,"lined"] & card_shading[2,"hollow"] & card_shading[3,"shaded"])  |
    (card_shading[1,"lined"] & card_shading[2,"shaded"] & card_shading[3,"hollow"])  |
    (card_shading[1,"shaded"] & card_shading[2,"hollow"] & card_shading[3,"lined"])  |
    (card_shading[1,"shaded"] & card_shading[2,"lined"] & card_shading[3,"hollow"])  
    ))
 
    E.add_constraint(allDiffNumber.negate() |  (
  	(card_number[1,1] & card_number[2,2] & card_number[3,3]) |
    (card_number[1,1] & card_number[2,3] & card_number[3,2]) |
    (card_number[1,2] & card_number[2,1] & card_number[3,3]) |
    (card_number[1,2] & card_number[2,3] & card_number[3,1]) |
    (card_number[1,3] & card_number[2,1] & card_number[3,2]) |
    (card_number[1,3] & card_number[2,2] & card_number[3,1]) 
    ))

    
    E.add_constraint(((sameShape | allDiffShape) & (sameShading | allDiffShading) & (sameColour | allDiffColour) & (sameNumber| allDiffNumber)))
 
 
    return E


def setVarFalse():
  #initalize the stuff false
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
  setVarFalse()
 
  for i in [1,2,3]:
    card_colour[(i,cardGroup[i-1][1])] = true
    card_shape[(i,cardGroup[i-1][2])] = true
    card_number[(i,cardGroup[i-1][3])] = true
    card_shading[(i,cardGroup[i-1][4])] = true


  T = example_theory()
  #print("\nSatisfiable: %s" % T.is_satisfiable())
  #print("# Solutions: %d" % T.count_solutions())
  ##print("   Solution: %s" % T.solve());
  return T.is_satisfiable()


def groupsIn12Cards():
  listofCards = []
  testlist = []
  print("List of 12 random cards: ")
  for i in range(12):
    c1 = randomCard()
    listofCards.append(c1)
    testlist.append(i)
    printCards(i+1, c1)

  count = 0;
  validSet = []
  validSetCards = []
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
    print("Valid set:", i+1)
    for j in range(3):
      #print(validSet[i])
      #print("ooooooooooooooooooo")
      #print(validSet[i][j])
      printCards(validSetCards[i][j], validSet[i][j])
  print("--------------------------------")
  return count



def find3rdCard(cardGroup):
  setVarFalse()
  finalCard = manual3rdCard(cardGroup)
  tempcardGroup = [cardGroup[0],cardGroup[1],finalCard]
  # tempcardGroup.append(finalCard)
  for i in [1,2,3]:
    card_colour[(i,tempcardGroup[i-1][1])] = true
    card_shape[(i,tempcardGroup[i-1][2])] = true
    card_number[(i,tempcardGroup[i-1][3])] = true
    card_shading[(i,tempcardGroup[i-1][4])] = true
    printCards(i, tempcardGroup[i-1])

  T = example_theory()
  #print(T.is_satisfiable)
  return T.is_satisfiable()


def manual3rdCard(cardpair):
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
  print(" Card "+ str(i)+ " :", card[3], card[4], card[1], card[2]+ "s.")



if __name__ == "__main__":
  print("Welcome to group 67: \"SET\" Theory.")


  # card1 = {1:"purple", 2: "squiggle", 3: 3, 4: "lined"}
  # card2 = {1:"purple", 2: "oval", 3: 3, 4: "lined"}
  #     #######
  # cardGroup = [card1, card2]
  # test = find3rdCard(cardGroup)
  # #test = testGroupOf3(cardGroup)
  # if(test == True):
  #   print("These cards are a set.")
  # else:
  #   print("These cards are not a set.")
  # print("--------------------------------")



  model = input("Choose a model to explore: \nModel 1 - Given 3 cards, are they a valid set? \nModel 2 - Given 12 cards, how many valid sets are there? \nModel 3 - Given 2 cards, what 3rd card completes a valid set? \nTo exit the program type 'exit': \n Enter a number (as an int): ")
  print("--------------------------------")
  while(model != "exit"):
    if(model == "1"):
      print("Model 1: Valid Sets:")
      model1 = input(" Enter 1 for 3 random cards. \n Enter 2 for 3 preset cards\n Enter 3 to set 3 cards. ")
      print("--------------------------------")
      cardGroup = []
      if(model1 == "1"):
        print("Model 1.1: 3 random cards")
        r1 = randomCard()
        r2 = randomCard()
        r3 = randomCard()
        cardGroup = [r1, r2, r3]
        printCards(1, r1)
        printCards(2, r2)
        printCards(3, r3)
      elif(model1 == "2"):
        print("Model 1.2: 3 preset cards")
        card1 = {1:"purple", 2: "squiggle", 3: 3, 4: "lined"}
        card2 = {1:"purple", 2: "oval", 3: 3, 4: "lined"}
        card3 = {1:"purple", 2: "diamond", 3: 3, 4: "lined"}
        cardGroup = [card1, card2, card3]
        printCards(1, card1)
        printCards(2, card2)
        printCards(3, card3)
      elif(model1 == "3"):
        print("Model 1.3: 3 user set cards")
        for i in range(3):
          print("Card: " + str(i+1))
          c = input(" Colour of card " +str(i+1)+ " (only 'purple' 'red' or 'green'): ")
          s = input(" Shape of card " +str(i+1)+ " (only 'oval' 'diamond' or 'squiggle'): ")
          n = input(" Number of shapes on card "+str(i+1)+ " (only '1' '2' or '3'): ")
          h = input(" Shading of card "+str(i+1)+ " (only 'hollow' 'shaded' or 'lined'): ")
          card = {1:c, 2: s, 3: n, 4: h}
          cardGroup.append(card)
          printCards(i+1, card)
          #print(cardGroup)

      test = testGroupOf3(cardGroup)
      if(test == True):
        print("These cards are a set.")
      else:
        print("These cards are not a set.")

    elif(model == "2"):
      print("Model 2: How many sets are in 12 cards:")
      model1 = input(" Enter 1 to test 1 group of 12 cards. \n Enter 2 to find the average of n groups of 12 cards. ")
      print("--------------------------------")
      if(model1 == "1"):
        c1 = groupsIn12Cards()
      elif(model1 == "2"):
        cardsets = input(" How many 12 card sets do you want? ")
        sumNumOfSets = 0
        for i in range(int(cardsets)):
          sumNumOfSets += groupsIn12Cards()
        #print("--------------------------------")
        avg = sumNumOfSets/int(cardsets)
        print(" The average number of sets in", cardsets, "groups of 12 cards is:", avg)

        

    elif(model == "3"):
      print("Model 3: Find the 3rd card ")
      model1 = input(" Enter 1 for 2 random cards. \n Enter 2 for 2 preset cards\n Enter 3 to set 2 cards. ")
      print("--------------------------------")
      cardGroup = []
      if(model1 == "1"):
        print("Model 3.1: 2 random cards")
        r1 = randomCard()
        r2 = randomCard()
        #####
        cardGroup = [r1, r2]
        # printCards(1, r1)
        # printCards(2, r2)
        # printCards(3, r3)
      elif(model1 == "2"):
        print("Model 3.2: 2 preset cards")
        card1 = {1:"purple", 2: "squiggle", 3: 3, 4: "lined"}
        card2 = {1:"purple", 2: "oval", 3: 3, 4: "lined"}
        #######
        cardGroup = [card1, card2]
        # printCards(1, card1)
        # printCards(2, card2)
        # printCards(3, card3)
      elif(model1 == "3"):
        print("Model 3.3: 2 user set cards")
        for i in range(2):
          print("Card: " + str(i+1))
          c = input(" Colour of card " +str(i+1)+ " (only 'purple' 'red' or 'green'): ")
          s = input(" Shape of card " +str(i+1)+ " (only 'oval' 'diamond' or 'squiggle'): ")
          n = input(" Number of shapes on card "+str(i+1)+ " (only '1' '2' or '3'): ")
          h = input(" Shading of card "+str(i+1)+ " (only 'hollow' 'shaded' or 'lined'): ")
          card = {1:c, 2: s, 3: n, 4: h}
          cardGroup.append(card)
          # printCards(i+1, card)
          #print(cardGroup)

      # for i in range(3):
      #   print("pppp")
      #   printCards(i+1, cardGroup[1])

      test = find3rdCard(cardGroup)
      #print(test)
      if(test == True):
        print("These cards are a set.")
      else:
        print("These cards are not a set.")
    print("--------------------------------")
    model = input("Choose a model to explore: \nModel 1 - Given 3 cards, are they a valid set? \nModel 2 - Given 12 cards, how many valid sets are there? \nModel 3 - Given 2 cards, what 3rd card completes a valid set? \nTo exit the program type 'exit': \n Enter a number (as an int): ")
    print("--------------------------------")

  print("Thank you! Sincerley Group 67!")

