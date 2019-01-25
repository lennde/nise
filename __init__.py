from flask import Flask, g, session, request
from flask import render_template

from nise.controller import Context
from nise.forms import StartForm

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
        return render_template("experiment.html", participant=participant, sound_planning=sound_planning)
    return render_template("welcome.html", form=form)


if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True, port=5000)
