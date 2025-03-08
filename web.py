from flask import Flask,render_template
app = Flask(__name__)
@app.route("/show/info")
def index():
    # return "第一个web 小小应用"
    #打开这个文件，读取内容并返回
    #默认去当前目录的template 文件中找
    return render_template("index.html")
@app.route("/get/news")
def get_news():
    
    return render_template("get_news.html")

if __name__ == "__main__":
    app.run()##运行起来