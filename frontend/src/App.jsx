import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Routes, Route} from 'react-router-dom'
import Home from './components/Home'
import EateryCard from './components/EateryCard'
import EateryList from './components/EateryList'
import HotSpotCard from './components/HotSpotCard'
import HotSpotList from './components/HotSpotList'
import Locations from './components/Locations'

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
        </Routes>
      </div>
  )
}

export default App
