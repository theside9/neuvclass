import json
import re
import requests
from PIL import Image
import pytesseract


#定义全部链接
host="http://vclass.neusoft.edu.cn/"
report="exam/report/"#答案页后面跟xxx.html，下同
examing="exam/examing/"#考试页
coursepage="course/learn/116.html"#课程页
code="tools/identiry/code.html"#验证码页
index="index.html"#主页
login="auth/ajaxlogin.html"#post登录信息
home="user/home.html"#个人中心
ques="exam/ques.html"#提交答案地址
video="course/video/"#查看视频页面

#初始化session并获取验证码
try:
    session=requests.session()
    img=session.get(host+code)#index不会设置cookies
    cookies=requests.utils.dict_from_cookiejar(img.cookies)
    headers={
    "Host": "vclass.neusoft.edu.cn",
    "Proxy-Connection": "keep-alive",
    "Accept":"*/*",
    "Origin": "http://vclass.neusoft.edu.cn",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://vclass.neusoft.edu.cn/index.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "JSESSIONID="+cookies["JSESSIONID"]
    }
    json_headers={
    "Host": "vclass.neusoft.edu.cn",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "Origin": "http://vclass.neusoft.edu.cn",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "DNT": "1",
    "Content-Type": "application/json",
    "Referer": "http://vclass.neusoft.edu.cn/exam/examing/117.html",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "JSESSIONID="+cookies["JSESSIONID"]
        }

    session.headers=headers

    #保存验证码
    with open('out.jpg', 'wb') as file:
        file.write(img.content)
    img=Image.open('out.jpg')
    img.close
except:
    print("初始化失败，请检查网络设置！")


def get_code():
    global img
    img=session.get(host+code)
    with open('out.jpg', 'wb') as file:
        file.write(img.content)
    img=Image.open('out.jpg')
    img.close


def get_html(url):
    return session.get(url)

def user_login(username="",passwd=""):
    if(username==""):
        username=input("用户名：")
    if(passwd==""):
        passwd=input("密码：")
    #img.show()
    #code=input("输入验证码")#即将机器学习支持
    code = pytesseract.image_to_string(img)#OCR自动识别
    Data="username="+username+"&password="+passwd+"&identiryCode="+code
    Data=bytes(Data,encoding="utf-8")
    req=session.post(host+login,data=Data)
    if json.loads(get_res(req))['errcode'] !=0:
        if(json.loads(get_res(req))['errcode']==2):
            get_code()
            return user_login(username,passwd)
        if(json.loads(get_res(req))['errcode']==1):
            print("用户或密码错误！")
            return user_login()
    return get_course()


def get_res(req):
    print(req)
    return str(req.content,'UTF-8')

def get_course():
    res=session.get(host+coursepage)
   # print(get_res(res))
    coursefind=re.compile('<a href="/course/video/(.*?).html" >')
    course=coursefind.findall(get_res(res))
    return course

def init_getanswer():
    global session
    session.headers=json_headers
    Data={"as":{"0":{"answer":"","point":0},"1":{"answer":"","point":1},"2":{"answer":"","point":2},"3":{"answer":"","point":3},"4":{"answer":"","point":4},"5":{"answer":"","point":5},"6":{"answer":"","point":6},"7":{"answer":"","point":7},"8":{"answer":"","point":8},"9":{"answer":"","point":9},"10":{"answer":"","question_type_id":3,"point":10},"11":{"answer":"","question_type_id":3,"point":11},"12":{"answer":"","question_type_id":3,"point":12},"13":{"answer":"","question_type_id":3,"point":13},"14":{"answer":"","question_type_id":3,"point":14}},"duration":1491,"eid":"942"}
    Data=json.dumps(Data)
    req=session.post(host+ques,data=Data)
#必须先向服务器提交一次题目，才可访问所有题目


def get_answer(eid):
    #findqustype=re.compile("<span>\[(.*?)\]</span>")
    #findanswer=re.compile("<span class=\"answer_value\">(.*?)</span>")
    #findtitle=re.compile("<p class=\"question-body-text\">(.*?)</p>")

    html=get_res(session.get(host+report+eid+".html"))
    html=html.replace(" ","").replace("\n","")
    findalll=re.compile("<span>\[(.*?)\]</span>.*?<pclass=\"question-body-text\">(.*?)</p>.*?<spanclass=\"answer_value\">(.*?)</span>")
    
    a=[]
    a.append(get_title(eid))
    a.append(list(findalll.findall(html)))
    return a

def get_title(eid):
    html=get_res(session.get(host+video+eid+".html"))
    findtitle=re.compile("<div class=\"course-title\" style=\"font-size: 24px;\">(.*?)</div>")
    return findtitle.findall(html)



if __name__=='__main__':
    print("vclass一键答题")
    course=user_login()
    init_getanswer()
    answerlist=[]
    i=1
    #开始获取答案同时答题
    for eid in course:
        answerlist.append(get_answer(eid))
        #i=i+1
        #if i>5:
         #   break

        #print(answerlist[0])
    for i in answerlist:
        print(i[0])
        for t in i[1]:
            print("题型：[",t[0],"] \n题目：",t[1],"\n答案：",t[2],"\n\n")
