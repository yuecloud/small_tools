#coding:utf-8
from tkinter import *
import tkinter.font as tkFont
import  requests
import tkMessageBox
import  time
from tkinter import  ttk

def  getserver_time(url,btname):
    btname.delete('1.0', 'end')
    var=requests.get("http://%s/update_time/update?f=get"%(url)).content
    # print var
    btname.insert('insert',var)

def  get_text(servernum,url,textname):
    ft = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    text1 = textname.get("0.0", "end")
    boolflag = tkMessageBox.askyesno(title='修改头条测试服务器【%s】时间'%(servernum), message='确定修改?')
    if  boolflag:
        requests.get("http://%s/update_time/update?f=update&datetime=%s"%(url,text1))
        time.sleep(0.5)

        tkMessageBox.showinfo('提示', "修改头条服务器时间成功，当前头条测试服务器"
                                    "【{0}】时间为{1}".format(servernum,requests.get("http://%s/update_time/update?f=get"%(url)).content))

def  modify_bjtime(servernum,url):
    boolflag = tkMessageBox.askyesno(title='修改头条测试服务器【%s】时间' % (servernum), message='确定修改?')
    if boolflag:
        # requests.get("http://%s/update_time/update?f=update&datetime=%s"
        #          %(url, requests.get("http://quan.suning.com/getSysTime.do").json().get("sysTime2")))
        # requests.get("http://%s/update_time/update?f=update&datetime=%s"
        #          %(url, requests.get("http://cgi.im.qq.com/cgi-bin/cgi_svrtime").content().strip()))

        index_value=numberChosen.current()

        print (index_value)
        # str1=number.get().strip()
        # print (str1)

        if index_value==0:
        # if str1==u"阿里":
            requests.get("http://%s/update_time/update?f=update&datetime=%s"
                 %(url, time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(requests.get("http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp").
            json().get("data").get("t")[0:-3])))))
        elif index_value==1:
            requests.get("http://%s/update_time/update?f=update&datetime=%s"
                 %(url, requests.get("http://quan.suning.com/getSysTime.do").json().get("sysTime2")))
        elif index_value==2:
            requests.get("http://%s/update_time/update?f=update&datetime=%s"
                     %(url, requests.get("http://cgi.im.qq.com/cgi-bin/cgi_svrtime").content().strip()))

        time.sleep(0.5)
        tkMessageBox.showinfo('提示', "修改头条服务器时间成功，当前头条测试服务器"
                                    "【{0}】时间为{1}".format(servernum,requests.get("http://%s/update_time/update?f=get"%(url)).content))

if __name__=="__main__":

    try:
        code=requests.get("http://www.baidu.com").status_code

    except Exception as e:
        tkMessageBox.showerror('提示',"当前PC运行环境网络异常，请确认网络")
    else:
        if  code==200:
            tk=Tk()
            tk.title(u'获取【头条测试服务器】当前时间')
            tk.geometry('800x400')

            ft = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
            #标签控件，显示文本和位图，展示在第一行

            #按钮控件
            serverurl1="test-mission-data.dftoutiao.com"
            serverurl2="test-wechat-program.dftoutiao.com"

            ft = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
            ftbt=tkFont.Font(family='Fixdsys', size=11, weight=tkFont.BOLD)



            Label(tk,text="【头条测试服1】当前时间(mission-data)：",height=1,width=50,font=ftbt).grid(row=3,column=0,sticky=W)#靠右
            #输入控件
            t1=Text(tk,height=1,width=30,font=ft,fg="blue")
            Label(tk).grid(row=2, sticky=E)
            t1.grid(row=3,column=1,padx=10,pady=10)
            button1=Button(tk,text="查询时间",command=lambda :getserver_time(serverurl1,t1),font=ftbt,fg='blue')
            button1.grid(row=4,column=0)
            button2=Button(tk,text="修改时间" ,font=ftbt,fg='red',command=lambda : get_text(1,serverurl1,t1))
            button2.grid(row=4,column=1)

            button3=Button(tk,text="修改为北京时间" ,font=ftbt,fg='brown',command=lambda : modify_bjtime(1,serverurl1))
            Label(tk).grid(row=5, sticky=E)

            button3.grid(row=6, column=0)

            Label(tk).grid(row=12, sticky=E)
            Label(tk).grid(row=13, sticky=E)
            Label(tk).grid(row=14,sticky=E)



            Label(tk,text="【头条测试服2】当前时间(wechat-program)：",height=1,width=50,font=ftbt).grid(row=18,sticky=E)#靠右
            t2=Text(tk,height=1,width=30,font=ft,fg="blue")
            t2.grid(row=18,column=1,padx=10,pady=10)
            button1=Button(tk,text="查询时间",command=lambda :getserver_time(serverurl2,t2),font=ftbt,fg='blue')
            button1.grid(row=19,column=0)

            button2=Button(tk,text="修改时间",font=ftbt,fg='red',command=lambda : get_text(2,serverurl2,t2))
            button2.grid(row=19,column=1)

            button3=Button(tk,text="修改为北京时间" ,font=ftbt,fg='brown',command=lambda : modify_bjtime(2,serverurl2))
            Label(tk).grid(row=20, sticky=E)
            button3.grid(row=21, column=0)

            Label(tk, text="【请选择北京时间校验服务器：】", height=1, width=50, font=ftbt).grid(row=0, column=0, sticky=W)

            number = StringVar()
            numberChosen = ttk.Combobox(tk, width=20, textvariable=number,font=ftbt)
            numberChosen['values'] = ("阿里", "苏宁", "腾讯")  # 设置下拉列表的值
            numberChosen.grid(column=1, row=0)  # 设置其在界面中出现的位置 column代表列 row 代表行
            numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
            #主事件循环
            mainloop()
