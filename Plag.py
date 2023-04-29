import requests


paperurl = []
def paper_id_finder(keyword):
    url = "https://api.semanticscholar.org/graph/v1/paper/search?query="
    url2 = "https://www.semanticscholar.org/paper/"
    payload={}
    headers = {}
    for x in keyword:
        response = requests.request("GET", url + x, headers=headers, data=payload).json()
        try:
            paper_data = response["data"]
            for paper in paper_data:
                print("id="+paper["paperId"] + "====>" + paper["title"])
                paperurl.append(url2+paper["paperId"])
        except:
            print(response)

def papercollector(paperurl):
    for x in paperurl:
        payload={}
        headers = {}
        response = requests.request("GET", x, headers=headers, data=payload).json()
        print(response)
        print("----------------------------")

keyword =["Machine Learning", "blockchain", "xray", "medical imageing"]
paper_id_finder(keyword)
print(paperurl)
print("====================================================================")
papercollector(paperurl)










# open_urls_in_chrome(paperurl)
# url = "https://api.semanticscholar.org/graph/v1/paper/search?query='00'"


# import webbrowser

# def open_urls_in_chrome(url_list):
#     for url in url_list:
#         webbrowser.get("chrome").open(url)


# keyword = ["Machine Learning", "IOT", "AI"]
# for i in keyword:
#     newurl = url.replace("00", i)
#     response = requests.request("GET", url, headers=headers, data=payload)
#     Data = response.json()
#     dataarray = Data["data"]
#     for paper in dataarray:
#         print("id="+paper["paperId"] + "====>" + paper["title"])
#         url2 = "https://www.semanticscholar.org/paper/"+ paper["paperId"]
#         paperurl.append(url2)
#         print("-----------------------------------------")
#     print("==========================================================")


# [
#     'https://www.semanticscholar.org/paper/51d188c003090bac18f40d01d91b06780fa4c414', 
#     'https://www.semanticscholar.org/paper/857f9f37f3b000285a53e2237e0acbf8cf675057', 
#     'https://www.semanticscholar.org/paper/f7e538b5b0f40152ba54877c0e08e76dcc85f469', 
#     'https://www.semanticscholar.org/paper/ac0853e983c33e664868149b5cf9668d7cc482fc', 
#     'https://www.semanticscholar.org/paper/d9adbd906bbf42df94153c9989f80baef44ed6ef', 
#     'https://www.semanticscholar.org/paper/d3fb0683ac5b039592f7a0113cb7b249898387d4', 
#     'https://www.semanticscholar.org/paper/bf0bda863693875db70177b1195986762a1656bb', 
#     'https://www.semanticscholar.org/paper/829110e4f37138a311bd0df1627ba689d1a69075', 
#     'https://www.semanticscholar.org/paper/3638b16a7b134bb42388f0a779086a1540d488b6', 
#     'https://www.semanticscholar.org/paper/75cd37dc1efcafb9abf2c9127a5e620a72ffd24c', 
#     'https://www.semanticscholar.org/paper/51d188c003090bac18f40d01d91b06780fa4c414', 
#     'https://www.semanticscholar.org/paper/857f9f37f3b000285a53e2237e0acbf8cf675057', 
#     'https://www.semanticscholar.org/paper/f7e538b5b0f40152ba54877c0e08e76dcc85f469', 
#     'https://www.semanticscholar.org/paper/ac0853e983c33e664868149b5cf9668d7cc482fc', 
#     'https://www.semanticscholar.org/paper/d9adbd906bbf42df94153c9989f80baef44ed6ef', 
#     'https://www.semanticscholar.org/paper/d3fb0683ac5b039592f7a0113cb7b249898387d4', 
#     'https://www.semanticscholar.org/paper/bf0bda863693875db70177b1195986762a1656bb', 
#     'https://www.semanticscholar.org/paper/829110e4f37138a311bd0df1627ba689d1a69075', 
#     'https://www.semanticscholar.org/paper/3638b16a7b134bb42388f0a779086a1540d488b6', 
#     'https://www.semanticscholar.org/paper/75cd37dc1efcafb9abf2c9127a5e620a72ffd24c', 
#     'https://www.semanticscholar.org/paper/51d188c003090bac18f40d01d91b06780fa4c414', 
#     'https://www.semanticscholar.org/paper/857f9f37f3b000285a53e2237e0acbf8cf675057', 
#     'https://www.semanticscholar.org/paper/f7e538b5b0f40152ba54877c0e08e76dcc85f469', 
#     'https://www.semanticscholar.org/paper/d9adbd906bbf42df94153c9989f80baef44ed6ef', 
#     'https://www.semanticscholar.org/paper/d3fb0683ac5b039592f7a0113cb7b249898387d4', 
#     'https://www.semanticscholar.org/paper/bf0bda863693875db70177b1195986762a1656bb', 
#     'https://www.semanticscholar.org/paper/3638b16a7b134bb42388f0a779086a1540d488b6', 
#     'https://www.semanticscholar.org/paper/829110e4f37138a311bd0df1627ba689d1a69075', 
#     'https://www.semanticscholar.org/paper/75cd37dc1efcafb9abf2c9127a5e620a72ffd24c', 
#     'https://www.semanticscholar.org/paper/5fc1f399c771a198e289715146648c94f79c59ac'
# ]

    



