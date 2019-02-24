from flask import Flask, request, json, jsonify
from random import randint
import requests
import os
app = Flask(__name__)


# bikin kuis baru
@app.route('/quiz', methods=['POST'])
def createQuiz():
    body = json.dumps(request.json)

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }

    if os.path.exists('./quizzes-file.json'):
        quizzesFile = open('./quizzes-file.json', 'r')
        quizData = json.load(quizzesFile)
    else:
        quizzesFile = open('./quizzes-file.json', 'x')

    quizData["totalQuizAvailable"] += 1
    quizData["quizzes"].append(body)

    quizzesFile = open('./quizzes-file.json', 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return str(quizData)

# bikin soal untuk kuis yang udah ada
@app.route('/question', methods=['POST'])
def createQuestion():
    body = json.dumps(request.json)  # untuk merubah dari ('') menjadi ("")

    questionData = {
        "questions": []
    }

    if os.path.exists('./question-file.json'):
        questionFile = open('./question-file.json', 'r')
        print("File ada")
        questionData = json.load(questionFile)
    else:
        questionFile = open('./question-file.json', 'x')
        print("file ga ada")

    questionFile = open('./question-file.json', 'w')
    questionData["questions"].append(body)
    questionFile.write(str(json.dumps(questionData)))

    return str(questionData)

# meminta data kuis dan soalnya
@app.route('/quizzes/<quizId>')  # kalau gaada methodnya itu defaulnya ["GET"]
def getQuiz(quizId):
    # nyari quiznya
    quizzesFile = open('./quizzes-file.json')
    quizzesData = json.load(quizzesFile)  # kalo load itu dari file

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)  # sedangkan loads itu dari string
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open('./question-file.json')
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

# minta data sebuah soal untuk kuis tertentu
@app.route('/quizzes/<quizId>/questions/<questionNumber>')
def getThatQuestion(quizId, questionNumber):
    quizData = getQuiz(int(quizId)).json

    for question in quizData["question-list"]:
        if question["question-number"] == int(questionNumber):
            return jsonify(question)


# bikin game baru
@app.route('/game', methods=["POST"])
def createGame():
    body = request.json

    # dapetin info quiz
    quizzesFile = open('./quizzes-file.json')
    quizzesData = json.load(quizzesFile)

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)

        if quiz["quiz-id"] == int(body["quiz-id"]):
            gameInfo = quiz

    gameInfo["game-pin"] = randint(100000, 999999)
    gameInfo["user-list"] = []
    gameInfo["leaderboard"] = []

    # create skeleton for list of game buat nulis
    # kalau belum pernah main game sama sekali
    gamesData = {
        "game-list": []
    }

    # simpen data game nya
    if os.path.exists('./games-file.json'):
        gamesFile = open('./games-file.json', 'r')
        gamesData = json.load(gamesFile)
    else:
        gamesFile = open('./games-file.json', 'x')

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"].append(gameInfo)
        gamesFile.write(str(json.dumps(gamesData)))

    return jsonify(gameInfo)


@app.route('/game/join', methods=["POST"])
def joinGame():
    body = request.json

    # open game data information
    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    position = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == int(body["game-pin"]):
            if body["username"] not in game["user-list"]:
                game["user-list"].append(body["username"])
                game["leaderboard"].append({"username": body["username"],"score": 0})
                gameInfo = game
                position = i
                break
            # TODO: error kalau usernya udah dipake

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"][position] = gameInfo
        gamesFile.write(str(json.dumps(gamesData)))

    return jsonify(request.json)


#
# 1. harus ada soalnya
# 2. ada pilihan jawabannya
# 3. identitas soalnya jelas
# 4. yang jawabnya juga tau siapa
# 5. si jawabannya
# 6. pin game nya
#

@app.route('/game/answer', methods=["POST"])
def submitAnswer():
    isTrue = False
    body = request.json

    # buka file question
    questionsFile = open('./question-file.json')
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        question = json.loads(question)

        if question["quiz-id"] == int(body["quiz-id"]) and question["question-number"] == int(body["question-number"]):
            if question["answer"] == body["answer"]:
                isTrue = True

    # TODO : update skor/Leaderboard
    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    gamePosition = 0
    for i in range(len(gamesData["game-list"])):
        game = gamesData["game-list"][i]

        if game["game-pin"] == body["game-pin"]:
            if isTrue:
                userPosition = 0
                for j in range(len(game["leaderboard"])):
                    userData = game["leaderboard"][j]

                    if userData["username"] == body["username"]:
                        userData["score"] += 100
                        print(userData)

                        userInfo = userData
                        userPosition = j
                        break

                game["leaderboard"][userPosition] = userInfo
                gameInfo = game
                gamePosition = i
                break

    with open('./games-file.json', 'w') as gamesFile:
        gamesData["game-list"][gamePosition] = gameInfo
        gamesFile.write(str(json.dumps(gamesData)))

    return jsonify(request.json)


@app.route('/game/leaderboard', methods=["POST"])
def getLeaderboard():
    body = request.json

    gamesFile = open('./games-file.json')
    gamesData = json.load(gamesFile)

    for game in gamesData["game-list"]:
        if game["game-pin"] == body["game-pin"]:
            leaderboard = game["leaderboard"]

    i = 0
    while (i < len(leaderboard)):
        for j in range(len(leaderboard)-i-1):
            if (leaderboard[j]["score"] < leaderboard[j+1]["score"]):
                leaderboard[j+1], leaderboard[j] = leaderboard[j], leaderboard[j+1]
        i += 1

    return jsonify(leaderboard)


# Member Register ======================================
@app.route('/register', methods=['POST'])
def creatAccount():
    body = request.json

    if body["skidipaw"] == "encrypt":
        body["password"] = encrypt(body["password"])
    elif body["skidipaw"] == "decrypt":
        body["password"] == decrypt(body["password"])

    registerAccountData = {
        "registerAccount": []
    }

    if os.path.exists('./registerAccount-file.json'):
        registerAccountFile = open('./registerAccount-file.json', 'r')
        registerAccountData = json.load(registerAccountFile)
    else:
        registerAccountFile = open('./registerAccount-file.json', 'x')

    # quizData["totalQuizAvailable"] += 1
    registerAccountData["registerAccount"].append(body)

    registerAccountFile = open('./registerAccount-file.json', 'w')
    registerAccountFile.write(str(json.dumps(registerAccountData)))

    return str(registerAccountData)


# Member log-in ======================================
@app.route('/log-in', methods=["POST"])
def logIn():
    body = request.json

    if body["skidipaw"] == "encrypt":
        body["password"] = encrypt(body["password"])
    elif body["skidipaw"] == "decrypt":
        body["password"] == decrypt(body["password"])

    # buka file yang udah register ========================
    registerAccountFile = open('./registerAccount-file.json')
    registerAccountData = json.load(registerAccountFile)
    # cari account yang udah register =====================
    for i in range(len(registerAccountData["registerAccount"])):
        userAccount = registerAccountData["registerAccount"][i]
        if userAccount["username"] == body["username"]:
            if userAccount["password"] == body["password"]:
                return 'selamat anda berhak mendapatkan account anda'
                break
            else:
                return "semudah itu kamu melupakanku"
    
# encrypt passwor======================================
chaisarMove = 2
def encrypt(secretMessage):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listCharts = list(chars)

  listSecretMessage = list(secretMessage)
#   print(listCharts)
#   print("=============")
#   print(listSecretMessage)

  for i in range(len(listSecretMessage)):
    indexChar = listCharts.index(listSecretMessage[i])
    changeChar = (indexChar+chaisarMove) % len(chars)
    listSecretMessage[i] = listCharts[changeChar]
  return "".join(listSecretMessage)


# decrypt passwor======================================


def decrypt(secretMessage):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listCharts = list(chars)

  listSecretMessage = list(secretMessage)
#   print(listCharts)
#   print("=============")
#   print(listSecretMessage)

  for i in range(len(listSecretMessage)):
    indexChar = listCharts.index(listSecretMessage[i])
    changeChar = (indexChar-chaisarMove) % len(chars)
    listSecretMessage[i] = listCharts[changeChar]
  return "".join(listSecretMessage)

# if name == "__main__":
# app.run(debug=True, port=14045)
#coba rubah dikit tjoy