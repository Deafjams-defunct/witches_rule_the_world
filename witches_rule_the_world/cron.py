"""Cronjob for witches bot"""
import os
import plan
import witches_rule_the_world

def witches_cron():
    """Config for witches cron"""
    cron = plan.Plan('witches_rule_the_world')
    path = witches_rule_the_world.__path__[0]
    environment = {
        'WITCHES_CONSUMER_KEY': os.environ['WITCHES_CONSUMER_KEY'],
        'WITCHES_CONSUMER_SECRET': os.environ['WITCHES_CONSUMER_SECRET'],
        'WITCHES_OAUTH_TOKEN': os.environ['WITCHES_OAUTH_TOKEN'],
        'WITCHES_OAUTH_SECRET': os.environ['WITCHES_OAUTH_SECRET']
    }

    cron.script(
        'rule.py',
        every='10.minutes',
        path=path,
        environment=environment
    )

    #update cron if crontab exists, write new cron if crontab doesn't exist
    try:
        cron.run('update')

    except plan.PlanError:
        cron.run('write')

if __name__ == '__main__':
    witches_cron()
