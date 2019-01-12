import React, { Component } from 'react';
import Faq  from './components/faq/Faq';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      data:[]
    }
  }
  componentDidMount(){
    fetch('http://localhost:8000/api/v1/faqs')
    .then( response => response.json())
    .then( parsedResponse => this.setState({data:parsedResponse}))
    .catch( err => console.log(err))
  }
  render() {
    return (
      /* rest application logic */
      <div className="fluid">
        <Faq data = {this.state.data}/>
      </div>
      
    );
  }
}

export default App;
