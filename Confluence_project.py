from atlassian import Confluence

confluence = Confluence(
    url='url here',
    username='username here',
    password='API Token here')

page_id = 'page_id here'
content = confluence.get_page_by_id(page_id=page_id, expand = 'body.storage')

space = confluence.get_page_space(page_id)
page_title = content['title']
page_content = '<p>Not real slim shady</p>'

#Обновление страницы
status = confluence.update_page(page_id, page_title, page_content)

#Удаление страницы
#status = remove_page(page_id, status=None, recursive=False)

#Создание страницы
#status = confluence.create_page(
#    space=space,
#    title='This is the title',
#    body='This is the body!')

print(status)