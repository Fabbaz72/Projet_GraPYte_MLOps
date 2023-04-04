{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue254;\red0\green0\blue0;
\red15\green112\blue1;\red0\green0\blue255;\red101\green76\blue29;\red144\green1\blue18;\red18\green112\blue68;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c63922\c8235\c8235;\cssrgb\c3529\c50588\c33725;
\cssrgb\c14510\c46275\c57647;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  fastapi.testclient \cf2 \strokec2 import\cf0 \strokec4  TestClient\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  .main \cf2 \strokec2 import\cf0 \strokec4  app, users\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 client = TestClient(app)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Test d'authentification invalide\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 test_invalid_authentication\cf0 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     input_data = \{\cb1 \
\cb3         \cf5 \strokec5 # Ajoutez ici les valeurs d'entr\'e9e pour les tests\cf0 \cb1 \strokec4 \
\cb3     \}\cb1 \
\
\cb3     response = client.post(\cb1 \
\cb3         \cf8 \strokec8 "/predict"\cf0 \strokec4 ,\cb1 \
\cb3         json=input_data,\cb1 \
\cb3         auth=(\cf8 \strokec8 "wrong_username"\cf0 \strokec4 , \cf8 \strokec8 "wrong_password"\cf0 \strokec4 ),\cb1 \
\cb3     )\cb1 \
\
\cb3     \cf2 \strokec2 assert\cf0 \strokec4  response.status_code == \cf9 \strokec9 401\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 assert\cf0 \strokec4  response.json() == \{\cf8 \strokec8 "detail"\cf0 \strokec4 : \cf8 \strokec8 "Authentification invalide"\cf0 \strokec4 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Test d'authentification valide et pr\'e9diction\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 test_valid_authentication_and_prediction\cf0 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     input_data = \{\cb1 \
\cb3         \cf5 \strokec5 # Ajoutez ici les valeurs d'entr\'e9e pour les tests\cf0 \cb1 \strokec4 \
\cb3     \}\cb1 \
\
\cb3     valid_user = \cf10 \strokec10 list\cf0 \strokec4 (users.keys())[\cf9 \strokec9 0\cf0 \strokec4 ]\cb1 \
\cb3     valid_password = users[valid_user]\cb1 \
\
\cb3     response = client.post(\cb1 \
\cb3         \cf8 \strokec8 "/predict"\cf0 \strokec4 ,\cb1 \
\cb3         json=input_data,\cb1 \
\cb3         auth=(valid_user, valid_password),\cb1 \
\cb3     )\cb1 \
\
\cb3     \cf2 \strokec2 assert\cf0 \strokec4  response.status_code == \cf9 \strokec9 200\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 assert\cf0 \strokec4  \cf8 \strokec8 "output"\cf0 \strokec4  \cf6 \strokec6 in\cf0 \strokec4  response.json()}