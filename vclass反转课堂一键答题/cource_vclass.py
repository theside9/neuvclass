import requests
import sys
from bs4 import BeautifulSoup


consid="cres"#课程
timestamp="1572352966"
sign="d8154dc1e84673ef5f253ec57c5c73d2"#post数据传回的签名
inlinefileid="1554718284_avfvv.mp4"#视频名称
inlinefiletype=".mp4"#类型
academicyearno="2019"#学年
termno="0"#学期
courseno="52015CC0AV"#课程编号
teachingclassno="300682-002"#课程班级
datid="48055"#
rid="hw1571981801582"#
accessorid="17180600714"#学号


session = requests.session()
res = session.get("https://course.neusoft.edu.cn")
cookie = requests.utils.dict_from_cookiejar(res.cookies)
#res2=session.post("http://hw.neusoft.edu.cn/hw/lrn/fileview.do",)

def main():
    html=session.get("http://hw.neusoft.edu.cn/hw/lrn/lrn.do?cno=52015CC0AV&teachingclassno=300682-002")
    print(html)
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))