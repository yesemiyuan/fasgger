# 项目简介

## flasgger环境配置
首先需要安装flasgger，网上很多教程说需要更新setuptools到最新版本，目前未发现其必要性，所以直接安装flasgger

    pip install flasgger
flasgger也适用于RESTful接口，只需要安装flask_restful

    pip install flask_restful

不论运行单个文件还是项目整体，在对应的app = Flask(__name__)下面添加代码

    Swagger(app)
然后运行时就可以查看接口文档了，默认地址是http://localhost:5000/apidocs/

## flasgger使用
#### 单文件运行
1.注释处用yaml格式说明接口内容，tags可以为你的接口分组，parameters放置你的请求参数，responses放置返回内容，
参考文件restful.py

2.创建yaml文件，可以通过配置查找，参考文件colors.py，也可以使用swag_from导入

3.创建json文件，本项目无该案例，读者可自行查阅资料

#### 查看项目接口
由于关于flasgger在项目运行中的案例太少，本项目仅试验了多个文件整理接口文档，未进行任何配置

注意：接口文档写在注释中时，该接口文档未识别

所以本项目在run.py中运行的接口均是通过swag_from导入

运行项目，就可以在http://localhost:5000/apidocs/查看接口文档了