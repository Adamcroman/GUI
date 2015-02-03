from wtforms import Form, TextField, TextAreaField, SubmitField

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Messsage")
  submit = SubmitField("Send")
