from app import create_app

app = create_app(config_name="production")

if __name__ == '__main__':
    app.run(debug=True)