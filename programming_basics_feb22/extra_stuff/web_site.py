import webbrowser as wb

def web_automation():
    chrome_path = '/Applications/Google Chrome.app %s'
    urls = ('apple.com', 'google.com')

    for url in urls:
        print('Opening: ' + url)
        wb.get(chrome_path).open_new_tab(url)

web_automation()