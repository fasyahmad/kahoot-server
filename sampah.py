@app.route('/codewars/history')
def getSearchHistory():
    historyFile = open("history-user", 'r')
    return historyFile.read()


@app.route('/codewars/<username>')
def getUserInfo(username):
    historyFile = open("history-user", 'a')
    historyFile.write(username)
    historyUser.append(username)

    data = requests.get("https://www.codewars.com/api/v1/users/%s" % username)
    theName = data.json()["name"]
    theHonor = data.json()["honor"]
    result = "Saya yang bernama %s mempunyai nilai %s" % (theName, theHonor)

    return result


@app.route('/')  # example = google.com
def home():
    return "<h1>Pulang Kuuyyy</h1>"


@app.route('/jam-pulang')
def jamPulang():
    return "Sekarang sudah saatnya"


@app.route('/kalkulator-sederhana/<numb1>/<numb2>')
def summation(numb1, numb2):
    numb1 = int(numb1)
    numb2 = int(numb2)

    result = numb1 + numb2
    return str(result)


@app.route('/kalkulator-sederhana')
def pengurangan():
    numb1 = request.args.get('numb1')
    numb2 = request.args.get('numb2')

    numb1 = int(numb1)
    numb2 = int(numb2)

    result = numb1 - numb2
    return str(result)
