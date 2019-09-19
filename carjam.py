from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import threading
from threading import Thread
lock = threading.Lock()
import logging
import sys
import datetime
from selenium.webdriver.chrome.options import Options
import pickle
import time

chrome_path = r"/Users/oscar/Projects/syn/trawler/chromedriver"

#output_cars = r"/Users/oscarxw/Projects/syn/trawler/output_cars.obj"
#filehandler = open(output_cars, 'wb')

class Car:
    def __init__(self):
        self.plate = None
        self.exists = False
        self.year = None
        self.make = None
        self.model = None
        self.smodel = None
        self.bstyle = None
        self.vin = None

    def __str__(self):
        str = ""
        if self.exists:
            if self.year is not None:
                str += "Year: " + self.year + "\n"
            if self.make is not None:
                str += "Make: " + self.make + "\n"
            if self.model is not None:
                str += "Model: " + self.model + "\n"
            if self.smodel is not None:
                str += "Submodel: " + self.smodel + "\n"
            if self.bstyle is not None:
                str += "Body Style: " + self.bstyle + "\n"
            if self.vin is not None:
                str += "VIN: " + self.vin + "\n"
        else:
            str = "Plate: " + self.plate + " has never been registered" + "\n"

        return str


files = [a.rstrip() for a in open('new_plates.txt').readlines()]
css_output = open('test_output.css', 'w')

writing = []

def write_to_csv():
    if len(writing) == 0:
        time.sleep(0.5)
    else:
        print(writing)
        css_output.write(writing.pop(0))


def main():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path=chrome_path)
    for itt in range(len(files)):
        plate = files.pop(0)
        driver.get("https://carjam.co.nz/car/?plate=" + plate)
        YEAR, MAKE, MODEL, SMODEL, BSTYLE = None, None, None, None, None
        print(plate + " starting...")

        running = True

        while running:

            if driver.title.startswith("Report"):
                try:
                    YEAR = driver.find_element_by_xpath("//*[contains(text(), 'Year:')]/../span[2]").text
                except: None
                try:
                    MAKE = driver.find_element_by_xpath("//*[contains(text(), 'Make:')]/../span[2]").text
                except: None
                try:
                    MODEL = driver.find_element_by_xpath("//*[contains(text(), 'Model:')]/../span[2]").text
                except: None
                try:#
                    SMODEL = driver.find_element_by_xpath("//*[contains(text(), 'Submodel:')]/../span[2]").text
                except: None
                try:
                    BSTYLE = driver.find_element_by_xpath("//*[contains(text(), 'Body Style:')]/../span[2]").text
                except: None

                outputerst = str(YEAR) + "," + str(MAKE) + "," + str(MODEL) + "," + str(SMODEL) + "," + str(BSTYLE) + "\n"
                writing.append(outputerst)


                running = False
                print(plate + " finished...")

            elif driver.title == "Vehicle information, history check and reports | CarJam":
                running = False

            else:
                time.sleep(0.1)

writing_worker = Thread(target=write_to_csv())
writing_worker.start()

main()