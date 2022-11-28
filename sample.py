from cgitb import text
from curses.textpad import Textbox
from datetime import datetime, date
from email.mime import image
from logging import root
from dateutil.relativedelta import relativedelta
import calendar
import jpholiday
import tkinter as tk
from numpy import imag

WEEKDAY_COLOR = (None, "red", *(["black"] * 5), "blue")
A_MONTH = relativedelta(months=1)
image_weather = []


def button_click(): #日付がクリックされた時にこの関数をcommandで指定して日記用のウィンドウを開きたい
    
    window = tk.Tk()
    window.title("diary")
    window.geometry("500x500")

    image_weather.append(tk.PhotoImage(file="/Users/koyo/Desktop/koyo/py_program/太陽.png"))
    image_weather.append(tk.PhotoImage(file="/Users/koyo/Desktop/koyo/py_program/雨.png"))
    image_weather.append(tk.PhotoImage(file="/Users/koyo/Desktop/koyo/py_program/雲.png"))
    image_weather.append(tk.PhotoImage(file="/Users/koyo/Desktop/koyo/py_program/雪.png"))
    
    label_for_wather = tk.Label(window, text="天気")
    label_for_wather.pack()
    
    frame_for_weather = tk.Label(window) #天気のボタンを配置するためのframe
    frame_for_weather.pack()
    button_sunny = tk.Button(frame_for_weather, text="雨", image=image_weather[0])
    button_rainy = tk.Button(frame_for_weather, text="雨", image=image_weather[1])
    button_cloudy = tk.Button(frame_for_weather, text="曇り", image=image_weather[2])
    button_snowy = tk.Button(frame_for_weather, text="雪", image=image_weather[3])
    button_sunny.pack(side=tk.LEFT)
    button_rainy.pack(side=tk.LEFT)
    button_cloudy.pack(side=tk.LEFT)
    button_snowy.pack(side=tk.LEFT)

    textbox_for_diary = tk.Text(window, font=("",20), height=500, width=500, bg="skyblue") #日記入力用のテキストボックスを作成
    textbox_for_diary.pack()

    window.mainloop()

class TkCalendar(tk.Frame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.pack()
        today = datetime.today()
        self.date = date(today.year, today.month, 1)
        self.calendar = calendar.Calendar()
        self.calendar.setfirstweekday(6)

    def build(self):
        self.build_date()
        self.build_weekdays()
        self.build_days()

    def build_date(self, font=("", 20)):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        # 先月ボタン
        prev = tk.Button(frame, text="<", font=font, command=self.prev_month)
        prev.pack(side=tk.LEFT)
        # 年月表示
        self.year = tk.Label(frame, text=self.date.year, font=font)
        self.year.pack(side=tk.LEFT)
        slash = tk.Label(frame, text="/", font=font)
        slash.pack(side="left")
        self.month = tk.Label(frame, text=self.date.month, font=font)
        self.month.pack(side=tk.LEFT)
        # 翌月ボタン
        next = tk.Button(frame, text=">", font=font, command=self.next_month)
        next.pack(side=tk.LEFT)

    def build_weekdays(self):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        for column, weekday in enumerate("日月火水木金土", 1):
            widget = tk.Button(frame, text=weekday, fg=WEEKDAY_COLOR[column],
                                height=2, width=4, relief="flat")
            widget.grid(column=column, row=1, padx=10, pady=5)

    def build_days(self):
        self.days = tk.Frame(self)
        self.days.pack()
        self.update_days()

    def update_days(self):
        for day in self.days.winfo_children():
            day.destroy()
        year, month = self.date.year, self.date.month
        weeks = self.calendar.monthdayscalendar(year, month)
        for row, week in enumerate(weeks, 1):
            for column, day in enumerate(week, 1):
                if day == 0:
                    continue
                color = WEEKDAY_COLOR[column]
                if jpholiday.is_holiday(date(year, month, day)):
                    color = "red"
                widget = tk.Button(self.days, text=day, fg=color,
                                   height=2, width=4, relief="flat",command=button_click) #このボタンが日付を表示している。commandを指定して日にちがクリックされた時に新たなウィンドウを開く
                widget.grid(column=column, row=row, padx=10, pady=5)

    def update(self):
        self.year["text"] = self.date.year
        self.month["text"] = self.date.month
        self.update_days()

    def prev_month(self):
        self.date -= A_MONTH
        self.update()

    def next_month(self):
        self.date += A_MONTH
        self.update()


def main():
    root = tk.Tk()
    root.title("calendar")
    root.geometry("600x440")
    tkcalendar = TkCalendar(root)
    tkcalendar.build()
    root.mainloop()

if __name__ == "__main__":
    main()