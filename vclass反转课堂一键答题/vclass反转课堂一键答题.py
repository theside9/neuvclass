import json
import re
import requests
from PIL import Image
import pytesseract
import random
import getpass

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
point="exam/getResult.html"#查看分数

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
	try:
		if(username==""):
			username=input("用户名：")
		if(passwd==""):
			passwd=getpass.getpass("请输入你的密码（不会显示，正常输入后回车即可）：")
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
	except:
		print("服务器有毛病，重试")
		user_login(username,passwd)


def get_res(req):
	return str(req.content,'UTF-8')

		
def get_course():
	try:
		res=session.get(host+coursepage)
		coursefind=re.compile('<a href="/course/video/(.*?).html" >')
		course=coursefind.findall(get_res(res))
		print(course)
		return course
	except:
		print("服务器抽风，重试")
		get_course()

def init_getanswer():
	try:
		global session
		session.headers=json_headers
		Data={"as":{"0":{"answer":"","point":0},"1":{"answer":"","point":1},"2":{"answer":"","point":2},"3":{"answer":"","point":3},"4":{"answer":"","point":4},"5":{"answer":"","point":5},"6":{"answer":"","point":6},"7":{"answer":"","point":7},"8":{"answer":"","point":8},"9":{"answer":"","point":9},"10":{"answer":"","question_type_id":3,"point":10},"11":{"answer":"","question_type_id":3,"point":11},"12":{"answer":"","question_type_id":3,"point":12},"13":{"answer":"","question_type_id":3,"point":13},"14":{"answer":"","question_type_id":3,"point":14}},"duration":1491,"eid":"942"}
		Data=json.dumps(Data)
		req=session.post(host+ques,data=Data)
	except:
		print("服务器坏掉了，在重试")
		init_getanswer()

def get_answer(eid):
	try:
		html=get_res(session.get(host+report+eid+".html"))
		html=html.replace(" ","").replace("\n","")
		findalll=re.compile("<span>\[(.*?)\]</span>.*?<pclass=\"question-body-text\">(.*?)</p>.*?<spanclass=\"answer_value\">(.*?)</span>")
		return findalll.findall(html)
	except:
		print("服务器被玩坏了，你要负责哟！")
		get_answer(eid)

def get_title(eid):
	try:
		html=get_res(session.get(host+video+eid+".html"))
		findtitle=re.compile("<div class=\"course-title\" style=\"font-size: 24px;\">(.*?)</div>")
		return findtitle.findall(html)
	except:
		print("服务器死掉了，呜呜呜~>_<")
		get_title(eid)

def update_answer(Data):
	try:
		global session
		session.headers=json_headers
		Data=json.dumps(Data)
		req=session.post(host+ques,data=Data)
		errcode=json.loads(get_res(req))
	except:
		print("服务器在休产假")
		update_answer(Data)

def checkpoint():
    #print("checkpoint!")
	try:
		res=get_res(session.get(host+point))
		errcode=json.loads(res)
		data=errcode['data']
		return data['getScores']
	except:
		print("服务器还在休产假")

if __name__=='__main__':
    print("vclass一键答题")
    course=user_login()
    init_getanswer()
    answerlist=[]
    #开始获取答案同时答题
    for eid in course:
        print(eid)
        b={}
        c={}
        i=0
        answerlist=get_answer(eid)
        if len(answerlist)==0:
            continue
        #print(answerlist)
        for answer in answerlist:
            a={}
            a.update(answer=answer[2])
            if answer[0]=="判断题":
                 a.update(question_type_id=3)
            a.update(point=i)
            b.update({str(i):a})
            i=i+1
            #print(b)
        c.update({'as':b})
        #"duration":1491,"eid":"942"
        c.update(duration=random.randint(100,600))
        c.update({"eid":eid})
        #print(c)
        update_answer(c)
        print(get_title(eid),"得分：",checkpoint())
    print("全部完成！")
    input("按回车退出")