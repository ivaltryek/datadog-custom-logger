# Datadog Custom Logger
[![PyPI version](https://badge.fury.io/py/datadog-custom-logger.svg)](https://badge.fury.io/py/datadog-custom-logger)  [![Open in VS Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/meet86/datadog-custom-logger)

## Usage

### Steps
- Install pip package
  
  ```shell
  pip install datadog-custom-logger==0.1.0
  ```
- Import package
  
  ```python
  from datadog_custom_logger import DatadogCustomLogHandler
  ```
- Initialize the handler
  
  ```python
  datadog_custom_handler = DatadogCustomLogHandler(level=logging.INFO)  
  ```
  > 💡Note: if the level is set to logging.WARNING, you won't be able to see info or debug level logs.

## Hierarchy:
    - debug (logging.DEBUG)
    - info (logging.INFO)
    - warning (logging.WARNING)
    - error (logging.ERROR)
  
- Attach the handler
  
  ```python
  logging.basicConfig()
  logger = logging.getLogger()
  logger.addHandler(datadog_custom_handler)
  logging.getLogger().setLevel(logging.INFO)
  ```
- Now simply log the logs
  
  ```python
  # This statement won't be logged because the .setLevel() is set to logging.INFO.
  # Please check the logging hierarchy for more.
  logging.debug("This is debug level code")
  # This will be logged as per .setLevel()
  logging.info("This is info level logs")
  ```

  ## Complete example:
  [![datadog-logger-example](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/meet86/datadog-logger-example)

  

