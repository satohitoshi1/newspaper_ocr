import argparse

import cv2
import layoutparser as lp #layoutparserが入らないwindowsのせい？


def main():
    args = parse_args()

    image = cv2.imread(args.src)

    detectron2_model = lp.Detectron2LayoutModel(
        'lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config',
        extra_config=['MODEL.ROI_HEADS.SCORE_THRESH_TEST', 0.5],
        label_map={0: 'Text', 1: 'Title', 2: 'List', 3:'Table', 4:'Figure'}
    )
    detectron2_layout = detectron2_model.detect(image)

    ocr_agent = lp.GCVAgent.with_credential(args.gcp_credential_json, languages=['ja'])
    res = ocr_agent.detect(image, return_response=True)
    ocr_layout = ocr_agent.gather_full_text_annotation(res, agg_level=lp.GCVFeatureType.BLOCK)

    print('### レイアウト解析あり(図表エリアごとにテキスト抽出)')
    for l in detectron2_layout:
        if l.type in ['Table', 'Figure']:
            texts = ocr_layout.filter_by(l.block, center=True).get_texts()
            print('\n'.join(texts).replace(' ', ''))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gcp_credential_json', type=str)
    parser.add_argument('--src', type=str)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
