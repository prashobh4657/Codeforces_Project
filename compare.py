def compare(comparator):
    import easygui
    import requests
    import json
    import matplotlib.pyplot as plt
    import pandas as pd
    from csv import writer

    compare_with = easygui.enterbox("Enter the username with whom you want to compare the Rating Graph..","Codeforces Analysis")
    response = requests.get('https://codeforces.com/api/user.info?handles='+compare_with)
    response_text = response.text
    if(response_text == ""):
        easygui.msgbox("User Not Found!","Codeforces Analysis")
    else:
        all_contests_given_by_comparator = requests.get('https://codeforces.com/api/user.rating?handle='+comparator)
        json_all_contests_given_by_comparator = json.loads(all_contests_given_by_comparator.text)

        all_contests_given_by_p_two = requests.get('https://codeforces.com/api/user.rating?handle='+compare_with)
        json_all_contests_given_by_p_two = json.loads(all_contests_given_by_p_two.text)

        total_contests_given = max(len(json_all_contests_given_by_comparator['result']),len(json_all_contests_given_by_p_two['result']))
        cnt = 0
        csv_f = open("cf_data.csv",'w')
        writer_object=writer(csv_f,lineterminator='\n')
        writer_object.writerow(["Rating of 1","Rating of 2"])
        writer_object.writerow([json_all_contests_given_by_comparator['result'][0]['oldRating'],json_all_contests_given_by_p_two['result'][0]['oldRating']])
        cnt = cnt + 1

        for i in range(cnt,total_contests_given+1):
            try:
                writer_object.writerow([json_all_contests_given_by_comparator['result'][i-1]['newRating'],json_all_contests_given_by_p_two['result'][i-1]['newRating']])
            except:
                try:
                    writer_object.writerow(["",json_all_contests_given_by_p_two['result'][i-1]['newRating']])
                except:
                    writer_object.writerow([json_all_contests_given_by_comparator['result'][i-1]['newRating'],""])
        csv_f.close()

        df = pd.read_csv('cf_data.csv')
        df.plot()
        plt.title("Rating Comparison")
        L=plt.legend()
        L.get_texts()[0].set_text(comparator)
        L.get_texts()[1].set_text(compare_with)
        plt.show()

        all_contests_given = requests.get('https://codeforces.com/api/user.rating?handle='+comparator)
        json_all_contests_given = json.loads(all_contests_given.text)

        total_contests_given = len(json_all_contests_given['result'])
        cnt = 0
        csv_f = open("cf_data.csv",'w')
        writer_object=writer(csv_f,lineterminator='\n')
        writer_object.writerow(["Rating"])
        writer_object.writerow([json_all_contests_given['result'][0]['oldRating']])
        cnt = cnt + 1

        for i in range(cnt,total_contests_given+1):
            writer_object.writerow([json_all_contests_given['result'][i-1]['newRating']])
        
        csv_f.close()