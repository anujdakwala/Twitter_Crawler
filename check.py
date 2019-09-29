import requests
import pandas as pd
import lxml.html as html
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as BS
import re

train  = pd.read_excel('C:\\Users\\Anuj\\Desktop\\GetOldTweets-python-master\\ThreeUK0207.xlsx')


venue_list=["switch",
"threeuk",
"albertsons stadium",
"alfond arena",
"alumni baseball diamond",
"alumni hall",
"alumni turf",
"amanda littlejohn stadium"
]

      

venues = []                
if any(ven in train.tweet.lower() for ven in venue_list):
	if ("/" in city):
		venue=city.strip().split("/")[1].strip()
		print(venue)
		city=city.strip().split("/")[0].strip()
		print(city)
	else:
		venue=city.strip()
		print(venue)
		city=""
cities.append(city)
venues.append(venue)
        except:
            pass
    
        

        # for Event Home-Away-Neutral and Tournament
        soup = BS(reqvar.text,'lxml')
        divs = soup.find('div', {'class': 'schedule-content clearfix'})
        types=[]
        tournaments=[]
        EventNameTime1=[]
        EventNamelist=[]
        opponent_link=[]
        EventNameAtVS=[]
        venues=[]
        cities=[]
        
        try:
            div_list = divs.find_all('div', {'class': 'event-row'})
            for div in div_list:            
                infos = div.find('div', {'class': 'event clearfix'}).find_all('div')
                EventNameTime1.append(str(infos[0].text.strip()))
                EventNamelist.append(str(infos[2].text.replace("\n","")))
                #print(EventNamelist[-1])
                if("%" in EventNamelist[-1]):
                    EventNamelist[-1] = EventNamelist[-1].strip("%")
                    tournaments.append("Tournament")
                else:
                    tournaments.append("")      
                try:
                    venue = ""
                    city = str(infos[3].text.replace("\n",""))
                    if("|" in city):
                        city=city[:(city.find("|"))-1]
                    if any(ven in city.lower() for ven in venue_list):
                        if ("/" in city):
                            venue=city.strip().split("/")[1].strip()
                            city=city.strip().split("/")[0].strip()
                        else:
                            venue=city.strip()
                            city=""
                    elif any(word in city.upper() for word in stop_words):
                        city=""
                    elif("STADIUM" in city.upper() or "PARK" in city.upper() or "FIELD" in city.upper()):
                        if("-" in city):
                            city,venue=city.split("-",1)
                        else:
                            city,venue="",city
                    elif ("HAMILTON GYMNASIUM" in city.upper()):
                        city=city[:city.upper().find("(HAMILTON GYMNASIUM)")]
                        venue="hamilton gymnasium"
                    elif ("QUICKEN LOANS ARENA" in city.upper()):
                        city=city[:city.upper().find("(QUICKEN LOANS ARENA)")]
                        venue="quicken loans arena"
                    elif("BREAK CHALLENGE" in city.upper()):
                        city=city[:city.upper().find("BREAK CHALLENGE")]
                    elif("- FIRST ROUND" in city.upper()):
                        city=city[:city.upper().find("- FIRST ROUND")]
                    elif("-" in city):
                        city,venue=city.split("-",1)
                    cities.append(city)
                    venues.append(venue)
                except:
                    cities.append("")
                    venues.append("")
                types.append(div.find_all('a', {'class': 'venue'})[0]['title'].strip())
                EventNameAtVS.append(str(div.find_all('div', {'class': 'va'})[0].getText().strip()))
                opponent_link.append("")
            formatTime(EventNameTime1)
        except Exception as e:
            print(e,"============================== ")
            pass
    else:
        print("Completed")
        continue
    finallist = []
    for i in range(0,EventNamelist.__len__()):
        tupp = []
        tupp.append(url)                            #URL
        tupp.append(EventNamelist[i])               #Event name
        tupp.append(EventNameAtVS[i])               #VS/at
        tupp.append(EventNameStartDate[i])          #Start date
        tupp.append(EventNameEndDate[i])            #End date
        tupp.append(EventNameTime1[i])              #Time
        tupp.append(cities[i].capitalize())         #City
        tupp.append(venues[i])                      #Venue
        tupp.append(opponent_link[i])               #Opponenet Link
        tupp.append(types[i])                       #Home-Away-Neutral
        tupp.append(tournaments[i])                 #Tournaments
        finallist.append(tupp)

    df2 = pd.DataFrame(finallist , columns=["URL", "EventName","VS/at","Start Date","End Date","Time","City","Venue","Opponent Link","Home-Away-Neutral","Tournament"])
    df=df.append(df2)
    print("Completed")
    ii=ii+1
    break
df.to_csv('25feb_init_file_10College_updated_new_2.csv', index=False, sep='\t', encoding = 'utf-8')
