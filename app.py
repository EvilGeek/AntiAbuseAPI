# using flask_restful
from flask import *
#from helper import *
# from flask_restful import Resource, Api, reqparse

# creating the flask app
app = Flask(__name__)


# function to get file contents
def get_content(filepath):
    with open(filepath, 'r') as f:
        lines = set()       # using sets to avoid duplicate enteries
        for line in f:
            lines.add(line.strip())
    return list(lines)
   # return {'words': list(lines)}

def rmSpCh(text):
    cha = ['+','*',':',';','!','?','/','\\','_','-','|','.',',','@','#','$','%','=']
    for s in cha:
        text=text.replace(s, '')
    return text
    
def checker(text):
    abuses = get_content("cuss_words.txt")
    mlist = text.split()
    for w in mlist:
        if w in abuses:
            p=True
            break
        else:
            p=False
    return p
        
@app.route('/', methods=['POST', 'GET'])
def home():
    return 'CodentX'

@app.route('/api', methods=['POST', 'GET'])
def abuseapi():
    abuses = get_content("cuss_words.txt")
    return jsonify(words=abuses)

@app.route('/api/check', methods=['POST', 'GET'])
def check():
    text = request.args.get('text')
    if text!=None:
        text=rmSpCh(text)
        check=checker(text)
        if check==True:
            return jsonify(response=True)
        else:
            return jsonify(response=False)
    else:
        return jsonify(response=False)

@app.errorhandler(404)
def notf():
    return 'Not Found'

# driver function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
