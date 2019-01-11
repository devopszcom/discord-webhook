def convert_sentry(data):
    attachment = dict()
    attachment['color'] = "#f43f20"
    attachment['fields'] = list()
    attachment['fields'].append({
        'title': 'Culprit',
        'value': data['culprit'],
        'short': False,
    })
    attachment['fields'].append({
        'title': 'Project',
        'value': data['project'],
        'short': False,
    })

    attachment['fallback'] = '[{}] {}'.format({data["project"]}, data['event']['metadata']['title'])
    attachment['title_link'] = data['url']
    attachment['title'] = data['event']['metadata']['title']

    discord_data = dict()
    # discord_data['username'] = 'Sentry'
    discord_data['attachments'] = list()
    discord_data['attachments'].append(attachment)

    return discord_data
