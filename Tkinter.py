# Tkinterのライブラリを取り込む
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
from Tes import Tes
from poppler import poppler

image_weather = []


# ファイルの参照処理
def click_refer_button():
    fTyp = [("", "*")]
    iDir = os.path.abspath(os.path.dirname(__file__))  # ファイル名を取得してパスに書き換える
    filepath = filedialog.askopenfilename(filetypes = fTyp, initialdir = iDir)  # ファイルを開くダイアログボックス
    file_path.set(filepath)


# 出力処理
def click_export_button():
    path = file_path.get()
    if path[-4:] == '.png':
        PNG = Tes()
        text_data = PNG
        textBox.insert(END, text_data)
    elif path[-4:] == '.pdf':
        PDF = poppler()
        PDF_PNG = Tes()
        textBox.insert(END, PDF_PNG)
    else:
        # 画面作成
        version = tkinter.Tcl().eval('info patchlevel')
        window = tkinter.Tk()
        window.geometry("1200x2500")
        window.title("画像表示：" + version)

        # キャンバス作成
        canvas = tkinter.Canvas(window, bg="#deb887", height=800, width=2000)
        # キャンバス表示
        canvas.place(x=0, y=0)

        # イメージ作成
        image_weather.append(tkinter.PhotoImage(file=r"C:\Users\user\PYTHON\newspaper_ocr\ruwater.png", master=window))
        # キャンバスにイメージを表示
        canvas.create_image(0, 0, image=image_weather, anchor=tkinter.NW)
        textBox.insert(END, '\n読み込みができない種類のファイルです')
        # input("Press enter to start operations...")
        textBox.delete(1.0, tkinter.END)


if __name__ == '__main__':
    # ウィンドウを作成
    root = tkinter.Tk()
    root.title("newspaper_ocr")  # アプリの名前
    root.geometry("500x500")  # アプリの画面サイズ

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル名：')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルのパスを表示するテキストボックスの作成
    file_path = StringVar()
    filepath_entry = ttk.Entry(frame1, textvariable=file_path, width=50)
    filepath_entry.grid(row=0, column=1)

    # 参照ボタンの作成
    refer_button = ttk.Button(frame1, text=u'参照', command=click_refer_button)
    refer_button.grid(row=0, column=2)

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid()

    # テキスト出力ボタンの作成
    export_button = ttk.Button(frame2, text='出力(PDFかPNGしか使えませんよ)', command=click_export_button, width=40)
    export_button.grid(row=0, column=0)

    # テキスト出力ボックスの作成
    textboxname = StringVar()
    textboxname.set('\n\n出力内容 ')
    label3 = ttk.Label(frame2, textvariable=textboxname)
    label3.grid(row=1, column=0)
    textBox = Text(frame2, width=50)
    textBox.grid(row=2, column=0)

    # ウィンドウを動かす
    root.mainloop()
