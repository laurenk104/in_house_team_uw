import React from "react"

var count = 0;
var list = [];

export default class Chat extends React.Component { 
  constructor(props) {
    super(props)
    this.socket = require('socket.io-client')('http://localhost:4040')
    this.socket.on("Chat", this.updateChat);
  }

  updateChat = (data) => {
    console.log("received new message..." + data.text);
    if (count == 10) {
      list.shift();
      count -= 1;
    }
    list.push(data.text);
    count += 1;
  }

  render() {
    return (
      <div className="text-box">
        Test
      </div>
    )
  }
}