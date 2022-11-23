# PDFをpngに poppler使う
# OCR(光学文字認識) Tesseract PDFをpngに変換、日本語学習済みtessdata_best 、tesseract_layout=4 が暫定トップ
# 文脈の理解 形態素解析 MeCab
# わかち書き MeCab、TinySegmenter
# scrap.pyのイメージでスクリーンショットで切り抜き
# アプリ化 kivy

import pyautogui as pag
import pyocr
import subprocess
import os
import time

acr_path = "C:/Program Files/Adobe/Acrobat DC/Acrobat/Acrobat.exe"

# PDF指定
pdf_path = "C:/Users/user/PYTHON/newspaper_ocr/kj/"


pdf_list = os.listdir(pdf_path)
i = 1


def run_ocr(tool, name_img):  # OCRを動かして、テキストデータに変換（スペース削除）
    result = tool.image_to_string(name_img, lang="jpn")
    result = result.replace(" ", "")
    print(result)
    return result


if __name__ == "__main__":

    # OCR呼び出し
    tools = pyocr.get_available_tools()
    tool = tools[0]

    # フォルダ内にあるPDFファイルをループ
    for idx, file in enumerate(pdf_list):

        # PDFファイルを開く
        pdf_pro = subprocess.Popen([acr_path, pdf_path + file], shell=False)
        time.sleep(3)

        # 座標指定箇所を切り取りして画像保存
        name_img = pag.screenshot(
            str(i) + "temp.png", region=(500, 200, 500, 500)
        )  # x,y座標,x長さ、y長さ
        # ここを座標ではなく記事ごと切り取りに書き換える

        # 指定座標を文字起こししてテキスト変換
        result = run_ocr(tool, name_img)

        i = i + 1
        pdf_pro.kill()
        time.sleep(1)
