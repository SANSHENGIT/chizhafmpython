from urllib import request

from bs4 import BeautifulSoup

from cz.api.category import Category

# url = 'http://www.kuwo.cn/www/category/index/'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
# cookie = cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler,request.HTTPHandler(debuglevel=1))
# request.install_opener(opener)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}

#获取类别（Python对象）
def fetch_categories():
    url = 'http://www.kuwo.cn/www/category/index/'
    req = request.Request(url, data=None, headers=headers)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html,'html5lib')

    cates = []
    for bang in soup.find_all('div',{'class':'bang'}):
        #print('大类',bang.h2['data-catid'],bang.h2.get_text())
        cate = Category(bang.h2['data-catid'],bang.h2.get_text())
        children_cates = []
        for a in bang.find('li').find_all('a'):
            #print(a.attrs['data-catid'],a.get_text())
            child = Category(a.attrs['data-catid'], a.get_text())
            children_cates.append(child)
        cate.children = children_cates
        cates.append(cate)

    return cates

#获取类别（json对象）
def fetch_json_categories():
    url = 'http://www.kuwo.cn/www/category/index/'
    req = request.Request(url, data=None, headers=headers)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html,'html5lib',from_encoding='uft-8')

    cates = list()
    for bang in soup.find_all('div',{'class':'bang'}):
        big_cate = dict()
        big_cate['id'] = bang.h2['data-catid']
        big_cate['name'] = bang.h2.get_text()
        children_cates = list()
        for a in bang.find('li').find_all('a'):
            child_cate = dict()
            child_cate['id'] = a.attrs['data-catid']
            child_cate['name'] = a.get_text()
            children_cates.append(child_cate)
        big_cate['children'] = children_cates
        cates.append(big_cate)
    return cates
    #return json.dumps(cates,ensure_ascii=False)


# cats = fetch_json_categories()
# print(cats)

#获取歌词
def fetch_music_lyric(mid):
    url = 'http://www.kuwo.cn/yinyue/{}'.format(mid)
    req = request.Request(url, data=None, headers=headers)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html5lib', from_encoding='uft-8')
    lyric = list()
    for p in soup.find_all('p',{'class':'lrcItem'}):
        lyric.append(p.get_text())
    return lyric

#获取歌曲详细信息（名称，链接，歌手，音乐id）
def fetch_music_detail(catId=88096, pageno=0, pagesize=50):
    url = 'http://www.kuwo.cn/www/category/content/music?catId={0}&pn={1}&rn={2}'.format(catId, pageno, pagesize)
    req = request.Request(url, data=None, headers=headers)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html5lib', from_encoding='uft-8')
    musics = []
    for li in soup.find_all('li'):
        name = li.find('div',{'class':'name'}).find('a').get_text()
        href = li.find('div',{'class':'name'}).find('a').attrs['href']
        artist = li.find('div',{'class':'artist'}).find('a').get_text()
        music_id = href.replace('http://www.kuwo.cn/yinyue/','')
        #lyric = fetch_music_lyric(href)
        path = 'http://antiserver.kuwo.cn/anti.s?rid=MUSIC%5F{0}&format={1}&response=url&type=convert%5Furl'.format(music_id,'mp3')
        music = {}
        music['name'] = name
        music['href'] = href
        music['artist'] = artist
        music['id']= music_id
        #music['lyric'] = lyric
        music['path'] = path
        musics.append(music)
    return musics
    #return json.dumps(musics,ensure_ascii=False)

# res = fetch_music_detail()
# print(res)

# res = fetch_music_lyric('507539')
# print(res)


