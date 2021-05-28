from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import os

def main() :
    print('収集したい画像の名称(名前)を入力してください>>>')
    _keyword = input() 
    print("収集したいページ数を入力してください(20枚/ページ)>>>")
    _max_page = input()
    search_download(_keyword, _max_page)

def search_download(_keyword, _max_page) :
    keyword = _keyword
    max_page = _max_page
    print (keyword, max_page)

    path = './Export/' + keyword
    os.mkdir(path)
    print("")

    dst_path = path + '/'
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
    }
    print('Starting')
    
    cnt = 1
    for i in range(int(max_page)):
        cnt += 20
        url = 'https://search.yahoo.co.jp/image/search?p={}&ei=UTF-8&b={}'.format(urllib.parse.quote(keyword), cnt)
    
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        soup = BeautifulSoup(res)
    
        div = soup.find('div', id='contents')
        imgs = div.find_all('img')
    
        for j in range(len(imgs)):
            
            print('-> Downloading image')
            img = imgs[j]['src']
            tmp = urllib.request.urlopen(img)
            data = tmp.read()
    
            file_name = dst_path + 'page' + str(i+1) + '_img' + str(j+1) + '.jpg'
    
            with open(file_name, 'wb') as save_img:
                save_img.write(data)

    print('└─  Complete')

if __name__ == "__main__" :
    main()