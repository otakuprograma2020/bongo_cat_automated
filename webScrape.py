import shutil, re, zipfile, json, requests
import selenium.webdriver.chrome.options as chromeOptions
import sys
import base64
from bs4 import BeautifulSoup
from time import sleep, ctime
from os import path, environ, listdir, remove, chmod, mkdir, system, name

class WebScrape:
    """ Classe contém funções para realizar extração de dados na web, seja usando selenium ou bs4 """
    def __init__(self, headers=None, feature=None, path_armadilha=None):
        if(headers):
            self.headers = headers
        else:
            self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            }
        if(feature):
            self.feature = feature
        else:
            self.feature = 'html.parser'
        self.chrome_options = chromeOptions.Options()
        self.chrome_extension = self.chromeAppData()

    def webScraping(self,feature=None, url=None, cookies =None, markup=None, headers=None, request=None, pause=None):
        """ retorna objeto BeautifulSoup com os dados do html seja ele vindo da requisição ou de html passado para função"""
        try:
            if(not request):
                if(url):
                    if(pause):
                        sleep(pause)
                    if(headers):
                        request = requests.get(url, headers=headers, cookies=cookies)
                    else:
                        request = requests.get(url, headers=headers, cookies=cookies)
            
            if(markup):
                if(feature):
                    soup = BeautifulSoup(markup, feature)
                else:
                    soup = BeautifulSoup(markup, self.feature)
            else:
                if(feature):
                    soup = BeautifulSoup(request.content, feature,from_encoding="utf-8")
                else:
                    soup = BeautifulSoup(request.content, feature,from_encoding="utf-8")
            return soup
        except requests.exceptions.ConnectionError as err:
            print('Erro de conexão: {0}'.format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def chromeAppData(self):
        """ Verifica se existe o caminho de extensões do chrome, caso não exista indica que não há uma instalação do chrome """
        try:
            if(name == 'nt'):
                chrome_extension = path.join(environ['USERPROFILE'], 'AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions')
            else:
                chrome_extension = path.join(environ['HOME'], '.config/google-chrome/Default/Extensions')
            if(path.isdir(chrome_extension)):
                return chrome_extension
            else:
                print('Instale o google chrome')
                sys.exit(0)
        except Exception as err:
            print('ERRO (chromeAppData): {}'.format(err))
    
    def optionsChrome(self, headless=False):
        """ Configura opções para chrome """
        print('Configurando navegador Chrome ...')
        if(headless):
            self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=600x600")
        self.chrome_options.add_argument("--disable-notifications")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--verbose')
        self.chrome_options.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        })
        self.chrome_options.add_experimental_option('useAutomationExtension', False)
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-software-rasterizer')
        return self.chrome_options