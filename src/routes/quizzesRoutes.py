from flask import Flask, request, json, jsonify
from random import randint
import requests
import os
from . import router, baseLocation
from ..utils.crypt import encrypt
from 


# bikin kuis baru
@router.route('/quiz', methods=['POST'])
def createQuiz():
    body = request.json

    quizData = {
        "totalQuizAvailable": 0,
        "quizzes": []
    }

    if os.path.exists(quizzesFileLocation):
        quizzesFile = open(quizzesFileLocation, 'r')
        quizData = json.load(quizzesFile)
    else:
        quizzesFile = open(quizzesFileLocation, 'x')

    quizData["totalQuizAvailable"] += 1
    quizData["quizzes"].append(body)

    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(quizData))

    return jsonify(quizData)

# meminta data kuis dan soalnya
@app.route('/quizzes/<quizId>')  # kalau gaada methodnya itu defaulnya ["GET"]
def getQuiz(quizId):
    # nyari quiznya
    quizzesFile = open(quizzesFileLocation)
    quizzesData = quizzesFile  # kalo load itu dari file

    for quiz in quizzesData["quizzes"]:
        quiz = json.loads(quiz)  # sedangkan loads itu dari string
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open(questionFileLocation)
    questionsData = questionsFile

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)


# meminta data kuis dan soalnya
@app.route('/quizzes/<quizId>', methods=["DELETE"])  # kalau gaada methodnya itu defaulnya ["GET"]
def deleteQuiz(quizId):
    # nyari quiznya
    quizzesFile = open(quizzesFileLocation)
    quizzesData = quizzesFile  # kalo load itu dari file

    for i in range(len(quizzesData["quizzes"])):
        if i["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open(questionFileLocation)
    questionsData = questionsFile

    for question in questionsData["questions"]:
        question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)
