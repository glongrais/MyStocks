import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="https://imageio.forbes.com/specials-images/imageserve/6354154d5e097d68cc4360ba/Picture-shows-green-graph-line-in-front-of-quotation-board/960x0.jpg?format=jpg&width=960"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i>presents</i>
        </h5>
        <h1>App with React + Django</h1>
      </div>
    );
  }
}

export default Header;