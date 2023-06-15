import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import NavBar from './components/NavBar';

function App() {
  return (
    <div className="App">

      <NavBar/>
      <BrowserRouter>
        <Routes>
          <Route exact path='/' element={<Home/>} />
        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;
