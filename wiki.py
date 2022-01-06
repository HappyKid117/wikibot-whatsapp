import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import warnings
warnings.filterwarnings("ignore")

def get_summary(query):
    print("====Wikipedia Query====")
    print(">Query = "+query)
    suggestion = wikipedia.search(query, results=1)
    print(">Suggestion = "+suggestion[0])
    print("=======================")
    return wikipedia.summary(suggestion[0], sentences=2)

def functionality(x):
    print(">Latest message = "+x)
    if(x.startswith("wiki")):
        x = x.replace('wiki', '')
        send_message(get_summary(x))
    elif(x == "go home bot"):
        send_message("bye")
        go_to_chat(home_chat)
    elif(x.startswith("bot go to ")):
        chat_name = x.replace('bot go to ', '')
        current_chat = get_current_chat()
        if(current_chat==home_chat):
            send_message("I am going to "+chat_name)
            go_to_chat(chat_name)
            send_message("I am here")
        else:
            send_message("You can't ask me to go to "+chat_name+" from "+current_chat)

def send_message(string):
    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    input_box.send_keys("_*WikiBot:*_ "+string + Keys.ENTER)
    print(">Message sent")

def get_current_chat():
    print("printing current chat...")
    current_chat_xpath = '//span[@class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"]'
    current_chat_elements = driver.find_elements_by_xpath(current_chat_xpath)
    current_chat_name = current_chat_elements[-1].get_attribute("title")
    print(">Current chat = "+current_chat_name)
    return current_chat_name

def get_latest_message():
    messages = driver.find_elements_by_xpath('//span[@class="i0jNr selectable-text copyable-text"]')
    latest_message = messages[len(messages)-1].get_attribute("innerHTML")
    latest_message = latest_message.replace('<span>', '')
    latest_message = latest_message.replace('</span>', '')
    return latest_message

def go_to_chat(chat_name):
    search_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="3"]'
    search_box = driver.find_element_by_xpath(search_xpath)
    print(">Going to chat "+chat_name)
    search_box.send_keys(chat_name+Keys.ENTER)

def initialize():
    opt = Options()
    opt.add_experimental_option("debuggerAddress","localhost:8989")
    func_driver = webdriver.Chrome(chrome_options=opt)
    func_driver.get("https://web.whatsapp.com/")
    print(">Keep the tab active till your home chat appears")
    func_driver.implicitly_wait(40)
    return func_driver


# type in cmd ->>> chrome.exe –remote-debugging-port=8989 –user-data-dir=D:\Code\projects\chromeprofiledata

print(">Starting Bot...")
home_chat = 'your_chat' # set your private chat
print("Home chat = "+home_chat)
print(">Initializing driver...")
driver = initialize()
go_to_chat(home_chat)
print(">Driver initialized.")
old = ""
while(True):
    try:
        x = get_latest_message().lower()
        if old==x:
            continue
        old = x
        functionality(x)
    except:
        send_message("Something went wrong")
        print(">ERROR")
    time.sleep(1)