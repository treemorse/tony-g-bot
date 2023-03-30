# create a Google Cloud Function running this command in the same line

``` shell
gcloud functions deploy telegram_bot --set-env-vars "TELEGRAM_TOKEN=6077821786:AAG59BKb2tGylC9knGY1_fRBHnuQQnstZJk" --runtime python39 --trigger-http --project=sample-bot-382120 --region=central1-a
```

Some details:

* Here webhook is the name of the function in the `main.py` file
* You need to specify your Telegram token with the `--set-env-vars` option
* `--runtime python38` describe the environment used by our function, Python 3.8 in this case
* `--trigger-http` is the type of trigger associated to this function, you can find here the complete list of triggers
The above command will return something like this:
  
Step three, you need to set up your Webhook URL using this API call:

``` shell
curl "https://api.telegram.org/bot6077821786:AAG59BKb2tGylC9knGY1_fRBHnuQQnstZJk/setWebhook?url=https://central1-a-sample-bot-382120.cloudfunctions.net/telegram_bot"
```
