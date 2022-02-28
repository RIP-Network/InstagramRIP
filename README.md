Creado por RIP-Network programa para banear gente en instagram , no me hago responsable de los usos . ;)

▓█████▄ ▓█████ ▓█████▄   ██████ ▓█████  ▄████▄     
▒██▀ ██▌▓█   ▀ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▒██▀ ▀█     
░██   █▌▒███   ░██   █▌░ ▓██▄   ▒███   ▒▓█    ▄    
░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒   
░▒████▓ ░▒████▒░▒████▓ ▒██████▒▒░▒████▒▒ ▓███▀ ░   
 ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░   
 ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒      
 ░ ░  ░    ░    ░ ░  ░ ░  ░  ░     ░   ░
   ░       ░  ░   ░          ░     ░  ░░ ░         
 ░              ░                      ░    
╦═╗╦╔═╗  ╔╗╔╔═╗╔╦╗╦ ╦╔═╗╦═╗╦╔═
╠╦╝║╠═╝  ║║║║╣  ║ ║║║║ ║╠╦╝╠╩╗
╩╚═╩╩    ╝╚╝╚═╝ ╩ ╚╩╝╚═╝╩╚═╩ ╩

version 1.1 ultima actualizacion el 23/02/2022

def open_followers(account_instagram):
   web.get("https://www.instagram.com/" + account_instagram + "/followers/")
   time.sleep(5)
   web.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()


   web.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()



   def new_page(new_page):
        web = webdriver.Firefox()
        web.get('http://instagram.com')
        time.sleep(5)# InstagramRIP
