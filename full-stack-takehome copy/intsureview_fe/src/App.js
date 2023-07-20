import logo from './logo.svg';
import './App.css';
import Header from './Components/Header';
import Footer from './Components/Footer';
import axios from 'axios';
import React from 'react';

class App extends React.Component {
  
  state = {
    details: [],
  }

  componentDidMount() {
    let data ;

    axios.get('http://localhost:8000/wel/')
    .then(res => {
      data = res.data;
      this.setState({
        details : data
      });
    })
    .catch(err => {})
  }

  render() {
   
    return(
      <div>
         <Header />

        
        {this.state.details.map((detail, id) => (
          <div key={id}>
            <div >
              <div>
                <h1>{detail.detail} </h1>
                <footer > --- by 
                <cite title="Source Title">
                  {detail.name}
                </cite>
                </footer>
              </div>
            </div>
          </div>
        )
      )}
      <Footer />
      </div>
    );
  }

}

export default App;





/*function App() {
  return (
    <div className="App">
      <Header />
      
      <header className="App-header">
        <main>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> 

        </main>
      </header>


      <Footer />
    </div>
  );
}

export default App;*/
