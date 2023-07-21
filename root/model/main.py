import requests
from bs4 import BeautifulSoup
link = "https://otakudesu.lol/"
replacerId = link+"anime/"

class Main:
    def home(self):
        try: 
            print(replacerId)
            page = requests.get(link)
            soup = BeautifulSoup(page.content, "lxml")
            ongoing = []
            completed = []
            element = soup.find("div", class_="venz")
            all_options = element.find_all("div", class_="detpost")
            for data in all_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                day = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "day": day,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                ongoing.append(obj)

            mainElement = soup.find("div", class_="rseries")
            secondElement = mainElement.find("div", class_="rseries")
            completed_options = secondElement.find_all("div", class_="detpost")
            for data in completed_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                rating = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rating": rating,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                completed.append(obj)
            
            response = {
                "code" : 200,
                "desc" : "Success",
                "data" : {
                    "ongoing" : ongoing,
                    "completed" : completed
                }
            }
            return response, 200
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "ongoing" : [],
                    "completed" : []
                }
            }
            return response, 500

    def completed(self):
        try:
            linkComplete = link+"complete-anime/"
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div", class_="venz")
            all_options = element.find_all("div", class_="detpost")
            pagination = soup.find("div", class_="pagination")
            paginate = []
            filterPagination = pagination.select(".page-numbers")
            for page in filterPagination:
                pageText = page.get_text().strip()
                if pageText.isnumeric(): 
                    pageNumber = int(pageText)
                else:
                    pageNumber = 0
                paginate.append(pageNumber)
            completed = []
            for data in all_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                rating = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rating": rating,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                completed.append(obj)

            if not completed:
                code = 404
                desc = "Not found"
            else: 
                code = 200 
                desc = "Success"
            response = {
                "code" : code,
                "desc" : desc,
                "data" : {
                    "completed" : completed,
                    "last_page" : max(paginate)
                }
            }
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "completed" : [],
                    "last_page" : 0
                }
            }
            return response, 500

    def completedWithPagination(self, page):
        try:
            linkComplete = link+"complete-anime/page/"+page
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div", class_="venz")
            all_options = element.find_all("div", class_="detpost")
            pagination = soup.find("div", class_="pagination")
            paginate = []
            filterPagination = pagination.select(".page-numbers")
            for page in filterPagination:
                pageText = page.get_text().strip()
                if pageText.isnumeric(): 
                    pageNumber = int(pageText)
                else:
                    pageNumber = 0
                paginate.append(pageNumber)
            completed = []
            for data in all_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                rating = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rating": rating,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                completed.append(obj)
            if not completed:
                code = 404
                desc = "Not found"
            else: 
                code = 200 
                desc = "Success"
            response = {
                "code" : code,
                "desc" : desc,
                "data" : {
                    "completed" : completed,
                    "last_page" : max(paginate)
                }
            }
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "completed" : [],
                    "last_page" : 0
                }
            }
            return response, 500

    def ongoing(self):
        try:
            linkComplete = link+"ongoing-anime/"
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div", class_="venz")
            all_options = element.find_all("div", class_="detpost")
            pagination = soup.find("div", class_="pagination")
            paginate = []
            filterPagination = pagination.select(".page-numbers")
            for page in filterPagination:
                pageText = page.get_text().strip()
                if pageText.isnumeric(): 
                    pageNumber = int(pageText)
                else:
                    pageNumber = 0
                paginate.append(pageNumber)
            ongoing = []
            for data in all_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                day = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "day": day,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                ongoing.append(obj)

            if not ongoing:
                code = 404
                desc = "Not found"
            else: 
                code = 200 
                desc = "Success"
            response = {
                "code" : code,
                "desc" : desc,
                "data" : {
                    "ongoing" : ongoing,
                    "last_page" : max(paginate)
                }
            }
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "ongoing" : [],
                    "last_page" : 0
                }
            }
            return response, 500

    def ongoingWithPagination(self, page):
        try:
            linkComplete = link+"ongoing-anime/page/"+page
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div", class_="venz")
            all_options = element.find_all("div", class_="detpost")
            pagination = soup.find("div", class_="pagination")
            paginate = []
            filterPagination = pagination.select(".page-numbers")
            for page in filterPagination:
                pageText = page.get_text().strip()
                if pageText.isnumeric(): 
                    pageNumber = int(pageText)
                else:
                    pageNumber = 0
                paginate.append(pageNumber)
            ongoing = []
            for data in all_options:
                episode = data.find("div", class_="epz").get_text().strip()
                date = data.find("div", class_="newnime").get_text().strip()
                day = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"").replace("/","")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "day": day,
                    "date": date,
                    "title": title,
                    "id":idAnime,
                    "images": images
                }
                ongoing.append(obj)
            if not ongoing:
                code = 404
                desc = "Not found"
            else: 
                code = 200 
                desc = "Success"
            response = {
                "code" : code,
                "desc" : desc,
                "data" : {
                    "ongoing" : ongoing,
                    "last_page" : max(paginate)
                }
            }
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "ongoing" : [],
                    "last_page" : 0
                }
            }
            return response, 500
        
    def genres(self):
        try:
            linkComplete = link+"genre-list/"
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("ul", class_="genres")
            all_options = element.find_all("a")
            genres = []
            for data in all_options:
                obj = {}
                obj["name"] = data.get_text().strip()
                idGenre = data.get("href")
                obj["id"] = idGenre.replace("genres/","").replace("/","")
                genres.append(obj)

            response ={
                "code" : 200,
                "desc" : "Success",
                "data" : genres
            }
            return response, 200
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": []
            }
            return response, 500
        
    def animeByGenre(self, id, page): 
        try: 
            linkComplete = link+"genres/"+id+"/page/"+page
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("div",class_="venser")
            all_options = element.find_all("div", class_="col-anime")
            anime = []
            pagination = soup.find("div", class_="pagination")
            paginate = []
            filterPagination = pagination.select(".page-numbers")
            for page in filterPagination:
                pageText = page.get_text().strip()
                if pageText.isnumeric(): 
                    pageNumber = int(pageText)
                else:
                    pageNumber = 0
                paginate.append(pageNumber)
            for data in all_options:
                obj = {}
                obj["title"] = data.find("a").get_text().strip()
                obj["id"] = data.find("a").get("href").replace(link+"anime","").replace("/","")
                obj["studio"] = data.find("div",class_="col-anime-studio").get_text().strip()
                obj["episode"] = data.find("div",class_="col-anime-eps").get_text().strip()
                obj["rating"] = data.find("div",class_="col-anime-rating").get_text().strip()
                obj["date"] = data.find("div",class_="col-anime-date").get_text().strip()
                obj["synopsis"] = data.find("div",class_="col-synopsis").get_text().strip()
                obj["images"] = data.find("div",class_="col-anime-cover").find("img").get("src")
                allGenre = []
                genres = data.find("div",class_="col-anime-genre").find_all("a")
                for dataGenre in genres: 
                    objGenre = {}
                    objGenre["name"] = dataGenre.get_text()
                    objGenre["id"] = dataGenre.get("href").replace(link+"genres/","").replace("/","")
                    allGenre.append(objGenre)
                obj["genres"] = allGenre
                anime.append(obj)

            
            if not anime:
                code =  404
                desc = "Not found"
            else:
                code = 200
                desc = "Success"
            response = {}
            response["code"] = code
            response["desc"] = desc
            response["data"] = {
                "anime" : anime,
                "last_page" : max(paginate)
            }
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": {
                    "anime" : [],
                    "last_page" : 0
                }
            }
            return response, 500
    
    def schedule(self):
        try:
            linkComplete = link+"jadwal-rilis"
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            schedules = []
            element = soup.find("div", class_="kgjdwl321")
            all_options = element.find_all("div",class_="kglist321")
            for data in all_options:
                obj = {}
                obj["day"] = data.find("h2").get_text().strip()
                animeList = []
                animes = data.find_all("a")
                for dataAnime in animes:
                    objAnime = {}
                    objAnime["id"] = dataAnime.get("href").replace(link+"anime/","").replace("/","")
                    objAnime["title"] = dataAnime.get_text().strip()
                    animeList.append(objAnime)
                obj["anime"] = animeList  
                schedules.append(obj)

            response = {}
            response["code"] = 200
            response["desc"] = "Success"
            response["data"] = schedules
            return response
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": []
            }
            return response, 500

    def search(self, searching):
        try: 
            parse = searching.strip().replace(" ", "+")
            linkComplete = link+"?s="+parse+"&post_type=anime"
            page = requests.get(linkComplete)
            soup = BeautifulSoup(page.content, "lxml")
            element = soup.find("ul", class_="chivsrc")
            all_options = element.find_all("li")
            searchAnime = []
            for data in all_options:
                obj ={}
                obj["images"] = data.find("img").get("src")
                obj["title"] = data.find("a").get_text().strip()
                obj["id"] = data.find("a").get("href").replace(link+"anime/","").replace("/","")
                allSet = data.select(".set")
                for set in allSet:
                    set.b.decompose()
                allGenre = []
                genres = allSet[0].find_all("a")
                for dataGenre in genres:
                    objGenre = {}
                    objGenre["name"] = dataGenre.get_text()
                    objGenre["id"] = dataGenre.get("href").replace(link+"genres/","").replace("/","")
                    allGenre.append(objGenre)

                obj["genres"] = allGenre
                obj["status"] = allSet[1].get_text().strip().replace(": ","")
                obj["rating"] = allSet[2].get_text().strip().replace(": ","")
                searchAnime.append(obj)
            
            if not searchAnime:
                code = 404
                desc = "Not found"
            else:
                code = 200
                desc = "Success"
            
            response = {}
            response["code"] = code
            response["desc"] = desc
            response["data"] = searchAnime
            return response, code
        except Exception as e:
            response = {
                "code": 500,
                "desc": "Internal server error " + str(e),
                "data": []
            }
            return response, 500
        