apps:

1. create a user object and emit the signal
2. consumer would receive this signal and ....

1. REST API interface
2. configure slots debezium
3. push whatever is appearing on the slot to kafka
4. we will create a consumer, which is receiving the events and do smth with it


Write to users:
```
curl -X POST http://127.0.0.1:8000/users \                                                   ✔  3.13    06:08:44 PM 
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "Pawel",
    "lastname": "dynow"
  }'
```

Read from the slot:

```
pg_recvlogical \                                                                                                   INT ✘  2m 5s   06:08:59 PM 
  -h 127.0.0.1 -p 5432 -U postgres -d postgres \
  --slot=my_first_slut --start \
  --plugin=wal2json \
  -o pretty-print=0 \
  -o add-tables=public.users \
  --file=-
```