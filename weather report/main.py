import requests
from bs4 import BeautifulSoup
import tkinter as tk

def url_decided(province,city):
    if province.strip() == "":
        url=f"https://www.msn.cn/zh-cn/weather/forecast/in-{city}?"
    else:
        url=f"https://www.msn.cn/zh-cn/weather/forecast/in-{province},{city}?"
    return url
def Webresponse(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"}
    response=requests.get(url,headers=headers)
    if(response.status_code==200):
        return response
    else:
        raise Exception("请检查输入是否正确，或是否联网")
def command_url():
    response=None
    try:
        province=e1.get()
        city=e2.get()
        url=url_decided(province,city)
        response=Webresponse(url)
    except Exception as e:
        print("请检查输入是否正确以及网络是否连接")
    
    if response:
        weather=CurrentWeather(response)
        summary=weather.get_summary()
        weather_summary.set(summary)

class CurrentWeather():
    def __init__(self,response):
        self.soup=BeautifulSoup(response.text,"html.parser")
    def get_summary(self):
        summary_div = self.soup.find("div", id="CurrentWeatherSummary")
        if not summary_div:
            return "未找到天气摘要容器（可能页面结构变化）"
        return summary_div.string

window=tk.Tk()
window.title('天气预报')
window.geometry('500x400')
l1=tk.Label(window,text='示例:辽宁省，沈阳市 请输入省份(如果是直辖市则不填)',width=45,height=6)
l1.pack(pady=5)
e1=tk.Entry(window,show=None)
e1.pack(pady=5)
l2=tk.Label(window,text='请输入城市',width=25,height=6)
l2.pack(pady=5)
e2=tk.Entry(window,show=None)
e2.pack(pady=5)
b=tk.Button(window,text='确认',command=command_url)
b.pack(pady=10)
weather_summary=tk.StringVar()
weather_summary = tk.StringVar()
l3 = tk.Label(
    textvariable=weather_summary, 
    font=("微软雅黑", 11),
    bg="white",
    fg="#333333",
    wraplength=500,
    justify="left",
    height=8,
    anchor="nw"
)
l3.pack(pady=10)
window.mainloop()
