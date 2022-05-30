import logging
import datetime
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    now = datetime.datetime.now()
   
    return func.HttpResponse (
        now.strftime("%Y-%m-%d %H:%M:%S")
        )

    