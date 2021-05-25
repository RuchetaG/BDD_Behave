from Library import config_reader, InitiateDriver


def before_scenario(context, scenario):
    context.driver = InitiateDriver.startBrowser(config_reader.config_reader('Data', 'Browser'))


def after_scenario(context, scenario):
    context.driver.quit()
