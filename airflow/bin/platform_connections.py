import sys
import os

class PlatformConnections(object):

    @classmethod
    def connect_data_platform(cls):

        # Import required arguments to run Data Platform
        sys_path = os.environ.get('DATA_PLATFORM_PATH')
        sys.path.insert(0,sys_path)
        sys.dont_write_bytecode = True

        from tornado.options import options
        from data_platform.server import DataPlatform
        from data_platform.server import configure
        from data_platform.core.options import define_for_server

        # Connect to application
        define_for_server()
        options.env = os.environ.get('AIRFLOW_ENV')
        configure()
        application = DataPlatform(options, None)
        application.connect()
