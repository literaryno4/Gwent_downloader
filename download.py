import os
import sys
import requests
import bs4
import wget
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--os', type=str, default='unix_like', choices=['unix_like', 'windows'])

args = parser.parse_args()

filename_root = 'https://gwent.one/cn/beta/card/'
file_root = 'https://gwent.one/video/card/loop/ob/'

for file_num in range(151269, 300000):
    try:
        print(file_num)
        filename_url = filename_root + str(file_num)
        file_url = file_root + str(file_num) + '.mp4'
        r = requests.get(filename_url)
        if r.status_code != 200:
            continue
        html = bs4.BeautifulSoup(r.text)
        filename = html.title.text.replace(' [梦境试炼]', '') + '.mp4'
        if filename == '.mp4':
            continue
        print(filename)
        if args.os == 'unix_like':
            os.system('wget ' + file_url + ' -O ' + filename)
        else:
            wget.download(file_url, filename)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        continue
