import requests
from bs4 import BeautifulSoup
from time import sleep, process_time

headers = {"User-Agent": "test"}
BASE_URL = "https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-"

extra = ["https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-244-side-story-1-i-am-an-employee-of-the-hunters-association/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-245-side-story-2-reunion-1/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-246-side-story-3-reunion-2/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-247-side-story-4-return/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-248-side-story-5-igrits-memories/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-249-side-story-6-your-daily-routine-1/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-250-side-story-7-your-daily-routine-2/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-251-side-story-8-your-daily-routine-3/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-252-side-story-9-your-daily-routine-4/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-253-side-story-10-your-daily-routine-5/",
"https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-254-side-story-11-your-daily-routine-6/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-255-side-story-12-decision/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-256-side-story-13-a-day-in-fangs-life/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-257-side-story-14-only-im-max-level/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-258-side-story-15-im-going-there-to-meet-you-right-now-1/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-259-side-story-16-im-going-there-to-meet-you-right-now-2/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-260-side-story-17-im-going-there-to-meet-you-right-now-3/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-261-side-story-18/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-262-side-story-19-twelve-years-later-1/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-263-side-story-20-twelve-years-later-2/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-264-side-story-21-twelve-years-later-fin/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-265-after-story-part-1-berus-memories/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-266-after-story-part-2-until-we-meet-again/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-267-after-stories-part-3-approach/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-268-after-stories-part-4-forward-forward/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-269-after-stories-part-5-conclusion/","https://wuxialib.net/novel/solo-leveling-i-alone-level-up/chapter-270-after-stories-part-6-goodbye/"]

for ch in range(5,21):
    CHAPTER_URL = BASE_URL + str(ch) +"/"
    response = requests.get(CHAPTER_URL, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    grafs = soup.find('div', class_="reading-content").find_all('p')
    chapter = ""
    for p in grafs: 
        chapter = chapter + p.text + "\n"
    
    filename = "chapters/chapter-"+str(ch)+".txt"
    f= open(filename,"w+")
    f.write(chapter)
    f.close()
    sleep(0.5)

# for ch in extra:
#     CHAPTER_URL = ch
#     response = requests.get(CHAPTER_URL, headers=headers)
#     soup = BeautifulSoup(response.text, "lxml")
#     grafs = soup.find('div', class_="reading-content").find_all('p')
#     chapter = ""
#     for p in grafs: 
#         chapter = chapter + p.text + "\n"

#     filename = "chapters/chapter-extra-"+str(extra.index(ch))+".txt"
#     f= open(filename,"w+")
#     f.write(chapter)
#     f.close()
#     sleep(0.5)