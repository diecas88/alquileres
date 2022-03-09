# importar las librerias necesarias para hacer el proyecto
import requests
import lxml.html as html
import os
import datetime
import random

#variables estaticas que usaremos
URL_ORIGIN = 'https://www.properati.com.co/s/bucaramanga/apartamento/arriendo?page='
DOMAIN = 'https://www.properati.com.co'
INMUEBLES = '//h2/ancestor::a/@href'

TITLE = '//h1/text()'
PRICE = '//div[contains(@class,"MoneyBlock")]/div[position()=1]/span/text()'
DESCRIPTION = '//div[@class="child-wrapper"]/div[position()=1]/text()'
UNIQUE_ID = '//div[@class="child-wrapper"]/div[position()=2]/text()'
ADD_INFO= '//div[contains(@class,"ContentFe")]/div/div/ul/li/text()'
CHARACTERISTICS = '//div[contains(@class,"StyledTypology")]/div/div[position()=2]/span/text()'

def descripcion_inmueble(link):
    try:
        response = requests.get(DOMAIN + link)
        if response.status_code == 200:
            predio = response.content.decode('utf-8')
            parsed = html.fromstring(predio)
            
            try:

                unique_id = parsed.xpath(UNIQUE_ID)[1].replace('\n','').replace(',','')
                title = parsed.xpath(TITLE)[0].replace('\n','').replace(',','')
                price = parsed.xpath(PRICE)[2].replace('\n','').replace(',','')
                descrip = ' '.join(parsed.xpath(DESCRIPTION)).replace('\n','').replace(',','')
                add_info = '--'.join(parsed.xpath(ADD_INFO)).replace('\n','').replace(',','')
                habitaciones = parsed.xpath(CHARACTERISTICS)[0]
                banos = parsed.xpath(CHARACTERISTICS)[2]
                mtr2 = parsed.xpath(CHARACTERISTICS)[4]


            except IndexError:
                return

            with open('../raw/data_raw.txt', 'a', encoding='utf-8') as f:
                
                f.write('"' + unique_id + '","' + title + '","' + price + '","' + descrip + '","' + add_info + '","' + habitaciones + '","' + banos + '","' + mtr2 + '"')
                f.write('\n')
                f.close()

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)



def enter_home():

    #vamos a obtener el numero de paginas deseado para la consulta
    for n_page in range(0,30):
        #try catch para manejar errores
        try:
            # hacemos requerimiento a la pagin
            response = requests.get(URL_ORIGIN+str(n_page))
            # si nos da una respuesta positiva
            if response.status_code == 200:
                home = response.content.decode('utf-8')
                parsed = html.fromstring(home)
                url_inmueble = parsed.xpath(INMUEBLES)
                
                # crear archivo csv
                for link in url_inmueble:
                    descripcion_inmueble(link)

            # si no, entonces enviar error al except
            else:
                raise ValueError(f'Error: {response.status_code}')
        #mostrar error del try
        except ValueError as ve:
            print(ve)



def run():
    enter_home()

if __name__ == '__main__':
    run()