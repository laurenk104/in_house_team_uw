import React from "react"

export default class ChatSender extends React.Component {
    constructor(props) {
        super(props);
        this.socket = require('socket.io-client')('http://localhost:4040')
        this.state = {
            word: "",
        };
    }

    submit() {
        console.log("submitting word: " + this.state.word);
        this.socket.emit("ChatSender", this.state.word);
        // resetting state to null
        this.setState({
            word: "",
        })
    }

    handleChange(value) {
        this.setState({
            word: value
        });
    }

    render() {
        return (
            <div>
                <input type="text" value={this.state.word} onChange={(e) =>this.handleChange(e.target.value)} />
                <input type="submit" value="Send" onClick={() => this.submit()} />
            </div>
        );
    }
}