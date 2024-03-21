#先开 后端进行 python3 ./app.py
#再单开一个terminal 输入python3 ./nowclient.py 前端运行
#按control c退出后端
# app.py
from flask import Flask
from flask_restful import Api
from auth import Login, Logout, login_manager
from upload import FileUpload

app = Flask(__name__)
app.secret_key = 'your_secret_key'
api = Api(app)

login_manager.init_app(app)

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(FileUpload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
