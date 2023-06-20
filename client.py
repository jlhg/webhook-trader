#!/usr/bin/env python
import socketio
import shioaji as sj

sio = socketio.Client()


@sio.on('get')
def get(data):
    print(data)  # {'from': 'server'}


if __name__ == '__main__':
    sio.connect('ws://localhost:5001')


    # https://sinotrade.github.io/quickstart/
    api = sj.Shioaji()
    accounts =  api.login("YOUR_API_KEY", "YOUR_SECRET_KEY")
    api.activate_ca(
        ca_path="/c/your/ca/path/Sinopac.pfx",
        ca_passwd="YOUR_CA_PASSWORD",
        person_id="Person of this Ca",
    )

    contract = api.Contracts.Stocks["2890"]
    order = api.Order(
        price=12,
        quantity=5,
        action=sj.constant.Action.Buy,
        price_type=sj.constant.StockPriceType.LMT,
        order_type=sj.constant.OrderType.ROD,
    )
    trade = api.place_order(contract, order)
