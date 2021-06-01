from selenium import webdriver
from log_info import username, password
import time

browser = webdriver.Firefox()

url="https://www.instagram.com/"
browser.get(url)
time.sleep(2)
user = input("Search User: ")

name = browser.find_element_by_name("username")
passw = browser.find_element_by_name("password")
log_btn = browser.find_element_by_css_selector(".L3NKy")

name.send_keys(username)
passw.send_keys(password)
log_btn.click()
time.sleep(4)

not_now = browser.find_element_by_css_selector(".cmbtv")
not_now.click()
time.sleep(2)
not_now2 = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
not_now2.click()
time.sleep(2)

src_btn = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
src_btn.send_keys(user)
time.sleep(2)

datas = browser.find_elements_by_css_selector(".jSC57  ._6xe7A")
personas = datas[0]
personas.click()
time.sleep(5)

infos = browser.find_element_by_css_selector("li.Y8-fY:nth-child(2)")
infos.click()
time.sleep(2)

jscommand = """
users = document.querySelector(".isgrP");
users.scrollTo(0, users.scrollHeight);
var lenOfPage=users.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

users = browser.find_elements_by_css_selector(".PZuss > li > div:nth-child(1) > div:nth-child(2)")

followerNo = 1
for user in users:
    with open("followers.txt","a", encoding="utf-8") as file:
        file.write(str(followerNo) + "\n*****************\n" + user.text + "\n*****************\n")
        followerNo += 1

browser.close()

