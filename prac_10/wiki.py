import wikipedia

search_word = input("Search: ")
while search_word != "":
    wikipedia.search(search_word)
    try:
        summary = wikipedia.summary(search_word)
        print("Title: {}".format(search_word.title()))
        print(summary)
        page = wikipedia.page(search_word)
        print("Link: {}".format(page.url))
    except wikipedia.exceptions.DisambiguationError as e:
        print("Did you mean?")
        print(e.options)
    search_word = input("Search: ")