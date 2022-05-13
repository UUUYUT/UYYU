#- - - - - - - - - - 
# => Bot Telegram  : .
# => Program : KABOS .
# => Kabos Tools - Team KRS . 
# => Dev Tele : @NnKoNn .
# => Dev - Ch Tele : @nn_konn .
M = "\033[1;96m"
#---------offices---------#
import telebot
import requests
from telebot import types
#---------commands_Bot---------#
tok_kabos = input(' ~ ToekN :'+M)
bot = telebot.TeleBot(tok_kabos)
kkaa = types.InlineKeyboardButton(text="- BooS × ",url="https://t.me/nn_konn")
kaa = types.InlineKeyboardButton(text="- List Visa ", callback_data='it')
sff = types.InlineKeyboardButton(text="- Get Visa ", callback_data='ti')
@bot.message_handler(commands = ["start"])
def kabos(message):
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 2
    Keyy.add(sff,kaa,kkaa)
    kafirst = message.chat.first_name
    aan = types.InlineKeyboardMarkup()
    aan.add(kkaa)
    bot.send_message(message.chat.id,text = f"""- Hi {kafirst} IN BOT GUESS VISA CARD .""",reply_markup=Keyy)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="ti":
        KABOS(call.message)
    elif call.data == "it":
    	KABS(call.message)

def KABOS(message):
        ka_A = message.text
        kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        req = requests.get(kabosinsta)
        res = req.json()
        j = res['CreditCard']['CardNumber']
        jh = res['CreditCard']['EXP']
        jj = res['CreditCard']['CVV']
        nn = res['information']['Name']
        hn = res['information']['Birthday']
        hj = res['information']['Gender']
        hdj = res['information']['Birthplace']
        dhdj = res['information']['Zodiac Sign']
        xhdj = res['information']['Address']
        q = res['information']['Company']
        w = res['information']['Phone Number']
        k = res['information']['Vehicle']
        txtkabos = f'''- NEW VISA .
- - - - - - - -
- Number Card : {j} .
---------------------
- ExP  : {jh} .
---------------------
- CvV  : {jj} .
---------------------
- Name : {nn} .
---------------------
- Birthday : {hn} .
---------------------
- Gender : {hj} .
---------------------
- Birthplace : {hdj} .
---------------------
- Zodiac Sign : {dhdj} .
---------------------
- Address : {xhdj} .
---------------------
---------------------
- Company : {q} .
---------------------
- Phone Number : {w} .
---------------------
- Vehicle : {k} .
- - - - - - - - 
        '''
        bot.send_message(message.chat.id,txtkabos)
        
        
def KABS(message):
        	ka_A = message.text
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	j = res['CreditCard']['CardNumber']
        	jh = res['CreditCard']['EXP']
        	jj = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jg = res['CreditCard']['CardNumber']
        	jhg = res['CreditCard']['EXP']
        	jjg = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	ju = res['CreditCard']['CardNumber']
        	jhu = res['CreditCard']['EXP']
        	jju = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jdf = res['CreditCard']['CardNumber']
        	jhdf = res['CreditCard']['EXP']
        	jjdf = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jxx = res['CreditCard']['CardNumber']
        	jhxx = res['CreditCard']['EXP']
        	jjxx = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jp = res['CreditCard']['CardNumber']
        	jhp = res['CreditCard']['EXP']
        	jjp = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	ji = res['CreditCard']['CardNumber']
        	jhi = res['CreditCard']['EXP']
        	jji = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	ja = res['CreditCard']['CardNumber']
        	jha = res['CreditCard']['EXP']
        	jja = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jt = res['CreditCard']['CardNumber']
        	jht = res['CreditCard']['EXP']
        	jjt = res['CreditCard']['CVV']
        	kabosinsta = f"https://cvcbnhfuu.ml/HMD/api/Random.php"
        	req = requests.get(kabosinsta)
        	res = req.json()
        	jg = res['CreditCard']['CardNumber']
        	jhg = res['CreditCard']['EXP']
        	jjg = res['CreditCard']['CVV']
        	txtkabjos = f'''- NEW LIST VISA .
- - - - - - - -
- ViSa : {j}|{jh}|{jj}
-
- ViSa : {jg}|{jhg}|{jjg}
-
- ViSa : {ju}|{jhu}|{jju}
-
- ViSa : {jdf}|{jhdf}|{jjdf}
-
- ViSa : {jxx}|{jhxx}|{jjxx}
-
- ViSa : {jp}|{jhp}|{jjp}
-
- ViSa : {ji}|{jhi}|{jji}
-
- ViSa : {ja}|{jha}|{jja}
-
- ViSa : {jt}|{jht}|{jjt}
-
- ViSa : {jg}|{jhg}|{jjg}
- - - - - - - - 
        '''
        	bot.send_message(message.chat.id,txtkabjos)
bot.polling(True)