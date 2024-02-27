import requests
from bs4 import BeautifulSoup
link = "https://otakudesu.cloud/"

class Anime:
    def anime(self, id):
        try:
            linkComplete = link+"anime/"+id
            page = requests.get(linkComplete, allow_redirects=False)
            if page.status_code == 302 or page.status_code == 404:
                code = 404
                desc = "Not found"
                response = {}
                response["code"] = code
                response["desc"] = desc
                response["data"] = {}
                return response, code
            code = 200
            desc = "Success"
            detail = {}
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div",class_="venser")
            details = element.find("div", class_="fotoanime").find_all("p")
            detail["main_title"] = element.find("div",class_="jdlrx").get_text().strip()
            detail["images"] = element.find("div", class_="fotoanime").find("img").get("src")
            detail["title"] = details[0].get_text().strip().replace("Judul: ","")
            detail["japanese"] = details[1].get_text().strip().replace("Japanese: ","")
            detail["rating"] = details[2].get_text().strip().replace("Skor: ","").replace("Skor:","")
            detail["producer"] = details[3].get_text().strip().replace("Produser: ","")
            detail["type"] = details[4].get_text().strip().replace("Tipe: ","")
            detail["status"] = details[5].get_text().strip().replace("Status: ","")
            detail["total_episode"] = details[6].get_text().strip().replace("Total Episode: ","")
            detail["duration"] = details[7].get_text().strip().replace("Durasi: ","")
            detail["date"] = details[8].get_text().strip().replace("Tanggal Rilis: ","")
            detail["studio"] = details[9].get_text().strip().replace("Studio: ","")
            allGenre = []
            genres = details[10].find_all("a")
            for dataGenre in genres:
                    objGenre = {}
                    objGenre["name"] = dataGenre.get_text()
                    objGenre["id"] = dataGenre.get("href").replace(link+"genres/","").replace("/","")
                    allGenre.append(objGenre)
            detail["genres"] = allGenre
            detail["synopsis"] = element.find("div", class_="sinopc").get_text().strip()
            animeList = element.select(".episodelist")
            batchs = []
            episodes = []
            batchList = animeList[0].find_all("li")
            episodeList = animeList[1].find_all("li")
            if episodeList:
                for episode in episodeList:
                    dataEpisode = {}
                    dataEpisode["id"] = episode.find("a").get("href").replace(link+"episode/","").replace("/","")
                    dataEpisode["title"] = episode.find("a").get_text().strip()
                    dataEpisode["date"] = episode.find("span",class_="zeebr").get_text().strip()
                    episodes.append(dataEpisode)
            if batchList:
                for batch in batchList:
                    dataBatch = {}
                    dataBatch["id"] = batch.find("a").get("href").replace(link+"batch/","").replace("/","")
                    dataBatch["title"] = batch.find("a").get_text().strip()
                    dataBatch["date"] = batch.find("span",class_="zeebr").get_text().strip()
                    batchs.append(dataBatch)
            detail["episodes"] = episodes
            detail["batch"] = batchs
            response = {}
            response["code"] = code
            response["desc"] = desc
            response["data"] = detail
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {}
            }
            return response, 500
    
    def episode(self, id, stream, bcrypt):
        try:
            linkComplete = link+"episode/"+id
            page = requests.get(linkComplete, allow_redirects=False)
            if page.status_code == 302 or page.status_code == 404:
                code = 404
                desc = "Not found"
                response = {}
                response["code"] = code
                response["desc"] = desc
                response["data"] = {}
                return response, code
            code = 200
            desc = "Success"
            detail = {}
            response = {}
            soup = BeautifulSoup(page.content, "lxml")
            prev = soup.find("a", string="Previous Eps.")
            next = soup.find("a", string="Next Eps.")
            detail["title"] = soup.select_one(".posttl").get_text().strip()
            detail["stream"] = soup.find(id="pembed").find("iframe").get("src") if stream else bcrypt.check_password_hash('$2b$12$cEAx4bsYybzb/6na.4TB8ucFh2ON1bhzwqVCHvEBxX7LIsTP03bn.', stream) if stream is not None else None
            detail["all_episode"] = soup.find("a",string="See All Episodes").get("href").replace(link+"anime/","").replace("/","")
            detail["prev_episode"] = prev.get("href").replace(link+"episode/","").replace("/","") if prev is not None else None
            detail["next_episode"] = next.get("href").replace(link+"episode/","").replace("/","") if next is not None else None
            downloads = []
            elementDownloads = soup.find("div",class_="download").select("ul")
            for index, data in enumerate(elementDownloads):
                allDownload = []
                listResolusion = data.find_all("li")
                for list in listResolusion:
                    detailDownload = {}
                    listDownload = []
                    elementDetail = list.find_all("a")
                    for child in elementDetail:
                        obj = {}
                        obj["link"] = child.get("href")
                        obj["name"] = child.get_text().strip()
                        listDownload.append(obj)
                    detailDownload["resolution"] = list.find("strong").get_text().strip()
                    detailDownload["links"] = listDownload
                    allDownload.append(detailDownload)
                objDownloads = {}
                objDownloads["format"] = "MP4" if index == 0 else "MKV" if index == 1 else "LAINNYA"
                objDownloads["list"] = allDownload
                downloads.append(objDownloads)

            detail["downloads"] = downloads
            response["code"] = code
            response["desc"] = desc
            response["data"] = detail
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {}
            }
            return response, 500
        
    def batch(self, id):
        try:
            linkComplete = link+"batch/"+id
            page = requests.get(linkComplete, allow_redirects=False)
            if page.status_code == 302 or page.status_code == 404:
                code = 404
                desc = "Not found"
                response = {}
                response["code"] = code
                response["desc"] = desc
                response["data"] = {}
                return response, code
            code = 200
            desc = "Success"
            detail = {}
            response = {}
            soup = BeautifulSoup(page.content, "lxml")
            info = soup.find("div", class_="infos").find_all("b")
            detail['title'] = info[0].next_sibling.strip().replace(": ","")
            detail['japanese'] = info[1].next_sibling.strip().replace(": ","")
            detail['type'] = info[2].next_sibling.strip().replace(": ","")
            detail['total_episode'] = info[3].next_sibling.strip().replace(": ","")
            detail['rating'] = info[4].next_sibling.strip().replace(": ","")
            detail['images'] = soup.select_one(".imganime").find("img").get("src")
            detail['duration'] = info[6].next_sibling.strip().replace(": ","")
            detail['studio'] = info[7].next_sibling.strip().replace(": ","")
            detail['producer'] = info[8].next_sibling.strip().replace(": ","")
            detail['date'] = info[9].next_sibling.strip().replace(": ","")
            detail['credit'] = info[10].next_sibling.strip().replace(": ","")
            allGenre = []
            genres = soup.find("div", class_="infos").find_all("a")
            for dataGenre in genres:
                    objGenre = {}
                    objGenre["name"] = dataGenre.get_text()
                    objGenre["id"] = dataGenre.get("href").replace(link+"genres/","").replace("/","")
                    allGenre.append(objGenre)
            detail["genres"] = allGenre
            downloads = []
            elementDownloads = soup.find("div",class_="batchlink").select("ul")
            for index, data in enumerate(elementDownloads):
                allDownload = []
                listResolusion = data.find_all("li")
                for list in listResolusion:
                    detailDownload = {}
                    listDownload = []
                    elementDetail = list.find_all("a")
                    for child in elementDetail:
                        obj = {}
                        obj["link"] = child.get("href")
                        obj["name"] = child.get_text().strip()
                        listDownload.append(obj)
                    detailDownload["resolution"] = list.find("strong").get_text().strip()
                    detailDownload["links"] = listDownload
                    allDownload.append(detailDownload)
                objDownloads = {}
                objDownloads["format"] = "MP4" if index == 0 else "LAINNYA"
                objDownloads["list"] = allDownload
                downloads.append(objDownloads)

            detail["downloads"] = downloads
            response["code"] = code
            response["desc"] = desc
            response["data"] = detail
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {}
            }
            return response, 500
    
    def random(self):
        try:
            linkComplete = link+"random"
            page = requests.get(linkComplete)
            if page.status_code == 404:
                code = 404
                desc = "Not found"
                response = {}
                response["code"] = code
                response["desc"] = desc
                response["data"] = {}
                return response, code
            code = 200
            desc = "Success"
            detail = {}
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div",class_="venser")
            details = element.find("div", class_="fotoanime").find_all("p")
            detail["main_title"] = element.find("div",class_="jdlrx").get_text().strip()
            detail["images"] = element.find("div", class_="fotoanime").find("img").get("src")
            detail["title"] = details[0].get_text().strip().replace("Judul: ","")
            detail["japanese"] = details[1].get_text().strip().replace("Japanese: ","")
            detail["rating"] = details[2].get_text().strip().replace("Skor: ","")
            detail["producer"] = details[3].get_text().strip().replace("Produser: ","")
            detail["type"] = details[4].get_text().strip().replace("Tipe: ","")
            detail["status"] = details[5].get_text().strip().replace("Status: ","")
            detail["total_episode"] = details[6].get_text().strip().replace("Total Episode: ","")
            detail["duration"] = details[7].get_text().strip().replace("Durasi: ","")
            detail["date"] = details[8].get_text().strip().replace("Tanggal Rilis: ","")
            detail["studio"] = details[9].get_text().strip().replace("Studio: ","")
            allGenre = []
            genres = details[10].find_all("a")
            for dataGenre in genres:
                    objGenre = {}
                    objGenre["name"] = dataGenre.get_text()
                    objGenre["id"] = dataGenre.get("href").replace(link+"genres/","").replace("/","")
                    allGenre.append(objGenre)
            detail["genres"] = allGenre
            animeList = element.select(".episodelist")
            batchs = []
            episodes = []
            batchList = animeList[0].find_all("li")
            episodeList = animeList[1].find_all("li")
            if episodeList:
                for episode in episodeList:
                    dataEpisode = {}
                    dataEpisode["id"] = episode.find("a").get("href").replace(link+"episode/","").replace("/","")
                    dataEpisode["title"] = episode.find("a").get_text().strip()
                    dataEpisode["date"] = episode.find("span",class_="zeebr").get_text().strip()
                    episodes.append(dataEpisode)
            if batchList:
                for batch in batchList:
                    dataBatch = {}
                    dataBatch["id"] = batch.find("a").get("href").replace(link+"batch/","").replace("/","")
                    dataBatch["title"] = batch.find("a").get_text().strip()
                    dataBatch["date"] = batch.find("span",class_="zeebr").get_text().strip()
                    batchs.append(dataBatch)
            detail["episodes"] = episodes
            detail["batch"] = batchs
            response = {}
            response["code"] = code
            response["desc"] = desc
            response["data"] = detail
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {}
            }
            return response, 500
