from flask import Flask, render_template, request

apl = Flask(__name__)


## Operational Semantics Code 
## Dev: Mikhail Rene Shaw - 1406944
'''
def getBrac(arr):
    bracArr = []
    for x in range(0, len(arr)):
        if arr[x] == '(' or arr[x] == "(":
            print("found")
            #arr[x] = "_"
            for y in range(x + 1, len(arr)):
                print(x + 1, " - ", y)
                print(arr)
                print(arr[y])
                if arr[y] != ')' or arr[y] != ")":
                    bracArr.append(arr[y])
                else:
                    break
            print(bracArr)
            aSize = len(bracArr)
            bracArr = getBrac(bracArr)
            print("Within Brackets(Brac): ", bracArr)
            bracArr = getProd(bracArr)
            print("Within Brackets(Prod): ", bracArr)
            bracArr = getQuot(bracArr)
            print("Within Brackets(Quot): ", bracArr)
            bracArr = getSum(bracArr)
            print("Within Brackets(Sum): ", bracArr)
            bracArr = getDiff(bracArr)
            print("Within Brackets(Diff): ", bracArr)

            arr[y] = "_"

            for y in range(x, len(arr)):
                print("X in underscore replace: ", x)
                if y - x != aSize:
                    arr[y] = "_"
                else:
                    arr[y] = bracArr[len(bracArr) - 1]
                    break

            print("After Brackets: ", bracArr)
            print("After Brackets: ", arr)
            bracArr = []

    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr
'''

def getProd(arr, text, oldAns):
    #print("OG: ",arr)
    
    for x in range(0, len(arr)):
        if arr[x] == '*' or arr[x] == "*":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X * Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) * int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X * Y , θ -> "+a+" * "+b+"  <"+a+" * "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

def getQuot(arr, text, oldAns):
    # text = ""
    #opCount  = 0
    for x in range(0, len(arr)):
        if arr[x] == '/' or arr[x] == "/":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X / Y θ> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(int(arr[x - 1]) / int(arr[x + 1])))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X / Y , θ -> "+a+" / "+b+"  <"+a+" / "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

def getSum(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '+' or arr[x] == "+":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X + Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) + int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X + Y , θ -> "+a+" + "+b+"  <"+a+" + "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

def getDiff(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '-' or arr[x] == "-":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) - int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X - Y , θ -> "+a+" - "+b+"  <"+a+" - "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans


def getPost(text):
    arr = text.split()
    #arr = getBrac(arr)
    
    ans = getProd(arr, "", 'null')
    print("New Array(Prod): ", ans)
    ans = getQuot(ans["array"], ans["text"], ans["old"])
    print("New Array(Quot): ", ans)
    ans = getSum(ans["array"], ans["text"], ans["old"])
    print("New Array(Sum): ", ans)
    ans = getDiff(ans["array"], ans["text"], ans["old"])
    print("New Array(Diff): ", ans)
    

    return ans["text"]

## Operational Semantics Code

@apl.route('/')
def main():
    current_page = "HOME"
    return render_template('root.html')


@apl.route('/opsemantic', methods=["POST","GET"])
def opsemantic():
    if request.method == 'POST':
            oldData =  request.form['data']
            Data = getPost(oldData)
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
