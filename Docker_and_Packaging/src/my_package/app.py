#先开 后端进行 python3 ./app.py
#再单开一个terminal 输入python3 ./nowclient.py 前端运行
#按control c退出后端
#example username and password:jgqmxjpy. ZPbImfSp
# app.py
from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from auth import Login, Logout, Register, login_manager
from upload import FileUpload

app = Flask(__name__)
app.secret_key = 'your_secret_key'
api = Api(app)

login_manager.init_app(app)

# 添加 RESTful 资源
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Register, '/register')
api.add_resource(FileUpload, '/upload')

# 全局错误处理
@app.errorhandler(Exception)
def handle_exception(e):
    # 如果异常是HTTP异常，返回它的错误信息和状态码
    if isinstance(e, HTTPException):
        return jsonify(error=str(e.description)), e.code
    # 如果不是HTTP异常，返回通用错误信息
    return jsonify(error='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(debug=True)

