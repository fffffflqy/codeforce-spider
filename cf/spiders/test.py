# import json
# import time
#
# import sheep as sheep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get("https://codeforces.com")
# with open('cookie2.txt') as f:
#     cookie = f.read()
#     cookie = json.loads(cookie)
#     for i in cookie:
#         driver.add_cookie(i)
# driver.refresh()
# if 'lqy' in driver.page_source:
#     print('ok')
# else :
#     print('no')
# # print(cookie1)
# # with open('cookie1.txt', 'w') as f:
# #     f.write(json.dumps(cookie1))
# # driver.find_element_by_id('handleOrEmail').send_keys('huas_lqy')
# # driver.find_element_by_id('password').send_keys('liuqiyu001')
# # driver.find_element_by_name('password').send_keys(Keys.ENTER)
# # driver.refresh()
# # cookie2 = driver.get_cookies()
# # # with open('cookie2.txt', 'w') as f:
# # #     f.write(json.dumps(cookie2))
# # if cookie1 == cookie2:
# #     print('yes')
# # else :
# #     print('no')
