def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return Flase
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True
article_chain = 

while continue_crawl(article_chain, target_url):
    first_link = find_first_link(url)
    article_chain.append(first_link)
    time.sleep(2)

        return False
    else:
        return True

start_url = "https://en.wikipedia.org/wiki/Persona_5"
target_url = "https://en.wikipedia.org/wiki/Timekeeping_in_games#Turn-based"
article_chain = [start_url]

while continue_crawl(article_chain, target_url)


