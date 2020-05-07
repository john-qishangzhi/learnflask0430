from flask import Flask, url_for, escape, send_from_directory, render_template, redirect

app = Flask(__name__)

app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')


@app.route('/')
def hello_world():
    return redirect(url_for('test_tiaozhuan'))


@app.route('/test/tiaozhuan')
def test_tiaozhuan():
    return redirect('https://www.zhihu.com/')


@app.route('/version/<name>')
def hello_test(name=None):
    return 'Hello ' + name


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/uploads/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    # return 'Subpath %s' % str(subpath)
    return send_from_directory('download', subpath)


# 重定向
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# 重定向 url_for()用于构建指定函数的 URL。它把函数名称作为第一个 参数。
# 它可以接受任意个关键字参数，每个关键字参数对应 URL 中的变量。未知变量 将添加到 URL 中作为查询参数
# @app.route('/')
# def index():
#     return 'index'
#
#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


# 使用模板渲染

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0")

# 稍后看看sqlite
# https://dormousehole.readthedocs.io/en/latest/quickstart.html#id2
# ETL，是英文Extract-Transform-Load的缩写，用来描述将数据从来源端经过抽取（extract）、转换（transform）、加载（load）至目的端的过程。
# ETL一词较常用在数据仓库，但其对象并不限于数据仓库

# https://dormousehole.readthedocs.io/en/latest/patterns/fileuploads.html#uploading-files
