from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Opcional: para guardado de captura
import os

# Configuración del driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://duckduckgo.com/")
    
    buscador = driver.find_element(By.NAME, "q")
    buscador.send_keys("inmuebles en Bogotá")
    buscador.send_keys(Keys.RETURN)

    wait = WebDriverWait(driver, 10)
    resultados = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.result__a"))
    )

    assert len(resultados) > 0, "No se encontraron resultados."

    print("✅ Prueba funcional completada con éxito. Resultados encontrados:", len(resultados))

    # Captura de pantalla
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot("screenshots/test_busqueda_resultado.png")

except Exception as e:
    print("❌ Error durante la prueba:", str(e))
    driver.save_screenshot("screenshots/test_busqueda_error.png")
    raise
finally:
    driver.quit()