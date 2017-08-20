from app import app


run = app.run

if __name__ == "__main__":
    run(debug=True, port=5001)