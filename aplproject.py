from flask import Flask, render_template, request
import oSemantics

apl = Flask(__name__)


@apl.route('/')
def main():
    current_page = "HOME"
    return render_template('root.html')


@apl.route('/opsemantic', methods=["POST","GET"])
def opsemantic():
    if request.method == 'POST':
            oldData =  request.form['data']
            Data = oSemantics.getPost(oldData)
            #Data = makeOpt(oldData)            
            print("\nData: \n%s", Data)
            return render_template(
                'op_semantic.html', data=Data, eq=oldData)

    return render_template("op_semantic.html", data=False)


@apl.route('/axsemantic')
def axsemantic():
    return render_template("ax_semantic.html")


@apl.route('/desemantic')
def desemantic():
    return render_template("de_semantic.html")


@apl.route('/lambda_calc')
def lambda_calc():
    return render_template("lam_calculus.html")


@apl.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    apl.run()
