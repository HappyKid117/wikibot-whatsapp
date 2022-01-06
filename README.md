# wikibot-whatsapp
Wikipedia bot for whatsapp

This is made for Chrome version 96

Instructions:
1) Get the correct version of chromedriver
2) Open command prompt and start chrome with devtools and assign a port number
    example: chrome.exe –remote-debugging-port=8989 –user-data-dir=D:\Code\projects\chromeprofiledata
3) Ensure the port number is correct in wiki.py
4) Set your home_chat (preferably your phone number's chat)

Commands:
1) wiki <topic> : returns a summary of <topic>
2) go home bot : goes to your home_chat from any chat
3) bot go to <chat_name> : goes to <chat_name> if the bot is currently in home_chat
