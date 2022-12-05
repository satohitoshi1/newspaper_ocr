import os
from pathlib import Path
from pdf2image import convert_from_path

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)
poppler_paths = r"C:\Users\user\PYTHON\newspaper_ocr\poppler\bin"

# PDFファイルのパス
pdf_path = "C:/Users/user/PYTHON/newspaper_ocr/kj/"

# PDFファイル名のリスト取得
pdf_lists = os.listdir(pdf_path)
# print(pdf_list) ・・・ ['20221115102133.pdf', 'kj.pdf']

for pdf in pdf_lists:
    # PDF -> Image に変換（600dpi）convert_from_path()
    pages = convert_from_path(pdf, poppler_paths)

    # 保存するフォルダ
    kj_dir = Path("./kj_png")
    # for i in range(len(pdf_path)):
    #    pages[i].save('kj_'+str(i)+'.png')
    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        # pngの名前
        file_name = str(pdf_lists) + "_{:02d}".format(i + 1) + ".png"
        # 保存するdirとファイル名
        kj_path = kj_dir / file_name
        # PNGで保存
        pages.save(str(kj_path), "PNG")
        print(pdf)
