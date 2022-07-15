from app import create_app, config

app = create_app()

env = config['ENVIRONMENT']
debug = env == 'develop'
from routes import *

if __name__ == '__main__':
    app.run(debug=debug, host='0.0.0.0', port=5000)
