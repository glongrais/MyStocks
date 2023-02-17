import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewStockForm extends React.Component {
  state = {
    pk: 0,
    symbol: "",
    name: "",
    currentPrice: 0,
    previousClose: 0,
    sector: "",
    dividendYield: 0,
    logoUrl: ""
  };

  componentDidMount() {
    if (this.props.stock) {
      const { pk, symbol, name, currentPrice, previousClose, sector, dividendYield, logoUrl } = this.props.stock;
      this.setState({ pk, symbol, name, currentPrice, previousClose, sector, dividendYield, logoUrl });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createStock = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editStock = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.stock ? this.editStock : this.createStock}>
        <FormGroup>
          <Label for="symbol">Symbol:</Label>
          <Input
            type="text"
            name="symbol"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.symbol)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="currentPrice">Current Price:</Label>
          <Input
            type="float"
            name="currentPrice"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.currentPrice)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="previousClose">Previous Close:</Label>
          <Input
            type="float"
            name="previousClose"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.previousClose)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="sector">Sector:</Label>
          <Input
            type="text"
            name="sector"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.sector)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="dividendYield">Dividend Yield:</Label>
          <Input
            type="float"
            name="dividendYield"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.dividendYield)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="logoUrl">Logo URL:</Label>
          <Input
            type="text"
            name="logoUrl"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.logoUrl)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewStockForm;