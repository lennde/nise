from wtforms import Form, StringField


class StartForm(Form):
    name = StringField('Study Participant')
