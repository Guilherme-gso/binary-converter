from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd

def get_binary_alphabet():
  chromedriver_path='/usr/local/bin/chromedriver'
  url='https://convertbinary.com/alphabet/'

  options = Options()
  options.headless = True

  results = {}

  driver = webdriver.Chrome(chromedriver_path, options=options)
  driver.get(url)

  xpath = '//figure[@class="wp-block-table is-style-stripes"]/table'
  elements = driver.find_elements_by_xpath(xpath)
  
  for idx in range(len(elements)):
    element = elements[idx]
    html = element.get_attribute('outerHTML')
    table = pd.read_html(html)[0]
    table.columns = ['key', 'value']
    results[idx] = table.to_dict('records')

  results = results[0] + results[1]
  driver.quit()

  return results

def ascii_to_binary(ascii_text):
  results = get_binary_alphabet()

  chars = list(ascii_text)
  binary_arr = []

  for idx in range(len(chars)):
    for result in results:
      char = chars[idx]

      if(result['key'] == char):
        binary_value = result['value']
        binary_arr.append(str(binary_value))
  
  binary_text = ' '.join(binary_arr)
  return binary_text

def binary_to_ascii(binary_text):
  results = get_binary_alphabet()
  chars = binary_text.split(' ')
  ascii_arr = []

  for idx in range(len(chars)):
    for result in results:
      char = chars[idx]

      if(str(result['value']) == char):
        binary_value = result['key']
        ascii_arr.append(str(binary_value))
  
  ascii_text = ''.join(ascii_arr)
  return ascii_text

def start():
  choice = input('Choose the type of conversion you want to do: \n [1]: ASCII to Binary | [2]: Binary to ASCII: ')

  print(choice)

  if (choice == '1'):
    ascii_phrase = input('Enter you ASCII phrase: ')
    print(f'Your binary phrase is {ascii_to_binary(ascii_phrase)}')
  
  if(choice == '2'):
    binary_phrase = input('Enter you Binary phrase: ')
    print(f'Your ASCII phrase is {binary_to_ascii(binary_phrase)}')

start()