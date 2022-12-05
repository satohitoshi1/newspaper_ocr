import sys
from PIL import Image
import pyocr
import pyocr.builders
import cv2

# import MeCab


def Tes():
    kj = cv2.imread("kj_png/kj_01.png")
    kj_gray = cv2.cvtColor(kj, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("kj_png/kj_gray.png", kj_gray)
    # print(kj_gray)
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいるread
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))


    txt = tool.image_to_string(
        Image.open("kj_png/kj_gray.png"),  # OCRする画像
        lang="jpn+jpn_vert",  # 学習済み言語データ
        builder=pyocr.builders.TextBuilder(tesseract_layout=4),  # 期待される出力のタイプを指定
    )
    # print(txt)
    return txt

# with open("text.txt", mode="w") as f:
#     f.writelines(txt)


if __name__ == "__main__":
    Tes()
