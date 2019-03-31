import requests

#https://statsapi.web.nhl.com/api/v1/teams
#Application Programming Interface = API



class HockeyTeams:

    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
        self.nhl_data = response.json()
        self.team_data = self.nhl_data['teams']

    def get_teams(self):
        idx = 0
        while idx < len(self.team_data):
            current_team = self.team_data[idx]
            idx += 1
            print(current_team['locationName'] + " " + current_team['teamName'])

    def list_info(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
        listtest = response.json()
        for keys in listtest.keys():
            print(listtest.keys())
            if isinstance(listtest[keys], list):
                for idx in range(len(listtest[keys])):
                    new_list = listtest[keys]
                    # print(new_list[idx])
                    if isinstance(new_list[idx], dict):
                        # print(new_list[idx].keys())
                        print(((new_list[idx].keys())))

            elif isinstance(listtest[keys], dict):
                print(listtest[keys].keys())



team_list = HockeyTeams()
#team_list.list_info()
