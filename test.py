from snscrape.modules.telegram import TelegramChannelScraper, TelegramPost
scraper = TelegramChannelScraper('klimzhukoff')  # создаем экземпляр класса, твитера, тг, вк,  и т.д, передаем
# назавание канала

result = []


for i, item in enumerate(scraper.get_items()):  # с помощью  get_items получаем все посты с канала (аккаунта)
        result.append(item)
        #print(i, item.content)  # с помощью  content, date получаем все записи из поста\ дату и время
        scr = TelegramPost(url=item.url, date=item.date, outlinks=item.outlinks, outlinksss=item.outlinksss, content=item.content)
        print(scr.content)
        if i == 10:

            break

