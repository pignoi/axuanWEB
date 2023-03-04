from server import t_ser

app = t_ser()

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug=True)
