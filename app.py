import os # GCP stuff
import logging
import google.cloud.logging
from slack_bot import SlackBot

def main():
    # Console Logs
    logging.basicConfig(level=logging.INFO)

    # Google Cloud Providor
    if int(os.environ.get("PRODUCTION", 0)) == 1:
        logging_client = google.cloud.logging.Client()
        logging_client.setup_logging

    # Slack Bot Intergration
    bot = SlackBot()    
    bot.start()

if __name__ == "__main__":
    main()
