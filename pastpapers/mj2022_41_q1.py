Score = []
Name = []

def ReadHighScores():
    global Name, Score

    try:
        with open("HighScore.txt", "r") as file:
            while True:
                name = file.readline().strip()
                if not name:   # EOF reached
                    break
                score = file.readline().strip()

                Name.append(name)
                Score.append(int(score))

    except FileNotFoundError:
        print("File not found: creating new high score list.")


def OutPutHighScores():
    global Name, Score

    print("\n--- HIGH SCORES ---")
    for i in range(len(Name)):
        print(Name[i], Score[i])


ReadHighScores()
OutPutHighScores()

# --- INPUT NEW SCORE ---
NewName = input("Enter a 3 letter name: ").upper()
while len(NewName) != 3:
    NewName = input("Please enter exactly 3 letters: ").upper()

while True:
    try:
        NewScore = int(input("Enter the score between 1 and 100000: "))
        if 1 <= NewScore <= 100000:
            break
        else:
            print("Score must be between 1 and 100000.")
    except ValueError:
        print("Please enter a number.")


def UpdateScores(nameP, scoreP):
    global Name, Score

    Name.append(nameP)
    Score.append(scoreP)

    # SORT SCORES (DESCENDING)
    length = len(Name)
    for i in range(length):
        for j in range(i + 1, length):
            if Score[i] < Score[j]:
                Score[i], Score[j] = Score[j], Score[i]
                Name[i], Name[j] = Name[j], Name[i]

    # KEEP ONLY TOP 10
    del Name[10:]
    del Score[10:]


UpdateScores(NewName, NewScore)
OutPutHighScores()


def WriteTopTen(NameP, ScoreP):
    try:
        with open("NewHighScore.txt", "w") as file:
            for x in range(len(NameP)):
                file.write(NameP[x] + "\n")
                file.write(str(ScoreP[x]) + "\n")

    except Exception as e:
        print("Error writing file:", e)


WriteTopTen(Name, Score)
