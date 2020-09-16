import  requests,time
from bs4 import BeautifulSoup
from selenium import webdriver


"""
下载网易云音乐
"""



def search_163music(word):#获取网易云搜索列表结果
    search_url = "https://music.163.com/#/search/m/?s={word}".format(word=word)
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    dr=webdriver.Chrome(options=option)
    # dr=webdriver.Chrome()
    dr.get(search_url)
    time.sleep(2)
    dr.switch_to.frame("g_iframe")
    searchResultPk=dr.find_element_by_class_name("srchsongst").find_elements_by_xpath("./div")
    result_pack=[]
    for result in searchResultPk:
        songNameInfo=(songInfo:=result.find_elements_by_tag_name("a"))[1]#每个div下面有五个a标签，第2,4,5分别为歌曲名，作者名，专辑名
        songName,songNameUrl=songNameInfo.text,songNameInfo.get_attribute("href")
        songArtistInfo=songInfo[3]
        songArtistName,songArtistUrl=songArtistInfo.text,songArtistInfo.get_attribute("href")
        songAlbumInfo=songInfo[4]
        songAlbumName, songAlbumUrl = songAlbumInfo.text, songAlbumInfo.get_attribute("href")
        # print(songName,songNameUrl)
        # print(songArtistName,songArtistUrl)
        # print(songAlbumName, songAlbumUrl)
        # print("====================================")
        songId=songNameUrl.split("id=")[-1]#分割url字符串，获取songID
        result_pack.append((songName,songId))
    return result_pack

def songDownload(songName,songId):#下载音乐
    songDownLink="http://music.163.com/song/media/outer/url?id={muId}".format(muId=songId)
    header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


    res=requests.get(songDownLink,headers=header).content
    with open("./"+songName.replace(" ","_")+".mp3","wb") as f:
        f.write(res)
        print(songName,"下载完成")

def main1(song):
    for i in search_163music(song):
        songName,songId=i
        songDownload(songName, songId)

main1("wonderful U")
















# music_dowm_url="http://music.163.com/song/media/outer/url?id={muId}".format(muId=muId)