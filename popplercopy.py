import os
from pathlib import Path
from pdf2image import convert_from_path

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

# PDFファイルのパス
pdf_path = "C:/Users/user/PYTHON/newspaper_ocr/kj/"

# PDFファイル名のリスト取得
pdf_list = os.listdir(pdf_path)
# print(pdf_list) ・・・ ['20221115102133.pdf', 'kj.pdf']

for ls in pdf_list(): # これリスト呼び出せないと言われるのなぜ
    # PDF -> Image に変換（600dpi）
    pages = convert_from_path(ls, 600)
    # 画像ファイルを１ページずつ保存
    image_dir = Path("./kj_png")
    for i, page in enumerate(pages):
        file_name = str(pdf_list) + "_{:02d}".format(i + 1) + ".png"
        image_path = image_dir / file_name
        # PNGで保存
        page.save(str(image_path), "PNG")
