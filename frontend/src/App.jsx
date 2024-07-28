import './App.css'
import { Routes, Route } from 'react-router-dom'
import Home from './components/Home'
import EateryCard from './components/EateryCard'
import EateryList from './components/EateryList'
import HotSpotCard from './components/HotSpotCard'
import HotSpotList from './components/HotSpotList'
import Locations from './components/Locations'
import RatingForm from './components/RatingForm'
import CreateRating from './components/CreateRating'
import Login from './components/Login'
import Logout from './components/Logout'
import SideBar from './components/SideBar'
import RegisterForm from './components/RegisterForm'
// import Opening from './components/Opening'

function App() {

  return (
      <div className='App'>
        <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/eateries/" element={<EateryList />} />
                <Route path="/eateries/:id" element={<EateryCard />} />
                <Route path="/hotspots" element={<HotSpotList />} />
                <Route path="/hotspots/:id" element={<HotSpotCard />} />
                <Route path="/locations" element={<Locations />} />
                <Route path="/ratings/:id" element={<CreateRating />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<RegisterForm />} />
                <Route path="/logout" element={<Logout />} />
                <Route path="/user/:id" element={<SideBar />} />
                <Route path="/sidebar" element={<SideBar />} />
                {/* <Route path="/" element={<Opening currentUser={currentUser} />} /> */}
        </Routes>
      </div>
  )
}
export default App
