import json

'''
[{
    title:"title",
    link : "link", 
    contents: "contents",
    datetime: "date"
},...]
'''

years = [2016, 2017, 2018, 2019, 2020, 2021]
days_28 = [2]
days_31 = [1,3,5,7,8,10,12]

def ret_days(year, month):
    
    if month in days_31:
        return 31
    elif month in days_28:
        if (year%4 == 0):
            return 29
        else:
            return 28
    else:
        return 30

def load_jsons(year, month):
    #file name format : "year-month-1_year-month-enddaysnews.json"
    file_name = "{0}-{1}-1_{0}-{1}-{2}news.json".format(year, month, ret_days(year, month))
    path = './scraper/'+file_name
    with open(path, 'r') as file:
        json_data = json.load(file)
    for arts in json_data:
        arts['content'] = arts['content'].replace("\n"," ")
    return json_data

if __name__ == "__main__":
    merge_dict_list = []
    for year in years:
        if (year == 2016):
            for month in range(3,13):
                json_data = load_jsons(year, month)
                for data in json_data:
                    merge_dict_list.append(data)
                #print(json_data)
        elif (year == 2021):
            for month in range(1,3):
                json_data = load_jsons(year, month)
                for data in json_data:
                    merge_dict_list.append(data)
        else:
            for month in range(1,13):
                json_data = load_jsons(year, month)
                for data in json_data:
                    merge_dict_list.append(data)
    merge_dict_list = sorted(merge_dict_list, key= lambda k: k['date'], reverse = False)
    with open('merged_data.json', 'w') as merge_file:
        json.dump(merge_dict_list, merge_file, indent=4)