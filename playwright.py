from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://www.google.com')
    
    input("")
