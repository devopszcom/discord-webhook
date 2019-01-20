from os import environ

# Constants
FORWARDER_BASE_URL = environ.get('FORWARDER_BASE_URL', 'http://dev-discord-webhook.local')
DISCORD_BASE_URL = 'https://discordapp.com'

# Configure
SENTRY_DNS = environ.get('SENTRY_DNS', 'https://DUMMY_CONFIG@sentry.io/10101')
