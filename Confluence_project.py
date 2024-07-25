from atlassian import Confluence
import pandas as pd


#Создание страницы
def creating_page(space, title, body, parent_id=None):
    status = confluence.create_page(space=space, title=title, body=body)
    return status


#Удаление страницы
def deleting_page(page_id):
    confluence.remove_page(page_id, status=None, recursive=False)


#Редактирование страницы
def updating_page(page_id, page_title, page_body):
    confluence.update_page(page_id, page_title, page_body)


#Создаем датафрейм, содержащий в себе все space (названия и ключи)
def making_spaces_df():
    spaces_list = confluence.get_all_spaces()['results']
    space_names = []
    space_keys = []
    for obj in spaces_list:
        space_names.append(obj['name'])
        space_keys.append(obj['key'])
    space_df = pd.DataFrame(list(zip(space_names, space_keys)), columns=['name', 'key'])
    return space_df


#Создаем датафрейм, содержащий в себе все страницы, принадлежащие выбранному space (содержит название и id)
def making_pages_df(space_key):
    pages = confluence.get_all_pages_from_space(space_df['key'].iloc[space_key], 0, 100, content_type='page')
    pages_ids = []
    pages_titles = []
    for obj in pages:
        pages_titles.append(obj['title'])
        pages_ids.append(obj['id'])
    pages_df = pd.DataFrame(zip(pages_titles, pages_ids), columns=['title','id'])
    return pages_df


#Реализация case-switch механизма и самого процесса
def switch(request):
    print(space_df)
    space_number = int(input('Выберите space, в который хотите вносить изменения = '))
    pages_df = making_pages_df(space_number)
    if request == 1:
        body = data.to_html() # преобразовываем body в html
        title = 'Test title number 6' #задаем заголовок
        creating_page(space_df['key'].iloc[space_number], title, body)
        print('Страница успешно создана!')
    elif request == 2 or request == 3:
        print(pages_df)
        page_number = int(input('Выберите номер страницы, с которой хотите работать = '))
        page_id = pages_df['id'].iloc[page_number] #достаем page_id
        if request == 2:
            page_title = 'pepega New Edited title' #изменение заголовка страницы
            page_body = '<p>Not Real Slim Shady</p>' #изменение "тела" страницы
            updating_page(page_id, page_title, page_body) #вызов функции изменения
            print('Страница успешно отредактирована!')
        elif request == 3:
            deleting_page(page_id) #удаление страницы
            print('Страница успешно удалена!')


confluence = Confluence(
    url='https://YOUR_NAME.atlassian.net/',
    username='YOUR_USERNAME',
    password='YOUR_API_TOKEN')

data = pd.read_excel('data.xlsx')  #читаем excel-таблицу в датафрейм

space_df = making_spaces_df()  #создаем датафрейм space'ов

print('Выберите пункт меню:\n 1. Создать страницу\n 2. Редактировать страницу\n 3. Удалить страницу\n -1. Выход')
choice = int(input())
while choice != -1:
    switch(choice)
    print('Выберите пункт меню:\n 1. Создать страницу\n 2. Редактировать страницу\n 3. Удалить страницу\n -1. Выход')
    choice = int(input())
