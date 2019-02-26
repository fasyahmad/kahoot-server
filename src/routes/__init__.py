
from flask import Blueprint
from pathlib import Path

router = Blueprint('router', __name__)

baseLocation = Path(__file__).absolute().parent.parent
from .userRoutes import *
from .quizzesRoutes import *

usersFileLocation = baseLocation / "data"/"registerAccount-file.json"
quizzesFileLocation = baseLocation / "data"/"/quizzes-file.json"
gameFileLocation = baseLocation / "data"/"/games-file.json"


