# im
Pantry inventory management

# Inventory management system written in django - python
The object of this django app is to keep track of which goods you own, when they will expire, when you should consume them and when you shoud buy more.

## features
- Enter items in your pantry (or other locations, with their location) with their expiry date
- Items can have a minimum quantity you always want to keep in the pantry
 - a shopping list is automatically populated with items whose quantity is below this minimum quantity
  - you can add one off items to this shopping list that are not tracked in the inventory.
- You get an overview of items per expiry date so you know what to consume first (or throw away)

- Extensive search and filtering and grouping on locations, categories, units, expiry date using the auto generated django admin
  interface
- Locations are recursive so things can be in the kitchen pantry closet on the 3rd shelf on the right and still be in
  the kitchen

# Getting started (development/testing)
```
dnf install -y python3-pip git
pip3 install django
git clone git@github.com:JensTimmerman/im.git
cd im

python3 manage.py migrate
python3 manage.py createsuperuser 
```
add username and password for your admin login and start the development server
```
python3 manage.py runserver
```



Now you are running the development server, Visit http://127.0.0.1:8000/admin/
   to create a pantry inventory

5. Visit http://127.0.0.1:8000/inventory/ to view your inventory website.


# installation
```
dnf install python3-pip git
pip3 install django psycopg2 gunicorn
git clone git@github.com:JensTimmerman/im.git
cd im
vim im/settings.py
```
change key,: `''.join(random.SystemRandom().choice(string.printable) for i in range(50))`
set DEBUG=False
set allowed_hosts to the hosts you want to allow (e.g. [localhost, 127.0.0.1, 192.168.1.108, im.yourdomain] 

configure DATABASES to point to your database server
```
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventorryapp',
        'USER': 'inventorryapp',
        'PASSWORD': '<password>',
        'HOST': '<db server ip',
        'PORT': '', 
    }   
}
```

clear migrations and start from empty db
```
rm inventory/migrations/* -rf 
python3 manage.py migrate


python3 manage.py createsuperuser
python3 ./manage.py collectstatic
```
add im user
```
useradd im
```
add systemd service file
```

vim /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=im
Group=im
WorkingDirectory=/home/im
ExecStart=/usr/local/bin/gunicorn --workers 1 --bind 0.0.0.0:8000 im.wsgi:application


[Install]
WantedBy=multi-user.target

```

```
systemctl enable gunicorn
systemctl start gunicorn
```


on your nginx server
```

useradd im

sudo usermod -a -G im nginx

chmod 710 /home/im

chcon -Rt httpd_sys_content_t /home/im/
rsync -rav /home/im/inventorryapp/static/  <app_server_ip>:/home/im/inventorryapp/static/

```
in /etc/nginx/nginx.conf
DNS: to do manually set up a cname for im to point to yourdomain 
```
    server {
       listen 80;
       server_name im.yourdomain ;
       location /static {
           root /home/im/inventorryapp/static ;
       }
       location / {
          proxy_pass http://192.168.122.6:8000;
          proxy_redirect off ;
          proxy_set_header Host $host ;
          proxy_set_header X-Real-IP $remote_addr ;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for ;
          proxy_max_temp_file_size 0 ;
          client_max_body_size 10m ;
          client_body_buffer_size 128k ;
          proxy_connect_timeout 90 ;
          proxy_send_timeout 90 ;
          proxy_read_timeout 90 ;
          proxy_buffer_size 4k ;
          proxy_buffers 4 32k ;
          proxy_busy_buffers_size 64k ;
          proxy_temp_file_write_size 64k ;
       }
```
```
pip3 install certbot-nginx
certbot -n --nginx -d im.yourodmain --hsts
```

browse to https://im.yourdomain


# feature requests
## High
- Add itmes per location, click a location and then start adding items with the location list prepopulated
- auto refresh dropdown boxes after items have been added in admin view, so page reload is not needed
- auto parse dates in different date formats when given in a datefield. e.g. 20 12 2020 or 2020 12 20 to 2020-12-20
 - also make ipad show the numbered keyboard here
  - actually perhaps a date scroller is nicer here
- units always minor case
- make expirations a calendar view, generate ics file to import
- public wishlist
- easy clearing of shopping list
- add easy consume view
 - save date consumed in history

## medium
# medium high
- mobile app
 - (requires rest api?)
- garden something? layout
- journal of things thrown away

# medium
- make work offline
- add users
 - federated? use sqrl instead of passwords?


# medium low
- allow for lending stuff out
 - auto mailings when things should be returned?
 - double bookkeeping of where things are if both parties have this set up
  - ipfs (+ blockchain?)
   - will be done in a seperate app, oos for inventory

- make it look something like this https://getbootstrap.com/docs/4.0/examples/dashboard/


- figure out average usage of items over time and predict how much to buy in shopping list based on average expiry
  dates
- figure out how long a certain item can last given current stock and average usage

- easily deploy somewhere

## low
- add recepies
- shopping list created based on recepy ingredients
- auto proposal of recepy based on next expiry dates
- offer to buy things that have been on shopping list for a while online (in bulk/aggregated)
- 3d view of where things are in space
- vr to help locate things
