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
            <th>Current Price</th>
            <th>Previous Close</th>
            <th>Sector</th>
            <th>Dividend Yield</th>
            <th>Logo URL</th>
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
              <tr key={stock.pk}>
                <td>{stock.symbol}</td>
                <td>{stock.name}</td>
                <td>{stock.currentPrice}</td>
                <td>{stock.previousClose}</td>
                <td>{stock.sector}</td>
                <td>{stock.dividendYield}</td>
                <td>{stock.logoUrl}</td>
                <td align="center">
                  <NewStockModal
                    create={false}
                    stock={stock}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={stock.pk}
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