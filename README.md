#  Get Started

## Install ampalibe in your pc

```sh
pip install ampalibe
```

## Create a .env file
```yml
# PAGE ACCESS TOKEN 
export AMP_ACCESS_TOKEN=<Facebook Page Access Token>

# PAGE VERIF TOKEN
export AMP_VERIF_TOKEN=<random_token>


# DATABASE AUTHENTIFICATION
#export ADAPTER=SQLITE
#export ADAPTER=MYSQL
export ADAPTER=POSTGRESQL
#export ADAPTER=MONGODB

####### CASE MYSQL, POSTGRESQL OR MONGODB ADAPTER
export DB_HOST=
export DB_USER=
export DB_PASSWORD=
export DB_NAME=
export DB_PORT=
#export SRV_PROTOCOL=1

####### CASE SQLITE ADAPTER
#export DB_FILE=ampalibe.db


# APPLICATION CONFIGURATION
export AMP_HOST=0.0.0.0
export AMP_PORT=4555

# URL APPLICATION, use ngrok to create online tunnel for your localhost
export AMP_URL=<Your https ngrok link>
```

## Run your app
```sh
ampalibe run --dev
```
```sh
ngrok http 4555
```

