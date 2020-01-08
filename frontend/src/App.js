import React, { Component } from 'react';

class App extends Component {
  state = {
    albums: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/albums/');
      const albums = await res.json();
      this.setState({
        albums: albums.results
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.albums.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.artist}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
