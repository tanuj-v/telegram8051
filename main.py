import requests
import pandas as pd
url= "https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv"
df=pd.read_csv(url, sep='\t')
base_url="https://api.telegram.org/bot5447639931:AAGS953aZZydfq94ouqvNdOZyhyneRtrZbU"

def read_msg(offset):
  parameters = {
      "offset": offset
  }
  resp=requests.get(base_url + "/getUpdates", data =parameters)
  data=resp.json()

  print(data)

  for result in data["result"]:
    send_msg(result["message"]["text"])

    if data["result"]:
      return data["result"][-1]["update_id"] + 1

def auto_answer(message):
  answer=df.loc[df['Question'].str.lower()==message.lower()]
  if not answer.empty:
    answer=answer.iloc[0]['Answer']
    return answer


def send_msg(message):
  answer=auto_answer(message)
  parameter={
      "chat_id" : "-1001490247023",
      "text" : answer
  }
  resp=requests.get(base_url + "/sendMessage", data =parameter)
  print(resp.text)

offset=0
while True:
  offset =read_msg(offset)