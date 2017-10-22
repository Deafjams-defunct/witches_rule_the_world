# Witches Rule The World

A tumblr bot to reblog witchy stuff

## Install
```bash
git clone https://github.com/Deafjams/witches_rule_the_world.git
cd witches_rule_the_world
python setup.py
```

## Configure
```bash
export WITCHES_CONSUMER_KEY={{Your tumblr consumer key}}
export WITCHES_CONSUMER_SECRET={{Your tumblr consumer secret key}}
export WITCHES_OAUTH_TOKEN={{Your tumblr oauth token}}
export WITCHES_OAUTH_SECRET={{Your tumblr oauth secret}}
```

## Run
### Once
```bash
python rule.py
```

### Regularly via crontab
```bash
python cron.py
```
