import numpy as np
import pandas as pd
import sys
import time
from datetime import time, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.crowley.com.br/cbab/relatorios/mailing_anual/TOP100BrasilTheCrowleyOfficialBroadcast2021.pdf")