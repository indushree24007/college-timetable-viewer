from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/timetable')
def timetable():

    timetable_data = [
        {"day": "Monday", "subject": "Math", "time": "9 AM"},
        {"day": "Tuesday", "subject": "Physics", "time": "10 AM"},
        {"day": "Wednesday", "subject": "Chemistry", "time": "11 AM"},
        {"day": "Thursday", "subject": "Biology", "time": "12 PM"},
        {"day": "Friday", "subject": "Computer Science", "time": "1 PM"}
    ]

    return render_template('timetable.html', data=timetable_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)