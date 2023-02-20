import React, { Component } from "react";
import { Table } from "reactstrap";
import NewStockModal from "./NewStockModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class StockList extends Component {
  render() {
    const stocks = this.props.stocks;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Symbol</th>
            <th>Name</th>
            <th>Quantity</th>
            <th>Current Price</th>
            <th>Purchased Price</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!stocks || stocks.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no stock yet</b>
              </td>
            </tr>
          ) : (
            stocks.map(stock => (
              <tr key={stock.id}>
                <td>{stock.stock.symbol}</td>
                <td>{stock.stock.name}</td>
                <td>{stock.shares}</td>
                <td>{stock.stock.currentPrice}</td>
                <td>{stock.purchasePrice}</td>
                <td align="center">
                  <NewStockModal
                    create={false}
                    stock={stock}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={stock.id}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default StockList;