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
                idAnime = anime.find("a").get("href").replace(replacerId,"")
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
                rate = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rate": rate,
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
            filterPagination = pagination.find_all("a")
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
                rate = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rate": rate,
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
                    "ongoing" : [],
                    "completed" : []
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
                rate = data.find("div", class_="epztipe").get_text().strip()
                anime = data.find("div", class_="thumb")
                title = anime.find("h2").get_text().strip()
                idAnime = anime.find("a").get("href").replace(replacerId,"")
                images = anime.find("img").get("src")
                obj = {
                    "episode" : episode,
                    "rate": rate,
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
                    "ongoing" : [],
                    "completed" : []
                }
            }
            return response, 500