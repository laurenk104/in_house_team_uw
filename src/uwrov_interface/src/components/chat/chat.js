import React from "react"

function Text(props) {
  const text = props.text;
  return text.split('\n').map(str => <p>{str}</p>);
}
export default class Chat extends React.Component {
  constructor(props) {
    super(props)
    this.socket = require('socket.io-client')('http://localhost:4040')
    this.state = {
      text: "Placeholder Text",
    }
    this.socket.on("Chat", this.updateChat);
  }

  updateChat = (data) => {
    console.log("received new message: " + data.text);
    this.setState({ text: data.text });
  }

  render() {
    return (
      <div className="text-box">
        <Text text={this.state.text}/>
      </div>
    )
  }
}