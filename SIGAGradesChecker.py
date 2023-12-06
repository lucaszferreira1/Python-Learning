from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from telegram import Bot
from hashlib import sha256
import asyncio
import time


async def enviar_notificacao(bot, msg):
    await bot.send_message(chat_id='6387851237', text=msg)

# Remover comentários desta função
def realizar_login(driver, username, password):
    #script = f'''
    #    document.getElementById('j_username').value = '{username}';
    #    document.getElementById('senha').value = '{password}';
    #    realizarLogin();
    #'''
    driver.execute_script(script)


def buscar_semestre(semestre, driver):
    text_field = driver.find_element("xpath", "//input[@id='formPrincipal:input_filtro_aca_periodo_letivo_campo_input']")
    driver.execute_script("arguments[0].value = '';", text_field)
    time.sleep(1)
    text_field.send_keys(semestre)
    time.sleep(1)
    text_field.send_keys(Keys.RETURN)


def getNotas(n, driver):
    notas = []
    for i in range(0, n):
        field = driver.find_element('id', f'formPrincipal:notasFaltas:{i}:j_idt180')
        notas.append(field.text)
    return notas


async def main():
    username = 'username'
    password = 'password'
    login_url = 'https://siga.udesc.br/sigaSecurityG5/login.jsf?tipoLogin=PADRAO&motivo=SESSAO_DESTRUIDA_POR_USUARIO&evento=logout&codigoSistemaLogout=EDU09'
    target_url = 'https://siga.udesc.br/sigaMentorWebG5/jsf/central/cal/notasFaltas.jsf'

    bot_token = "token"
    bot = Bot(token=bot_token)

    notas_antigas = []
    first = True

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    campos_xpath = ['formPrincipal:notasFaltas::j_idt180']

    while True:
        if first:
            first = False
            msg = 'Bot Iniciado!'
        else:
            msg = 'Notas Atualizadas!'

        # Log in to the website using Selenium
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(login_url)

        realizar_login(driver, username, password)
        time.sleep(5)

        driver.get(target_url)
        time.sleep(5)

        buscar_semestre('2023/2', driver)
        time.sleep(5)

        notas_atuais = getNotas(5, driver)

        if notas_atuais != notas_antigas:
            await enviar_notificacao(bot, msg)
            notas_antigas = notas_atuais
        # Close the WebDriver when done
        driver.quit()
        time.sleep(100)

if __name__ == "__main__":
    asyncio.run(main())
