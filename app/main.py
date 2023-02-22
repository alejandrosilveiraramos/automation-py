from fastapi import FastAPI
from selenium import webdriver


from controller import  moveMouse, pageManipulation


app = FastAPI()



@app.get('/')
def index():
    return{'Working'}


@app.get('/mouse-position')
def mousePosition():
    
    position = moveMouse.mouseLocation()
    
    return position


@app.get('/auto-login')
def autoLogin():
    
    driver = webdriver.Chrome()
    
    pageManipulation.fill_login_form(driver)
    
    pageManipulation.create_repository(driver)
    
   
    return { 'Got it'}

