import requests
import json
import re

############################### CONFIG:
owner = 'NCATSTranslator' # Replace with the repository owner's name or organization name
repo = 'Feedback'   # Replace with the repository name
asset_headers = ['Relationship','Settings','InputName','InputID','OutputName','OutputID','Expected Result','Author','issue label']

############################### UTILS:
def parse_entry(text,H):
  dat = {}
  for entries in text:
    entries = entries.lstrip()
    for h in H:
      if h in entries:
        dat[h] = re.split(h+":", entries, 1)[1].lstrip()
  return dat

def parse_body(text,H):
  testing_framework = text.split("## Testing framework:",1)
  if len(testing_framework)>1:
    templated_text_entries = testing_framework[1].splitlines()
    data_dict = parse_entry(templated_text_entries,H)
  else:
    data_dict = {}
  return data_dict

############################### SCRIPT: For the moment, does not take into account multiple templates in 1 issue, in case of multiplicity, the syntax needs to be worked out first
if __name__ == '__main__':
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    data = []
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from GitHub API. Status code: {response.status_code}")
        print(response.text)
        templated_issues = []
    else:
        issue_list = response.json()
        issue = issue_list[0]
        templated_issues = []
        for issue in issue_list:
            body = issue['body']
            asset = parse_body(body,asset_headers)
            if len(asset)>0:
                # pk = parse_entry(body.splitlines(),['PK'])
                UI_url = parse_entry(body.splitlines(),['URL'])
                # ars_response = requests.get("http://ars.ci.transltr.io/ars/api/messages/" + pk['PK']).json()
                # ars_response['fields']['data']['message']['query_graph']['nodes']['ids']
                asset['InputID'] = UI_url['URL'].split(r"results?l=")[1].split("&")[1][2:]
                asset['InputName'] = UI_url['URL'].split(r"results?l=")[1].split("&")[0].replace("%20"," ")
                asset['labels'] = [l['name'] for l in issue['labels']]
                # asset['Relationship'] need to use ars message for that, currently does not work
                # asset['Settings'] do we really need this?
                templated_issues.append(asset)
        
    print(templated_issues)




