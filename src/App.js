import logo from './logo.svg';
import { Button } from 'bootstrap';
import './App.css';
import Hello from './component/Hello';
import Welcome from './component/Welcome';

function App() {
  const name ='Tom'
  const user = {
    name: '네이버',
    url: 'https://m.naver.com/'
  }
  return (
    <div className="App">
      <div style={{color: 'red', font: 'bold', fontSize: '50px', backgroundColor: 'greenyellow'}}>
        welcome, {name}
        <p>{2+3}</p>
      </div>
      <a href={user.url}>{user.name}</a>
      <Hello/>
      <Welcome/>
      <button> primary button </button>
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
          <br/> 송가람 react test 입니다.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
