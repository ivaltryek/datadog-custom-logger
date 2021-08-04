import os
import logging
import datetime
from dateutil.parser import parse as dateutil_parser

# Datadog python client dependencies.
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_api
from datadog_api_client.v1.models import *

LOG_LEVEL_ALERT_TYPE_MAPPINGS = {
    logging.DEBUG: "info",
    logging.INFO: "info",
    logging.WARNING: "warning",
    logging.ERROR: "error",
    logging.CRITICAL: "error"
}


class DatadogCustomLogHandler(logging.Handler):

    def __init__(self, tags=None, service="default", ** kwargs):
        super(DatadogCustomLogHandler, self).__init__(**kwargs)

        self.tags = tags
        self.service = service

    def emit(self, record):
        text = self.format(record)

        create_args = {
            "title": record.getMessage(),
            "text": text
        }

        if record.levelno in LOG_LEVEL_ALERT_TYPE_MAPPINGS:
            create_args["alert_type"] = LOG_LEVEL_ALERT_TYPE_MAPPINGS[record.levelno]

        # Datadog Configuration
        configuration = Configuration()

        # configuration.api_key['apiKeyAuth'] = os.environ['DD_CLIENT_API_KEY']

        # Get UTC time and format it into default Datadog Python log pipeline standards.
        time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S,%f')[:-3]
        
        with ApiClient(configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            body = HTTPLog([
                HTTPLogItem(
                    ddsource="python",
                    message=f"{time} {record.levelname.upper()} :: {create_args['text']}",
                    service=self.service,
                    ddtags=self.tags +
                    f",level:{record.levelname}" if self.tags is not None else f"level:{record.levelname}"
                )
            ])
        try:
            api_response = api_instance.submit_log(body)
        except ApiException as e:
            logging.info(
                "Exception when calling LogsApi->submit_log: %s\n" % e)