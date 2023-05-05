from selenium import webdriver
from decimal import Decimal
import time

# Configurando o driver do Chrome
driver = webdriver.Chrome('/path/to/chromedriver')

# Acessando a página do livro
driver.get('https://www.kabum.com.br/produto/364836/monitor-gamer-lg-34-led-ultra-wide-curvo-160-hz-qhd-1ms-hdmi-displayport-99-srgb-freesync-premium-hdr-10-vesa-preto-34wp65c-b')

# Esperando a página carregar
time.sleep(5)

# Localizando o elemento span com a classe "header-price"
preco_element = driver.find_element("css selector", "h4.finalPrice")

# Fazendo conversões do valor encontrado
preco_str = preco_element.text
preco_str = preco_str.replace("R$ ", "").replace(".", "").replace(",", ".")
preco = float(preco_str)
print(f"O valor do livro é R$ {preco:.2f}.")

# Verificando se o preço é menor que R$ 90
if preco < 3000:
    print("Aproveitar e comprar")
else:
    print("Não comprar Livro")

# Fechando o driver
driver.quit()