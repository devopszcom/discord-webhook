import requests
from flask import Flask
from flask import jsonify, request

import config
import converter
from utils import get_ip

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=config.SENTRY_DNS,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route("/")
def get_your_ip():
    real_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    data = {'ip': get_ip(request.remote_addr), 'real_ip': real_ip}

    return jsonify(data)


@app.route('/api/webhooks/convert')
def convert():
    discord_webhook_url = request.args.get('webhook_url')
    forwarder_webhook_url = discord_webhook_url.replace(config.DISCORD_BASE_URL, config.FORWARDER_BASE_URL)

    return forwarder_webhook_url


@app.route('/api/webhooks/<channel_id>/<token>/<type>', methods=['GET', 'POST'])
def forward(channel_id, token, type):
    # dest_url = '{}/api/webhooks/{}/{}'.format(DISCORD_BASE_URL, channel_id, token)
    dest_url = '{}/api/webhooks/{}/{}/slack'.format(config.DISCORD_BASE_URL, channel_id, token)

    origin_data = request.get_json()

    if type == 'sentry':
        discord_data = converter.convert_sentry(origin_data)

    res = requests.post(dest_url, json=discord_data)

    return jsonify(res.content)
