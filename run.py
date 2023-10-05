from market import app

# check if the run.py has been executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True)