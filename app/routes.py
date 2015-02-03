from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'p1n3M@rtin'
#@app.before_request
#def csrf_protect():
#  if request.method == "POST":
#    token = session.pop('_csrf_token', None)
#    if not token or token != request.form.get('_csrf_token'):
#      abort(403)

#def generate_csrf_token():
#  if '_csrf_token' not in sesssion:
#    session['_csrf_token'] = some_random_string()
#  return session['_csrf_token']

#app.jinja_env.globals['csrf_token'] = generate_csrf_token

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    return 'Form Posted'

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
 
if __name__ == '__main__':
  app.run(debug=True)

