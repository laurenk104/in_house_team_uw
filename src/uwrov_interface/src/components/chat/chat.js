import React from "react"
export default class Chat extends React.Component {
  constructor(props) {
    super(props)
    this.socket = require('socket.io-client')('http://localhost:4040')
    this.state = {
      text: [],
    }
    this.socket.on("Chat", this.updateChat);
  }

  updateChat = (data) => {
    console.log(data.text);
    if (this.state.text.length == 5) {
      // maintain array length of 5
      this.setState({
        
      })
    }
    this.setState({
      text: this.state.text.concat([data.text])
    })
    console.log(this.state.text)
  }

  render() {
    return (
      <div className="text">
        {
          this.state.text.map(entry => <div>{entry}<br/></div>)
        }
      </div>
    )
  }
}