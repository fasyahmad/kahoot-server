from flask import Flask, request, json, jsonify
from random import randint
import requests
import os
from . import router, baseLocation
from ..utils.crypt import encrypt




@router.route('/alala')
def alala():
    return "sampe"

# Member Register ======================================
@router.route('/register', methods=['POST'])
def creatAccount():
    body = request.json

    if body["skidipaw"] == "encrypt":
        body["password"] = encrypt(body["password"])
    elif body["skidipaw"] == "decrypt":
        body["password"] == decrypt(body["password"])

    registerAccountData = {
        "registerAccount": []
    }

    if os.path.exists(usersFileLocation):
        registerAccountFile = open(usersFileLocation, 'r')
        registerAccountData = json.load(registerAccountFile)
    else:
        registerAccountFile = open(usersFileLocation, 'x')

    # quizData["totalQuizAvailable"] += 1
    registerAccountData["registerAccount"].append(body)

    registerAccountFile = open(usersFileLocation, 'w')
    registerAccountFile.write(str(json.dumps(registerAccountData)))

    return jsonify(registerAccountData)

