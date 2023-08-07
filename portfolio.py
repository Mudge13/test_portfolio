from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as database:
        database.write(
            f'\nemail: {email}, subject: {subject}, message: {message}')


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    csv_data = [email, subject, message]
    with open('database.csv', 'a', newline='') as database2:
        csv_write = csv.writer(database2, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(csv_data)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:pagename>")
def my_home_return(pagename):
    return render_template(pagename)


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         msg = request.form['message']
#         print(data)
#         return redirect(f'/thankyou.html/{msg}')
#     else:
#         return "something went wrong, try again"


# @app.route("/thankyou.html/<msg>")  #does not show proper js and css
# def thank_you(msg=None):
#     return render_template("thankyou.html", message=msg)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return "something went wrong, try again"

# @app.route('/thankyou.html', methods=['POST', 'GET'])
# def thankyou():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         msg = request.form['message']
#         print(data)
#         # Process the form data if needed

#     # Render the "Thank You" page
#     return render_template('thankyou.html', message=msg)
