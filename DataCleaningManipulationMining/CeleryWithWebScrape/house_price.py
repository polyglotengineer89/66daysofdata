from requests import get
from bs4 import BeautifulSoup

import pandas as pd

def get_house_price():
    url = "http://www.olx.co.id/depok-kota_g4000024/dijual-rumah-apartemen_c5158?filter=type_eq_rumah"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    list_detail_house = html_soup.find_all(
        'li', class_='EIR5N')
    #print(list_detail_house.a)
    column = ['link', 'src', 'price', 'detail', 'title', 'location', 'publish']

    link_list = []
    img_list = []
    price_list = []
    detail_list = []
    title_list = []
    location_list = []
    publish_list = []

    for item in list_detail_house:
        link = item.a['href']
        img = item.a.figure.img['src']
        if item.find('div', class_='IKo3_') is not None:
            span_ik03 = item.find('div', class_='IKo3_')
            price = span_ik03.find('span', class_='_89yzn').text
            detail = span_ik03.find('span', class_='_2TVI3').text
            title = span_ik03.find('span', class_='_2tW1I').text
            if span_ik03.find('span', class_='_1KOFM') is not None:
                sub_detail = span_ik03.find('span', class_='_1KOFM')
                location = sub_detail.find('span', class_='tjgMj').text
                publish = sub_detail.find('span', class_='zLvFQ').span.text
            else:
                location = publish = None

            link_list.append(link)
            img_list.append(img)
            price_list.append(price)
            detail_list.append(detail)
            title_list.append(title)
            location_list.append(location)
            publish_list.append(publish)

            result = {'link': link_list,
                    'img': img_list,
                    'price': price_list,
                    'title': title_list,
                    'detail': detail_list,
                    'location': location_list,
                    'publish': publish_list
                    }

            harga_rumah = pd.DataFrame(result, columns=column)

            harga_rumah.to_excel("harga_rumah.xlsx")
        else:
            print("There is no data which can be scrape")


get_house_price()
