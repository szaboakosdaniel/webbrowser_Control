# File: Statemachine.py
# Author: Szabo Akos Daniel
# Description: This script demonstrates how to control a web browser programmatically.

from statemachine import StateMachine, State
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import pyautogui
import time
import socket


#Youtube specific function using Selenium
class YoutubeBrowser():
        
    driver="NULL"
    URL_open="NULL"   

#Start Stop Youtube video
    def Play(self):
        pyautogui.press('k')

#Next video
    def Next(self):
        pyautogui.keyDown('shift')
        pyautogui.press('n')
        pyautogui.keyUp('shift')

#Full screen
    def Full(self):
        pyautogui.press('f')
#Start Browser    
    def Start(self):
        firefox_options = Options()
        firefox_options.add_argument("--kiosk")  # Fullscreen mode
        self.driver = webdriver.Firefox(options=firefox_options)
        print("Ez oké?")
#Open URL    
    def Open(self):
        print(self.URL_open)
        self.driver.get(self.URL_open)
        print("Betöltött")

#Click Accept cookie button
    def Accept_All(self):
        wait = WebDriverWait(self.driver, 20)
        button_locator = self.driver.find_element(By.XPATH,"//button[contains(.,'" + "Accept all" + "')]"); #Elfogadó gomb
        try:
            # Wait until the button is clickable
            button_element = wait.until(EC.element_to_be_clickable(button_locator))
            print("Gomb lathato")
            # Click the button
            button_element.click()
        except Exception as e:
            print("An error occurred:", str(e))

#Click on Play_all  (play list)
    def Play_All(self):
        wait = WebDriverWait(self.driver, 20)
        button_locator = self.driver.find_element(By.XPATH,"//a[contains(.,'" + "Play all" + "')]");
        try:
            # Wait until the button is clickable
            button_element = wait.until(EC.element_to_be_clickable(button_locator))
            print("Gomb lathato")
            #Click the button
            button_element.click()
            time.sleep(5)
            pyautogui.press('f')
        except Exception as e:
            print("An error occurred:", str(e))

#Close browser
    def Quit(self):
        self.driver.quit()

#StateMachine Class
class BrowserControlMachine(StateMachine,YoutubeBrowser):
#States for webbrowser control
    START= State(initial=True)
    INIT = State()
    WAIT_FOR_CONNECTION = State()
    WAIT_FOR_MESSAGE = State()
    DECODE_MESSAGE = State()
    EXECUTE_COMMAND = State()
    STOP =State(final = True)

#Transition between states
    a=START.to(INIT)
    b=INIT.to(WAIT_FOR_CONNECTION)
    c=WAIT_FOR_CONNECTION.to(WAIT_FOR_MESSAGE)
    d=WAIT_FOR_MESSAGE.to(DECODE_MESSAGE)
    e=DECODE_MESSAGE.to(EXECUTE_COMMAND)
    f=EXECUTE_COMMAND.to(STOP)
# Grouped States
    start = a | b
    cycle = c | d | e

#Function to get Server IP
    def get_internal_ip(self):
        try:
            internal_ip = socket.gethostbyname(socket.gethostname())
            print(internal_ip)
            return internal_ip
        except Exception as e:
            print("Hiba a belső IP lekérdezése közben:", e)
            return None
        
        
#Private variables
    def __init__(self):
        self.server_ip=self.get_internal_ip()
        self.server_port = 12345
        self.client_socket=None
        self.received_message="NULL"
        self.decoded_message="NULL"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.FFBrowser=YoutubeBrowser()
        self.on_enter_START()
#Setters
    def set_server_ip(self, value):
        self.server_ip = value

    def set_server_port(self, value):
        self.server_port = value

    def set_client_socket(self, value):
        self.client_socket = value

    def set_received_message(self, value):
        self.received_message = value

    def set_decoded_message(self, value):
        self.received_message = value

    def set_server_socket(self, value):
        self.server_socket = value

#Getters
    def get_server_ip(self):
        return self.server_ip

    def get_server_port(self):
        return self.server_port

    def get_client_socket(self):
        return self.client_socket

    def get_received_message(self):
        return self.received_message
    
    def get_decoded_message(self):
        return self.received_message

    def get_server_socket(self):
        return self.server_socket

#Check TCP/IP Connection
    def check_connection(self):
        print("1")
        if self.client_socket is None:
            return False
            
        try:
            self.client_socket.send(b' ')
            return True
        except:
            return False
           


#State functions

#START
    def on_enter_START(self):
        print("Start state...")
        self.on_enter_INIT()
#INIT
    def on_enter_INIT(self):
        print("Init state...")
        self.server_socket.bind((self.server_ip, self.server_port))
        self.on_enter_WAIT_FOR_CONNECTION()
     
#WAIT_FOR_CONNECTION
    def on_enter_WAIT_FOR_CONNECTION(self):
        print("Wait for connection...")
        self.server_socket.listen(1)  # Maximum 1 kapcsolatot várakoztatunk
        self.client_socket, client_address = self.server_socket.accept()
        print(f"Kliens kapcsolódott: {client_address}")
        self.on_enter_WAIT_FOR_MESSAGE()


#WAIT_FOR_MESSAGE
    def on_enter_WAIT_FOR_MESSAGE(self):
            print("Varakozas üzenetre...")
            try:
                 with self.client_socket:    
                    while True:
                            data = self.client_socket.recv(1024)
                            if not data:
                                break
                            else:
                                self.received_message = data.decode("utf-8")
                                self.on_enter_DECODE_MESSAGE()
            except Exception as e:
                print("Kivetel keletkezett:", e)
                self.client_socket.close()
                self.on_enter_WAIT_FOR_CONNECTION()

    #DECODE_MESSAGE
    #TCP/IP socket encrypton need to be implemented
    def on_enter_DECODE_MESSAGE(self):
        print("Üzenet dekodolasa...")
        self.decoded_message=self.received_message #Decoding message need to implemented in this function
        print(self.decoded_message)
        print("Üzenet erkezett:")
        self.on_enter_EXECUTE_COMMAND()
        

 
#EXECUTE_COMMAND
    def on_enter_EXECUTE_COMMAND(self):
        
        #Check if đ in the message
        if 'đ' in self.decoded_message:
            parts = self.decoded_message.split('đ') 
            message=parts[0]
        else:
            message=self.decoded_message
        
        #if message open then opens the gcen url
        if message=="open":
            if self.FFBrowser.driver=="NULL":
                self.FFBrowser.Start()
            self.FFBrowser.URL_open=parts[1]
            print(self.FFBrowser.URL_open)
            self.FFBrowser.Open()
            print("Parancs vegrehajtasa...")
        elif message=="play_stop\n":
            self.FFBrowser.Play()
        elif message=="next\n":
            self.FFBrowser.Next()
        elif message=="full\n":  
            self.FFBrowser.Full()
        elif message=="accept_all\n":  
            self.FFBrowser.Accept_All()
        else:
            print("Not command")

        self.on_enter_WAIT_FOR_MESSAGE()


  

def main():
    test1=BrowserControlMachine()

if __name__ == "__main__":
    main()