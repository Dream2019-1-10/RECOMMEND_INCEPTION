import requests
import pandas as pd
import numpy as np


def get_image(url, headers, image_name):
    """ 爬取图片
    :param url: 图片网址
    :param headers: 请求头
    :param image_name: 保存的图片名称
    """
    # 带请求头的爬虫
    html = requests.get(url, headers)
    print(html)

    # 保存图片到本地
    with open(image_name, "wb") as f:
        f.write(html.content)


def test_get_image():
    # 读取url
    sheets = ['上衣','下衣']
    pic_path = 'D:/work/歌莉娅项目/img'
    # 图片网址
    i = 0
    for sheet in sheets:
        data = pd.read_excel(pic_path + '/imgs.xlsx', sheet_name=sheet)
        for cn,url in zip(data['cate_name'],data['pic_url']):
            # 请求头
            headers = {
                "Host": "img0.bdstatic.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
            }

            # 保存图片名称
            import os
            from os.path import exists
            output_dir = '../dataset/train/'+sheet
            if not exists(output_dir):
                os.mkdir(output_dir)
            path_format = os.path.join(output_dir, "{}_{:02d}.jpg")
            # image_name = output_dir + "0001.jpg"
            print('cn:',cn)
            try:
                image_name = path_format.format(cn,i)
                # print(image_name)
                # 爬取图片
                get_image(url, headers, image_name)
            except:
                image_name = path_format.format(cn.split('/')[0], i)
                # print('--1--')
                # 爬取图片
                get_image(url, headers, image_name)
            i += 1



# 作为运行脚本，才执行此函数
if __name__ == "__main__":
    test_get_image()