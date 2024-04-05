from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    crop = request.form['crop']
    pest = request.form['pest']
    solution = request.form['solution']

    if not crop or not pest or not solution:
        error_message = 'All fields are required.'
        return render_template('index.html', entries=entries, error_message=error_message)

    entries.append({'crop': crop, 'pest': pest, 'solution': solution})

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)