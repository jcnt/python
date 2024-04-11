import data_manager
import flight_search
import notification_manager

sheet = data_manager.DataManager()
sheet_data = sheet.get_reqs()['prices']

search = flight_search.FlightSearch()

for i in sheet_data: 
    if i['iataCode'] == "": 
        print(i['city'], i['id'])
        iata = search.get_iata(i['city'])
        print(iata)
        sheet.update_iata(iata, i['id'])

for i in sheet_data:
    hit = search.flight_search(i['iataCode'], i['maxstop'])
    if hit[4] < i["lowestPrice"]:
        leave = hit[5].split("T")[0]
        back = hit[6].split("T")[0]
        message = notification_manager.NotificationManager()
        message.sendtext(f"Deal!! {hit[0]} -> {hit[2]}: {hit[4]} EUR. {leave} -> {back}")

