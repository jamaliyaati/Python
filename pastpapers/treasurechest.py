class TreasureChest:
    def __init__(self,question,answer,points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self,ans):
        if ans == self.__answer:
            return True
        else:
            return False
    
    def getPoints(self,attempts):
        if attempts == 1:
            return (int(self.__points))
        elif attempts == 2:
            return (int(self.__points) // 2)
        elif attempts == 3 or attempts == 4:
            return (int(self.__points) // 4)
        else:
            return 0


arrayTreasure=[] #of TreasureChest
def readData():
    try:
        file = open("TreasureChestData.txt")
        for x in range(5):
            question = file.readline().strip()
            answer = file.readline().strip()
            points = file.readline().strip()
            object = TreasureChest(question,answer,points)
            arrayTreasure.append(object)
    except IOError:
        print("file not find")

readData()
choice = int(input("enter question number:"))
question = arrayTreasure[choice - 1].getQuestion()
print(question)
answer = input("enter answer: ")
numAttempts = 1
correct = False

while not correct:
    check = arrayTreasure[choice - 1].checkAnswer(answer)
    if not check:
        numAttempts += 1
        answer = input("enter answer: ")
    else:
        correct = True
score = arrayTreasure[choice - 1].getPoints(numAttempts)
print("score: ", score)
