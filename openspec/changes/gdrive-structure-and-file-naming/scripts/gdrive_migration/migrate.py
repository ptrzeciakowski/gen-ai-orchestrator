#!/usr/bin/env python3
"""Conservative Google Drive structure migration, using Google Drive API v3."""
import argparse
import json
import os
import time
import unicodedata
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import planner

BASE = Path(__file__).resolve().parent
# OAuth (credentials.json, token.json) trzymamy poza repozytorium.
CONFIG = Path(os.environ.get('GDRIVE_MIGRATION_CONFIG', Path.home()/'.config'/'gdrive-migration'))
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
FOLDER = 'application/vnd.google-apps.folder'
ROOT_RENAMES = {
 '01👨‍👩‍👧‍👦 Rodzina':'01-👨‍👩‍👧‍👦-Rodzina', '02🏫Szkoła':'02-🏫-Edukacja-Dzieci',
 '03🏥Zdrowie':'03-🏥-Zdrowie','05💰Finanse':'05-💰-Finanse',
 '07🏢Praca':'07-🏢-Praca-i-Projekty','15🏡Lewickie':'11-🏡-Lewickie',
 '96🗄️Archiwum':'90-🗄️-Archiwum','08🏖️Wakacje':'24-🏖️-Podroze-i-Wyjazdy',
 '85🏃 Bieganie':'22-🏃-Sport-i-Aktywnosc','92🎵 Muzyka':'21-🎵-Audio-i-Multimedia',
 '93🎮Gry':'23-🎮-Gry-i-Hobby', '06🏠Mieszkanie':'10-🏠-Mieszkanie-i-Nieruchomosci',
 '09🚗Samochód':'12-🚗-Pojazdy',
}

def norm(s):
 return unicodedata.normalize('NFC', s)

def auth():
 token = CONFIG/'token.json'
 creds = Credentials.from_authorized_user_file(str(token), SCOPES) if token.exists() else None
 if creds and creds.expired and creds.refresh_token:
  creds.refresh(Request())
 if not creds or not creds.valid:
  creds = InstalledAppFlow.from_client_secrets_file(str(CONFIG/'credentials.json'), SCOPES).run_local_server(port=0)
 CONFIG.mkdir(parents=True,exist_ok=True,mode=0o700)
 token.write_text(creds.to_json()); token.chmod(0o600)
 return build('drive','v3',credentials=creds,cache_discovery=False)

def call(request):
 for i in range(6):
  try: return request.execute()
  except HttpError as e:
   if e.resp.status not in (429,500,502,503,504) or i==5: raise
   time.sleep(min(2**i,32))

def scan(api):
 files=[]; token=None
 while True:
  resp=call(api.files().list(q='trashed = false',spaces='drive',fields='nextPageToken,files(id,name,mimeType,parents,driveId)',pageSize=1000,pageToken=token))
  files.extend(resp.get('files',[])); token=resp.get('nextPageToken')
  if not token: break
 root_id=call(api.files().get(fileId='root',fields='id'))['id']
 return planner.my_drive(files,root_id)

def save(name,obj):
 (BASE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def root_map(files,root_id):
 roots={}
 for f in files:
   if root_id in f.get('parents',[]): roots.setdefault(norm(f['name']),[]).append(f)
 return roots

def apply(api,plan):
 raise RuntimeError('Legacy executor disabled; schema v2 requires reviewed execution tooling')

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('command',choices=['plan','apply','verify'])
 parser.add_argument('--approve',default='')
 args=parser.parse_args()
 if args.command=='apply':parser.error('apply disabled: schema v2 needs reviewed execution, verification and recovery tooling')
 api=auth()
 root_id=call(api.files().get(fileId='root',fields='id'))['id']
 if args.command=='plan':
  files=scan(api);save('inventory.json',files);plan=planner.make_plan(files,root_id,ROOT_RENAMES);save('plan.json',plan)
  (BASE/'dry_run_report.md').write_text(planner.summary(plan),encoding='utf-8')
  print('Plan operations:',len(plan['operations']),'blocked:',len(plan['blocked']))
 else:
  files=scan(api); roots=root_map(files,root_id)
  result={'root_files':[{'name':f['name'],'id':f['id']} for v in roots.values() for f in v if f['mimeType']!=FOLDER],
          'root_folders':sorted(roots),'count':len(files)}
  save('verification.json',result);print('Root loose files:',len(result['root_files']))
if __name__=='__main__':main()
