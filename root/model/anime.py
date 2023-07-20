import requests
from bs4 import BeautifulSoup
link = "https://otakudesu.lol/"

class Anime:
    def anime(self, id):
        try:
            linkComplete = link+'anime/'+id
            page = requests.get(linkComplete, allow_redirects=False)
            print(page.status_code)
            if page.status_code == 302 or page.status_code == 404:
                code = 404
                desc = 'Not found'
                response = {}
                response['code'] = code
                response['desc'] = desc
                response['data'] = {}
                return response, code
            code = 200
            desc = 'Success'
            detail = {}
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find('div',class_='venser')
            details = element.find('div', class_='fotoanime').find_all('p')
            detail['main_title'] = element.find('div',class_="jdlrx").get_text().strip()
            detail['images'] = element.find('div', class_='fotoanime').find('img').get('src')
            detail['title'] = details[0].get_text().strip().replace("Judul: ","")
            detail['japanese'] = details[1].get_text().strip().replace("Japanese: ","")
            detail['rating'] = details[2].get_text().strip().replace("Skor: ","")
            detail['producer'] = details[3].get_text().strip().replace("Produser: ","")
            detail['type'] = details[4].get_text().strip().replace("Tipe: ","")
            detail['status'] = details[5].get_text().strip().replace("Status: ","")
            detail['total_episode'] = details[6].get_text().strip().replace("Total Episode: ","")
            detail['duration'] = details[7].get_text().strip().replace("Durasi: ","")
            detail['date'] = details[8].get_text().strip().replace("Tanggal Rilis: ","")
            detail['studio'] = details[9].get_text().strip().replace("Studio: ","")
            allGenre = []
            genres = details[10].find_all('a')
            for dataGenre in genres:
                    objGenre = {}
                    objGenre['name'] = dataGenre.get_text()
                    objGenre['id'] = dataGenre.get('href').replace(link+'genres/','').replace('/','')
                    allGenre.append(objGenre)
            detail['genres'] = allGenre
            animeList = element.select('.episodelist')
            batchs = []
            episodes = []
            batchList = animeList[0].find_all('li')
            episodeList = animeList[1].find_all('li')
            if episodeList:
                for episode in episodeList:
                    dataEpisode = {}
                    dataEpisode['id'] = episode.find('a').get('href').replace(link+'episode/','').replace('/','')
                    dataEpisode['title'] = episode.find('a').get_text().strip()
                    dataEpisode['date'] = episode.find('span',class_='zeebr').get_text().strip()
                    episodes.append(dataEpisode)
            if batchList:
                for batch in batchList:
                    dataBatch = {}
                    dataBatch['id'] = batch.find('a').get('href').replace(link+'batch/','').replace('/','')
                    dataBatch['title'] = batch.find('a').get_text().strip()
                    dataBatch['date'] = batch.find('span',class_='zeebr').get_text().strip()
                    batchs.append(dataBatch)
            detail['episodes'] = episodes
            detail['batch'] = batchs
            response = {}
            response['code'] = code
            response['desc'] = desc
            response['data'] = detail
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": []
            }
            return response, 500