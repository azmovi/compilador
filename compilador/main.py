from cyclopts import App


app = App()

@app.default
def main(path: str):
    try:
        print(path)
    finally:
        print('funcionou')
