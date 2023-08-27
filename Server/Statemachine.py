from statemachine import StateMachine, State
import statemachine
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import string
import pyautogui
import time
import socket


class BrowserControlMachine(StateMachine):
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
    def get_internal_ip():
        try:
            internal_ip = socket.gethostbyname(socket.gethostname())
            print(internal_ip)
            return internal_ip
        except Exception as e:
            print("Hiba a belső IP lekérdezése közben:", e)
            return None
        
        
#Variables
    server_ip=get_internal_ip()
    server_port = 12345
    client_socket=None
    received_message="NULL"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        #self.server_ip=self.get_internal_ip()
        #self.server_port = 12345
        #self.client_socket=None
        #self.received_message="NULL"
        #self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.server_ip, self.server_port))
        self.on_enter_WAIT_FOR_CONNECTION()
     
#WAIT_FOR_CONNECTION
    def on_enter_WAIT_FOR_CONNECTION(self):
        print("Wait for connection...")
        self.server_socket.listen(1)  # Maximum 1 kapcsolatot várakoztatunk
        self.client_socket, client_address = self.server_socket.accept()
        print(f"Kliens kapcsolódott: {client_address}")
        self.on_enter_WAIT_FOR_MESSAGE()

    def on_WAIT_FOR_CONNECTION(self):
       # self.state = self.cycle
        print("itt vagy?")
        return True
        # Itt helyezd el a WAIT_FOR_CONNECTION állapotba tartozó kódodat

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
                #self.server_socket.close()
                self.on_enter_WAIT_FOR_CONNECTION()

    #DECODE_MESSAGE
    def on_enter_DECODE_MESSAGE(self):
        print("Üzenet dekodolasa...")
        if self.received_message=="hello\n":
            print("Üzenet erkezett:")#, self.no_device_foundreceived_message)
            self.on_enter_EXECUTE_COMMAND()
        else:
            #self.trigger(self.events.not_valid_message)
            print("Ez nem üzenet...")

 
#EXECUTE_COMMAND
    def on_enter_EXECUTE_COMMAND(self):
       print("Parancs vegrehajtasa...")
       self.on_enter_WAIT_FOR_MESSAGE()
        # Itt helyezd el az EXECUTE_COMMAND állapotba tartozó kódodat

def main():
    test=BrowserControlMachine()

if __name__ == "__main__":
    main()