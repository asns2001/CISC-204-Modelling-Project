
from nnf import Var, true, false
from lib204 import Encoding
import random

# Call your variables whatever you want
# shape1 = Var("s1")
# shape2 = Var("s2")
# shape3 = Var("s3")
# colour1 = Var("c1")
# colour2 = Var("c2")
# colour3 = Var("c3")
# shading1 = Var("p1")
# shading2 = Var("p2")
# shading3 = Var("p3")
# number1 = Var("n1")
# number2 = Var("n2")
# number3 = Var("n3")


# class Card(object):
#   def __init__(self, shape, colour, shading, number):
#     self.shape = shape
#     self.colour = colour
#     self.shading = shading
#     self.number = number

# card1 = Card("oval", "red", "hollow", 1)
# card2 = Card("oval", "purple", "hollow", 1)
# card2 = Card("oval", "green", "hollow", 1)
#var_card1 = Var(card1)

# a = Var('a')
# b = Var('b')
# c = Var('c')
# x = Var('x')
# y = Var('y')
# z = Var('z')

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
    # E.add_constraint()
    # E.add_constraint(a | b)
    # E.add_constraint(~a | ~x)
    # E.add_constraint(c | y | z)
    # return E
    for i in [1,2,3]:
       E.add_constraint(card_colour[i,"red"] | card_colour[i,"purple"] | card_colour[i,"green"]) #should we hard code this?
       E.add_constraint(card_shape[i,"oval"] | card_shape[i,"diamond"] | card_shape[i,"squiggle"])
       E.add_constraint(card_shading[i,"hollow"] | card_shading[i,"shaded"] | card_shading[i,"lined"])
       E.add_constraint(card_number[i,1] | card_number[i,2] | card_number[i,3])
    
    #E.add_constraint(((card1.shape != card2.shape) & (card1.shape != card3.shape) & (card2.shape != card3.shape)) | ((card1.shape == card2.shape) & (card2.shape == card3.shape)))
   
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

    # E.add_constraint(winningSet.negate() |  ((sameShape | allDiffShape) & (sameShading | allDiffShading) & (sameColour | allDiffColour) & (sameNumber| allDiffNumber)))
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
  # for i in [1,2,3]:

  setVarFalse()
 
  for i in [1,2,3]:
    # print(cardGroup[i-1][1])
    # print(cardGroup[i-1][2])
    card_colour[(i,cardGroup[i-1][1])] = true
    card_shape[(i,cardGroup[i-1][2])] = true
    card_number[(i,cardGroup[i-1][3])] = true
    card_shading[(i,cardGroup[i-1][4])] = true


  # 3 purple, squiggle, lined
  # card_colour[(1,"purple")] = true
  # card_shape[(1,"squiggle")] = true
  # card_number[(1,3)] = true
  # card_shading[(1,"lined")] = true
  # 3 purple, oval, lined
  # card_colour[(2,"purple")] = true
  # card_shape[(2,"oval")] = true
  # card_number[(2,3)] = true
  # card_shading[(2,"lined")] = true
  # 3 purple, diamond, lined
  # card_colour[(3,"purple")] = true
  # card_shape[(3,"oval")] = true
  # card_number[(3,3)] = true
  # card_shading[(3,"lined")] = true

  #print(cardGroup[0][2])
  #print(cardGroup[1][2])
  #print(cardGroup[2][2])
  T = example_theory()
  #print("\nSatisfiable: %s" % T.is_satisfiable())
  #print("# Solutions: %d" % T.count_solutions())
  ##print("   Solution: %s" % T.solve());
  return T.is_satisfiable()


def groupsIn12Cards():
  #creates 12 random cards: 
  print()
  listofCards = []
  testlist = []
  print("List of 12 random cards: ")
  for i in range(12):
    c1 = randomCard()
    listofCards.append(c1)
    testlist.append(i)
    printCards(i+1, c1)

  
  #print(listofCards)

  count = 0;
  for x in range(12):
    for y in range(x+1,12):
      for z in range(y+1,12):
        sat = testGroupOf3([listofCards[x], listofCards[y], listofCards[z]])
        #print(testlist[x], testlist[y], testlist[z])
        if(sat == True):
          count = count + 1
  
  print("There are", count, "solutions")




  
  


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
  print("Card "+ str(i)+ " :", card[3], card[4], card[1], card[2]+ "s.")





if __name__ == "__main__":
    print("Test1")
    c1 = groupsIn12Cards()
    #print(c1)
    print("Test")
    card1 = {1:"purple", 
             2: "squiggle",
             3: 3,
             4: "lined"}
    card2 = {1:"purple", 
             2: "oval",
             3: 3,
             4: "lined"}
    card3 = {1:"purple", 
             2: "diamond",
             3: 3,
             4: "lined"}

    cardGroup = [card1, card2, card3]
    print("yeee")
    p = testGroupOf3(cardGroup)
    print(p, "done")
    #T = example_theory()

    #print("\nSatisfiable: %s" % T.is_satisfiable())
    #print("# Solutions: %d" % T.count_solutions())
    #print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     print(" %s: %.2f" % (vn, T.likelihood(v)))
    print()
