from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommandForm(Form):
  minion = TextField("Minion", validators=[DataRequired()])
  module = TextField("Module", validators=[DataRequired()])
  args = TextField("Arguments", validators=[DataRequired()])
  submit = SubmitField("Send")
