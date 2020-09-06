from flask import Flask, render_template
from flask_restful import Resource, Api
from web.Class.database_util import database

app = Flask(__name__, static_folder='web/static',
            template_folder='web/templates')
api = Api(app)


class test(Resource):
    def get(self, last_name):
        instance = database('DESKTOP-BDJJ3BI\SQLEXPRESS', 'learning')
        cursor = instance.open_con().execute(
            "EXECUTE SelectEmployee @first_nm = null,@last_nm = {};".format(last_name))
        # cursor.execute("EXECUTE SelectEmployee @first_nm = null,@last_nm = {};".format(last_name))
        return instance.jsonify(cursor)


@app.route('/')
def api_documentation():
    return render_template("index.html", title='Projects')


api.add_resource(test, '/search/<string:last_name>')

if __name__ == '__main__':
    app.run(debug=True)
