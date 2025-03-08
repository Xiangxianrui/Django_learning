# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/show/info")
# def index():
#     return render_template("index.html")

# @app.route("/get/news")  # 访问路径：http://localhost:5000/get/news
# def get_news():
#     return render_template("get_news.html")

# @app.route("/goods/list")  # 新增商品列表路由，访问路径：http://localhost:5000/goods/list
# def goods_list():
#     return render_template("goods_list.html")

# if __name__ == "__main__":
#     app.run(debug=True)  # 开启调试模式
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/show/info")
def index():
    return render_template("index.html")  # 确保文件名一致

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")  # 确保文件存在

@app.route("/goods/list")  # 路由定义正确
def goods_list():
    return render_template("goods_list.html")  # 关键修正4：检查文件名是否完全一致

if __name__ == "__main__":
    app.run(debug=True)  # 关键修正5：开启调试模式