import re

def replaceStr(str, find, replace):
        #reg = re.compile(r"^.*"+find[i]+"*$", re.IGNORECASE)
        #opReg = re.compile(r"^.*[-&\/\\#,+$~%.'\":*?<>]*$", re.IGNORECASE)
        for x in range(0,len(find)):
            str =  str.replace(find[x],replace[x])
            #str = re.sub("^.*[-&\/\\#,+$~%.'\":*?<>]*$",'.',str) #str.replace(\[-&\/\\#,+$~%.'":*?<>]\\g,'.')
            str = str.replace("*" or "+" or "-" or "/", '.')
        
        return str


def calculate(text):
    ex = eval(text)
    data1 = data2 = data3 = data4 = data5 = ""

    if "+" in text:
        data1 = "Addition:   λm.λn.λf.λx m f(n f x) "
    
    if "-" in text:
        data2 = "Subtraction:   λm.λn.n pred m"

    if "*" in text:
        data3 = "Multiply:   λm.λn.λf.λx.m(n f)x"

    if "/" in text:
        data4 = "Division:  (λn.((λf.(λx.x x) (λx.f (x x))) (λc.λn.λm.λf.λx.(λd.(λn.n (λx.(λa.λb.b)) (λa.λb.a)) d ((λf.λx.x) f x) (f (c d m f x))) ((λm.λn.n (λn.λf.λx.n (λg.λh.h (g f)) (λu.x) (λu.u)) m) n m))) ((λn.λf.λx. f (n f x)) n))"

    
    find = ["0","1","2","3","4","5","6","7","8","9"]
    strReplace = ['0-λf.λx.x. ','1-λf.λx.f x ','2-λf.λx.f(f x)','3-λf.λx.f(f(f x))','4-λf.λx.f(f(f(f x)))','5-λf.λx.f(f(f(f(f x))))','6-λf.λx.f(f(f(f(f(f x)))))','7-λf.λx.f(f(f(f(f(f(f x))))))','8-λf.λx.f(f(f(f(f(f(f(f x)))))))','9-λf.λx.f(f(f(f(f(f(f(f(f x))))))))']

    text1 = replaceStr(text, find, strReplace)

    find = ["1","2","3","4","5","6","7","8","9",'0','10']
    strReplace = ['λa','λb','λc','λd','λe','λf','λg','λh','λi','λj','λk']

    text2 = replaceStr(text, find, strReplace)


    Data = {
        "1":data1,
        "2":data2,
        "3":data3,
        "4":data4,
        "t1":text1,
        "t2":text2,
        "ex": ex
    }
    return Data

    