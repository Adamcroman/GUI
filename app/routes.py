from flask import Flask, render_template, request, flash
from forms import CommandForm
from subprocess import call

app = Flask(__name__)

app.secret_key = 'p1n3M@rtin'

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/commands', methods=['GET', 'POST'])
def commands():
  form = CommandForm()
  if form.validate_on_submit():
    flash('minion="%s", module="%s", command="%s"' %
      (form.minion, form.module, form.command))
    return redirect('/index')
  return render_template('commands.html', title='Submit Command', form=form)

@app.route('/vltdevrestart')
def vltdevrestart():
  call = subprocess.call("sudo supervisorctl restart all"  , shell=True)

#  if request.method == 'POST':
#    return 'Form Posted'
#
#  elif request.method == 'GET':
#    return render_template('commands.html', form=form)

 
if __name__ == '__main__':
  app.run(debug=True)

