import base64
import drawTable
from flask import Flask
from io import BytesIO

app = Flask(__name__)

dt = drawTable.DrawTable()


@app.route('/page1')
def pageOne():
    sio = BytesIO()
    dt.showBar().savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    print(data)
    dt.showBar().show()
    html = '''
                    <html>
                        <body>
                            <img src="data:image/png;base64,{}" />
                        </body>
                     <html>
                 '''
    return html.format(data)


@app.route('/page2')
def pageTwo():
    sio = BytesIO()
    dt.showScatter().savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    print(data)
    dt.showScatter().show()
    html = '''
                    <html>
                        <body>
                            <img src="data:image/png;base64,{}" />
                        </body>
                     <html>
                 '''
    return html.format(data)


@app.route('/page3')
def pageThree():
    sio = BytesIO()
    dt.showPie().savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    print(data)
    dt.showPie().show()
    html = '''
                    <html>
                        <body>
                            <img src="data:image/png;base64,{}" />
                        </body>
                     <html>
                 '''
    return html.format(data)


@app.route('/page4')
def pageFour():
    sio = BytesIO()
    dt.showBar2().savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    print(data)
    dt.showBar2().show()
    html = '''
                    <html>
                        <body>
                            <img src="data:image/png;base64,{}" />
                        </body>
                     <html>
                 '''
    return html.format(data)


if __name__ == '__main__':
    app.run()
    '''
    url = 'https://dl.ke.com/ershoufang/pulandian/'
    gd = getData.Sniper(url)
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 5:
        urls = gd.getURLs()
        gd.getMessage(urls)
    '''

    '''
    sum1 = 0
    print(len(price))
    for i in price:
        sum1 += i
    print(sum1 / len(price))

    total = 0
    for i in range(len(data)):
        if data[i:i + 1].get('所在区域')[i] == '中山区':
            total += data[i:i + 1].单价[i]
    print(total)
    '''

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
