from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from telegram import Bot
import asyncio
import time
import winsound


async def enviar_notificacao(bot, msg):
    await bot.send_message(chat_id='6387851237', text=msg)


def elemento_existe(driver, id):
    try:
        driver.find_element('id', id)
    except NoSuchElementException:
        return False
    return True


def realizar_login(driver, username, password):
    script = f'''
        document.getElementById('j_username').value = '{username}';
        document.getElementById('senha').value = '{password}';
        realizarLogin();
    '''
    driver.execute_script(script)


def buscar_semestre(semestre, driver):
    text_field = driver.find_element("xpath", "//input[@id='formPrincipal:input_filtro_aca_periodo_letivo_campo_input']")
    driver.execute_script("arguments[0].value = '';", text_field)
    time.sleep(1)
    text_field.send_keys(semestre)
    time.sleep(1)
    text_field.send_keys(Keys.RETURN)


def buscar_notas_parciais(driver):
    text_field = driver.find_element("xpath", "//input[@id='formPrincipal:j_idt170_campo_input']")
    driver.execute_script("arguments[0].value = '';", text_field)
    time.sleep(1)
    text_field.send_keys('Nota')
    time.sleep(1)
    text_field.send_keys(Keys.RETURN)


def getNotas(driver):
    notas = {}
    test = elemento_existe(driver, f'formPrincipal:notasFaltas:0:j_idt177')
    cont = 0
    while test:
        field_disc = driver.find_element('id', f'formPrincipal:notasFaltas:{i}:j_idt177')
        if elemento_existe(driver, f'formPrincipal:notasFaltas:{i}:j_idt183'):
            field_nota = driver.find_element('id', f'formPrincipal:notasFaltas:{i}:j_idt183')
        else:
            field_nota = driver.find_element('id', f'formPrincipal:notasFaltas:{i}:j_idt185')
        notas[field_disc.text] = field_nota.text
        cont += 1
        test = elemento_existe(driver, f'formPrincipal:notasFaltas:{i+1}:j_idt177')
    return notas


def play_ding():
    winsound.PlaySound('ding.wav', winsound.SND_FILENAME)


async def main():
    username = 'user'
    password = 'password'
    login_url = 'https://siga.udesc.br/sigaSecurityG5/login.jsf?tipoLogin=PADRAO&motivo=SESSAO_DESTRUIDA_POR_USUARIO&evento=logout&codigoSistemaLogout=EDU09'
    target_url = 'https://siga.udesc.br/sigaMentorWebG5/jsf/central/cal/notasFaltas.jsf'

    bot_token = "token"
    bot = Bot(token=bot_token)

    notas_antigas = {}
    first = True
    diff = False

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')


    while True:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(login_url)

        realizar_login(driver, username, password)
        time.sleep(1)
        driver.get(target_url)
        time.sleep(2)

        buscar_semestre('2024/1', driver)
        time.sleep(2)
        buscar_notas_parciais(driver)
        time.sleep(2)

        notas_atuais = getNotas(driver)
        print(notas_atuais)
        
        if first:
            msg = 'Bot Iniciado!'
        else:
            msg = ''
            for chave in notas_atuais.keys():
                if notas_atuais[chave] != notas_antigas[chave]:
                    msg += f'{chave}: {notas_atuais[chave]}\n'
                    diff = True

        if diff or first:
            await enviar_notificacao(bot, msg)
            notas_antigas = notas_atuais
            play_ding()
            diff = False
            first = False

        driver.quit()
        time.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
