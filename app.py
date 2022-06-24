from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html")
    

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict()
        # print(args_dict)
       
        return "GET으로 전달된 데이터"
    else:
        url = request.form["url"]
        
        return f"POST <img src = '{url}'>"

if __name__ == '__main__':
    app.run(debug=True)
