import undetected_chromedriver
import time

try:
    options = undetected_chromedriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = undetected_chromedriver.Chrome(options)
    driver.get('https://kz.blsspainvisa.com/russian/book_appointment.php')
    time.sleep(5)
    body = driver.find_element('tag name', 'body')
    print(body.text)
    driver.execute_script('document.getElementsByTagName(\'input\')[0].click()')
    driver.execute_script('document.getElementsByTagName(\'select\')[1].value = \'35#56\'')
    driver.execute_script('getAppService(\'35#56\')')
    time.sleep(1)
    driver.execute_script('document.getElementsByTagName(\'select\')[2].value = \'Normal\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[2].value = \'+7\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[3].value = \'7476514287\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[4].value = \'grozergeorge80@gmail.com\'')
    driver.execute_script('document.getElementsByTagName(\'input\')[5].click()')
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()