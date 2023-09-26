from datetime import date, datetime, timedelta
import collections


def get_birthdays_per_week(users) -> dict:
    today = date.today()
    

    if users: 

        birthdays_dict = collections.defaultdict(list)
        seven_days = timedelta(days = 7)
        stop_date = today + seven_days
     
        for i in users:

            this_year_bd = i["birthday"].replace(year=today.year)
            next_year_bd = i["birthday"].replace(year=today.year+1)

            if today <= i["birthday"].replace(year=today.year) < stop_date and this_year_bd.strftime("%A") != "Saturday" and this_year_bd.strftime("%A") != "Sunday":
                birthdays_dict[this_year_bd.strftime("%A")].append(i.get("name"))

            elif today <= this_year_bd < stop_date:
                birthdays_dict[this_year_bd.strftime("Monday")].append(i.get("name"))

            elif today <= next_year_bd < stop_date and next_year_bd.strftime("%A") != "Saturday" and next_year_bd.strftime("%A") != "Sunday":
                birthdays_dict[next_year_bd.strftime("%A")].append(i.get("name"))

            elif today <= next_year_bd < stop_date:
                birthdays_dict[next_year_bd.strftime("Monday")].append(i.get("name"))
            
            else: 
                continue

        return birthdays_dict
    
    else: 
        print("the list is empty")
        return {}


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
