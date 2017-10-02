from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Landing page
@app.route("/")
def form():
    return render_template('form.html',error="")

# Displays welcome page
@app.route('/welcome', methods=["POST","GET"])
def welcome():
    # Obtain form values
    form_dict = request.args
    name = form_dict['name']
    year = form_dict['year']
    # Check values
    # If invalid, render 'form.html' with error message
    if not year.isdigit() or name.isdigit():
        return render_template('form.html',error="Invalid name or year")
    age = int(year) - 2000
    # Diagnostic print statements
    print "\n\n\n\n"
    print "Print app:"
    print app
    print "Print request.headers:"
    print request.headers
    print "Print request.method:"
    print request.method
    print "Print request.args:"
    print request.args
    #print "Print request.form:"
    #print request.form

    return render_template('welcome.html',
                            NAME = name,
                            YEAR = year,
                            AGE = age)


if __name__ == "__main__":
    app.debug = True
    app.run()





'''
SAMPLE RESPONSES
request.headers
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
    Connection: keep-alive
    Host: localhost:5000
    Upgrade-Insecure-Requests: 1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Language: en-US,en;q=0.8
    Accept-Encoding: gzip, deflate, br


    127.0.0.1 - - [29/Sep/2017 13:17:37] "GET / HTTP/1.1" 302 -
    127.0.0.1 - - [29/Sep/2017 13:17:37] "GET /page HTTP/1.1" 200 -
    127.0.0.1 - - [29/Sep/2017 13:17:39] "GET /page?name=hello&submit=Go%21 HTTP/1.1" 200 -

request.method
    GET
    127.0.0.1 - - [29/Sep/2017 13:19:55] "GET / HTTP/1.1" 302 -
    127.0.0.1 - - [29/Sep/2017 13:19:56] "GET /page HTTP/1.1" 200 -
'''
