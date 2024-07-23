import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import NavBar from './NavBar'

export default function Home() {

  return (
    <div className="Home">
        <h1>Home</h1>
        <header>
           {<NavBar/> }
        </header>
    </div>
  )
}