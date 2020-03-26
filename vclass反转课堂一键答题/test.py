json_data={"as":{"0":{"answer":"A","point":0},"1":{"answer":"A","point":1}}}

print(json_data)


b={}
c={}
#利用for对a字典添加答案和题号point，然后将题号与a作为键值对组合成b，反复循环最后添加给c
#a是答案的字典，b是{题号:答案}的字典，c是整体打包成{as:试卷答案}这个整体的字典
#之后用json格式化就行。
#如果是单选题，需要额外加类型3
a={}
a.update({"answer":"A","point":0})
b.update({"0":a})

a={}
a.update({"answer":"A","point":1})
b.update({"1":a})


c.update({'as':b})

print(c)
