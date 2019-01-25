from flask import Flask, g, request
from flask import render_template

from controller import Context
from forms import StartForm

import json

server = Flask(__name__)
server.secret_key = 'dAdinai99adn9N)Dna9d'
server.config['UPLOAD_FOLDER'] = "static/uploads"


@server.before_first_request
def before_first():
    Context().setup()


@server.before_request
def initialize():
    g.env = Context()


@server.route("/", methods=['GET', 'POST'])
def index():
    form = StartForm(request.form)
    if request.method == 'POST':
        # Create Participant and Sound Planning
        participant = g.env.create_participant(form.name.data)
        sound_planning = g.env.generate_sounds(participant.studyparticipant_id)
        return render_template("experiment.html", participant=participant)
    return render_template("welcome.html", form=form)


@server.route("/sound_planning/<participant_id>")
def sound_planning(participant_id):
    return json.dumps({ "sound_planning": g.env.get_sound_planning(participant_id)})


if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True, port=5050)
