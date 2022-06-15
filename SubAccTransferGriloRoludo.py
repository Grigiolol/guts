import json
import samino
import hmac
from hashlib import sha1
import os
from os import path
import pyfiglet
from time import sleep
import time
from pyfiglet import figlet_format
from colored import fg, bg, attr
def generate_device_Id():
        identifier = os.urandom(20)
        return("42" + identifier.hex() + hmac.new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()
        
#
#
#                                      🐈‍⬛
#                          Script by Grígio
#
# ============= OBSERVAÇÃO ===========
#
#   Por favor, não alterar as informações do
#   script ou ele provavelmente irá parar de
#   funcionar!
# #======================================

# color = bg('gold_1') + fg('black')
color2 = bg('orange_red_1') + fg('white')
color3 = bg('red_1') + fg('black')
color4 = bg('white') + fg('black')
##color3 = bg('yellow_1') + fg('black')
##color3 = bg('yellow_1') + fg('black')

color3 = bg('gold_1') + fg('black')
color = bg('gold_1') + fg('black')
# color = bg('red_1') + fg('white')
color4 = bg('white') + fg('black')
##color3 = bg('yellow_1') + fg('black')
##color3 = bg('yellow_1') + fg('black')
logo = pyfiglet.figlet_format(text="       SUBMUNDO", font="small")
	
reset = attr('reset')
def clear():
	os.system('clear')
	print(logo)
print("""



""")
print(""" 
Tenha a noção de que 
o amino está impondo 
novas mecanicas. Dado 
este fato, nosso coletor 
trabalha de forma devagar, 
contudo, ele é preciso e 
não vai deixar de coletar 
em nenhuma das contas. 

""")
sleep(1.0)
input(color+"Pressione ENTER para continuar..."+reset)
clear()
print("""                                                🐈‍⬛""")
print("   " + color + (" × ") + (" COLETOR ") + "            " + color4 + ("  × ByGrilo") + (" Lith ") + reset)
print("   " + color + (" × ") + (" SUBMUNDO") + "            " + color4 + ("  × Privado") + (" R$15 ") + reset)
sleep(2.0)
print(""" 

- Abaixo você deverá preencher com o nome e extensão (.json) do
arquivo de contas que você que coletar!
""")
arquivo=input("\n   " + color + " × NOME DO ARQUIVO : " + reset)
clear()
print(""" - Abaixo você deverá preencher com o link do blog qual você quer
que as contas mandem as coins!
""")
link=input("\n   " + color + " × LINK DO BLOG : " + reset)
file = path.dirname(path.abspath(__file__))
acc=path.join(file,arquivo)
client = samino.Client(generate_device_Id())
id=client.get_from_link(link)
clear()
comId=id.comId
blogId=id.objectId
dictlist=[]
with open(acc) as f:
    dictlist = json.load(f)
    def threadit(acc : dict):
    	email=acc["email"]
    	password=acc["password"]
    	device=acc["device"]
    	
    	client=samino.Client(deviceId=device)
    	try:
    		client.login(email,password)
    		print("\n   " + color4 + f" × LOGADO EM {email}"+reset)
    		client.join_community(comId)
    		print("\n   " + color + " × ENTRANDO NA COMUNIDADE " + reset)
    		coin=int(client.get_wallet_history().json['coinHistoryList'][0]['totalCoins'])
    		print("\n   "+ color+f" × A CONTA TEM {coin} COINS"+reset)
    		if coin>500:
    			ra = coin/500
    			if ra>9:
    				raa=9
    			else:
    				raa=ra
    			for i in range(int(raa)):
    				samino.Local(comId).tip_coins(coins=int(500),blogId=blogId)
    				print("\n   " + color + " × ENVIADO 500" + reset)
    				time.sleep(1.0)
    				
    		elif coin<1:
    			pass
    		else:
    			coinss=coin
    		coins=int(client.get_wallet_history().json['coinHistoryList'][0]['totalCoins'])	
    		samino.Local(comId).tip_coins(coins=int(coins),blogId=blogId)
    		time.sleep(1.0)
    		print(f"\n   " + color + f" × ENVIADO {coins} \n"+reset)
    		print("\n   "+color+" × -------------------------- × "+reset)
    	except Exception as e:
    		print(e)
    		pass
    	
for amp in dictlist:
	threadit(amp)