
Score = []
Name = []

def ReadHighScores():
    global Name,Score
    
    try:
        filename = "HighScore.txt"
        file = open(filename,'r')
        for i in range(10):
            name = (file.readline().strip())
            score = int((file.readline().strip()))
            Name.append(name)
            Score.append(score)
 
    except:
        FileNotFoundError
        print("file not found")


def OutPutHighScores():
    global Name,Score

    for i in range(10):
        print(Name[i],Score[i])


ReadHighScores()
OutPutHighScores()

NewName = input("enter a 3 letter name? ")
while len(NewName) != 3:
    NewName = input("please enter a 3 letter name?: ")

NewScore = int(input("enter the score between 1 and 100,000: "))
while NewScore < 1 or NewScore > 100000:
    NewScore = int(input("the score must be between 1 and 100,000: "))

def UpdateScores(nameP,ScoreP):
    global Name,Score

    Name.append(nameP)
    Score.append(ScoreP)
    tempname = ""
    tempscore = 0
    length = len(Name)
    for i in range(length):
        for j in range(i + 1,length):
            if Score[i] < Score[j]:
                tempscore = Score[j]
                Score[j] = Score[i]
                Score[i] = tempscore

                tempname = Name[j]
                Name[j] = Name[i]
                Name[i] = tempname


UpdateScores(NewName,NewScore)
OutPutHighScores()

def WriteTopTen(NameP,ScoreP):
    

    try:
        filename = "NewHighScore.txt"
        file = open(filename,'w')
        for x in range(0,10):
            file.write(str(NameP[x])+ '\n')
            file.write(str(ScoreP[x])+ '\n')
        file.close()

    except:
        FileNotFoundError


WriteTopTen(Name, Score)
