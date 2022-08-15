import requests
import json
import tkinter.ttk
from tkinter import *
from setuptools import Command



def rearea(area):
    if area == "安卓QQ":
        return "qq"

    if area == "安卓微信":
        return "wx"

    if area == "苹果QQ":
        return "ios_qq"

    if area == "苹果微信":
        return "ios_wx"

def ft(obj):
    dic = {}
    dic["name"] = obj["data"]["name"]
    dic["area"] = obj["data"]["area"]
    dic["areaPower"] = obj["data"]["areaPower"]
    dic["city"] = obj["data"]["city"]
    dic["cityPower"] = obj["data"]["cityPower"]
    dic["province"] = obj["data"]["province"]
    dic["provincePower"] = obj["data"]["provincePower"]
    dic["guobiao"] = obj["data"]["guobiao"]
    dic['updatetime'] = obj["data"]['updatetime']
    return dic

def find(hero,area,master):
    url = "https://www.jk.cxkf.cc/api_select.php"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    data = {
        "hero": f"{hero}",
        "type": f"{rearea(area)}"           # "qq、wx、ios_qq、ios_wx"
    }

    response = requests.get(url=url, params=data, headers=headers)
    response.encoding='utf-8'
    print("===============")
    c=response.text
    print(c)
    print("ssss")
    obj = json.loads(response.text)
    print(obj)
    dic = ft(obj)

    t = Text(master)
    for a in dic.items():
        t.insert(END, a)
        t.insert(END, "\n\n")
    t.place(relx=0.5-0.25,rely=0.3, relheight=0.4, relwidth=0.5)    



def main():
    #声明窗体
    root=tkinter.Tk()
    #编辑窗体提示文字
    root.title("王者荣耀最低战力查询")
    #设置窗体大小·注意，不是乘号*而是小写的x
    #如果想设置显示位置的写法是：root.geometry("800x600+100+50") 
    root.geometry("800x600+100+50")

    # 标签
    l1 = tkinter.Label(text="英雄名字", master=root)
    l2 = tkinter.Label(text="大区", master=root)
    # l3 =  
    input1 = tkinter.Entry(master=root, bd=1)
    input1.place(relx=0.4,rely=0.1)
    l1.place(relx=0.3,rely=0.1)

    # 大区
    var = StringVar()
    list_area = ["安卓QQ","安卓微信","苹果QQ","苹果微信"]
    com = tkinter.ttk.Combobox(root, textvariable=var, values=list_area)
    com.place(relx=0.4,rely=0.2)
    l2.place(relx=0.3,rely=0.2)

    # 按钮
    button = tkinter.Button(
        text="查询",
        command=lambda: find(hero=input1.get(), area=com.get(),master=root)
    )
    button.place(relx=0.4,rely=0.75,relheight=0.1,relwidth=0.2)




    
    #展示窗体
    root.mainloop()


if __name__ == '__main__':
    main()