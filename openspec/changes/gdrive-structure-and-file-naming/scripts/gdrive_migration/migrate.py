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
TREE = '''00-📥-Inbox/AI-Exports
00-📥-Inbox/Skany-i-Mobilne
00-📥-Inbox/Do-Przejrzenia
00-🔒-Poufne-Dokumenty/Tozsamosc
00-🔒-Poufne-Dokumenty/Majatek-Akty-Notarialne
01-👨‍👩‍👧‍👦-Rodzina/01-Wazne-Dokumenty
01-👨‍👩‍👧‍👦-Rodzina/02-Natalka
01-👨‍👩‍👧‍👦-Rodzina/03-Nadia
01-👨‍👩‍👧‍👦-Rodzina/04-Michal
01-👨‍👩‍👧‍👦-Rodzina/05-Genealogia
02-🏫-Edukacja-Dzieci/Michal
02-🏫-Edukacja-Dzieci/Nadia
03-🏥-Zdrowie/Pawel
03-🏥-Zdrowie/Natka
03-🏥-Zdrowie/Dzieci
03-🏥-Zdrowie/Rodzice
03-🏥-Zdrowie/Archiwum-Medyczne
04-📄-Dokumenty-Osobiste/Dziennik
04-📄-Dokumenty-Osobiste/Kariera-i-CV
04-📄-Dokumenty-Osobiste/Certyfikaty-i-Szkolenia
05-💰-Finanse/01-Budzet-i-Analizy
05-💰-Finanse/02-Podatki-PIT
05-💰-Finanse/03-Banki-i-Kredyty
05-💰-Finanse/04-Inwestycje-i-Emerytura
05-💰-Finanse/05-Paragony-i-Gwarancje
07-🏢-Praca-i-Projekty/2026-Biezace
07-🏢-Praca-i-Projekty/Projekty-Historyczne
07-🏢-Praca-i-Projekty/Publikacje-i-Wystapienia
07-🏢-Praca-i-Projekty/Warsztaty-i-Materialy-Szkoleniowe
10-🏠-Mieszkanie-i-Nieruchomosci/01-Pod-Strzecha-7
10-🏠-Mieszkanie-i-Nieruchomosci/02-Remonty-i-Wyposazenie
10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia
10-🏠-Mieszkanie-i-Nieruchomosci/04-Infrastruktura-Domowa-i-Siec
11-🏡-Lewickie/Eksploatacja-i-Oplaty
11-🏡-Lewickie/Geodezja-i-Dokumentacja
12-🚗-Pojazdy/Toyota-Corolla
12-🚗-Pojazdy/Samochod-Drugi
20-📚-Wiedza-i-Rozwoj/01-Inzynieria-Danych-i-AI
20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka
20-📚-Wiedza-i-Rozwoj/03-Ebooki-i-Publikacje
21-🎵-Audio-i-Multimedia
22-🏃-Sport-i-Aktywnosc
23-🎮-Gry-i-Hobby
24-🏖️-Podroze-i-Wyjazdy/2025
24-🏖️-Podroze-i-Wyjazdy/2026
80-📱-Aplikacje-i-Synchronizacja/80-Notability-Backup
80-📱-Aplikacje-i-Synchronizacja/81-Obsidian-Sync
90-🗄️-Archiwum/Archiwum-Dzialalnosci-Gospodarczej
90-🗄️-Archiwum/Archiwum-Studiow
90-🗄️-Archiwum/Stare-Projekty
99-🗑️-Do-Usuniecia'''.splitlines()
# These are safe direct moves only; no renaming, deleting, or encryption claims.
ROOT_FILE_DEST = {
 'Dziennik.gdoc':'04-📄-Dokumenty-Osobiste/Dziennik',
 'IMG_2312.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2313.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2314.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2315.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2316.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2317.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2318.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2319.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2320.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2321.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2322.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'IMG_2323.jpeg':'00-📥-Inbox/Skany-i-Mobilne',
 'home_budget_categorized_2026-06-21.csv':'05-💰-Finanse/01-Budzet-i-Analizy',
 'wprowadzenie-do-calek.docx':'20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka',
 'wprowadzenie-do-calek.gdoc':'20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka',
 'OWU Warta Travel - C0517.pdf':'24-🏖️-Podroze-i-Wyjazdy/2026',
 'Bilet - WH64222365.pdf':'24-🏖️-Podroze-i-Wyjazdy/2026',
}

def norm(s):
 return unicodedata.normalize('NFC', s)

def auth():
 token = BASE/'token.json'
 creds = Credentials.from_authorized_user_file(str(token), SCOPES) if token.exists() else None
 if creds and creds.expired and creds.refresh_token:
  creds.refresh(Request())
 if not creds or not creds.valid:
  creds = InstalledAppFlow.from_client_secrets_file(str(BASE/'credentials.json'), SCOPES).run_local_server(port=0)
 token.write_text(creds.to_json())
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

def legacy_make_plan(files,root_id):
 roots=root_map(files,root_id); operations=[]; blocked=[]
 existing_names=set(roots)
 for src,dst in ROOT_RENAMES.items():
  hits=roots.get(norm(src),[])
  if len(hits)==1 and dst not in existing_names:
   operations.append(dict(kind='rename',id=hits[0]['id'],source=src,target=dst))
   existing_names.add(dst)
  elif len(hits)>1 or (hits and dst in existing_names): blocked.append(dict(source=src,reason='ambiguous or destination exists'))
 for path in TREE:
  operations.append(dict(kind='ensure_folder',path=path))
 for name,dst in ROOT_FILE_DEST.items():
  hits=[f for f in roots.get(norm(name),[]) if f['mimeType']!=FOLDER]
  if len(hits)==1: operations.append(dict(kind='move_root_file',id=hits[0]['id'],name=name,target=dst))
  elif len(hits)>1: blocked.append(dict(source=name,reason='duplicate root filename'))
 for name,items in roots.items():
  if name in ('Takeout','95-💽-Takeout','91🔑Hasła') or name not in ROOT_RENAMES and name not in ROOT_FILE_DEST:
   blocked.append(dict(source=name,reason='manual mapping required; untouched',ids=[f['id'] for f in items]))
 blocked.append(dict(source='complex subfolder merges, sensitive IDs, archive purge',reason='manual review required; intentionally not automated'))
 return dict(operations=operations,blocked=blocked,inventory_count=len(files))

def child(api,parent,name):
 q="'%s' in parents and mimeType = '%s' and trashed = false"%(parent,FOLDER)
 matches=[f for f in scan_children(api,q) if norm(f['name'])==norm(name)]
 if len(matches)>1: raise RuntimeError('Ambiguous folder '+name)
 return matches[0]['id'] if matches else None

def scan_children(api,q):
 out=[]; token=None
 while True:
  r=call(api.files().list(q=q,fields='nextPageToken,files(id,name,mimeType,parents)',pageSize=1000,pageToken=token))
  out+=r.get('files',[]);token=r.get('nextPageToken')
  if not token:return out

def ensure(api,path):
 parent='root'
 for name in path.split('/'):
  found=child(api,parent,name)
  if not found:
   found=call(api.files().create(body={'name':name,'mimeType':FOLDER,'parents':[parent]},fields='id'))['id']
  parent=found
 return parent

def apply(api,plan):
 raise RuntimeError('Legacy executor disabled; schema v2 requires reviewed execution tooling')
 log=[]
 # Rename only if original is still in root and destination is not present.
 for op in plan['operations']:
  try:
   if op['kind']=='rename':
    f=call(api.files().get(fileId=op['id'],fields='id,name,parents,mimeType'))
    if f['name']==op['target']: status='already_done'
    elif norm(f['name'])!=norm(op['source']) or 'root' not in f.get('parents',[]): status='skipped_changed'
    elif child(api,'root',op['target']): status='skipped_collision'
    else:
     call(api.files().update(fileId=op['id'],body={'name':op['target']},fields='id'));status='done'
   elif op['kind']=='ensure_folder':
    ensure(api,op['path']);status='done'
   elif op['kind']=='move_root_file':
    f=call(api.files().get(fileId=op['id'],fields='id,name,parents'))
    dest=ensure(api,op['target'])
    if dest in f.get('parents',[]): status='already_done'
    elif norm(f['name'])!=norm(op['name']) or 'root' not in f.get('parents',[]): status='skipped_changed'
    else:
     siblings=scan_children(api,"'%s' in parents and trashed = false"%dest)
     if any(norm(x['name'])==norm(f['name']) for x in siblings):status='skipped_collision'
     else:
      call(api.files().update(fileId=op['id'],addParents=dest,removeParents='root',fields='id,parents'));status='done'
   else:status='skipped_unknown'
   log.append(dict(operation=op,status=status))
  except Exception as exc:
   log.append(dict(operation=op,status='error',error=str(exc)))
  save('migration_log.json',log)
 return log

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
 elif args.command=='apply':
  plan=json.loads((BASE/'plan.json').read_text(encoding='utf-8'))
  log=apply(api,plan);print('Finished:',len(log),'errors:',sum(x['status']=='error' for x in log))
 else:
  files=scan(api); roots=root_map(files,root_id)
  result={'root_files':[{'name':f['name'],'id':f['id']} for v in roots.values() for f in v if f['mimeType']!=FOLDER],
          'root_folders':sorted(roots),'count':len(files)}
  save('verification.json',result);print('Root loose files:',len(result['root_files']))
if __name__=='__main__':main()
