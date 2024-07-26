import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Link, useNavigate } from 'react-router-dom'

export default function SideBar() {
const [eateries, setEateries] = useState([])
const [hotspots, setHotspots] = useState([])
const [tasks, setTasks] = useState([])
const [taskInput, setTaskInput] = useState('')
const [editingTask, setEditingTask] = useState(null)
const [taskEditIndex, setTaskEditIndex] = useState(null)
const [user, setUser] = useState(null);
const [loading, setLoading] = useState(true);
const navigate = useNavigate();

useEffect(() => {
  const companyData = async () => {
    try {
      const [eateriesResponse, hotspotsResponse] = await Promise.all([
        axios.get('http://localhost:8000/eateries/'),
        axios.get('http://localhost:8000/hotspots/')
      ]);
      setEateries(eateriesResponse.data)
      setHotspots(hotspotsResponse.data)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  };
  companyData()
}, [])

const handleTaskSubmit = (e) => {
  e.preventDefault()
  if (taskInput.trim() === '') return

  if (taskEditIndex !== null) {
    const updatedTasks = tasks.map((task, index) =>
      index === taskEditIndex ? taskInput : task
    )
    setTasks(updatedTasks)
    setEditingTask(null)
    setTaskEditIndex(null)
  } else {
    setTasks([...tasks, taskInput])
  }
  setTaskInput('')
}

const handleEditClick = (index) => {
  setTaskInput(tasks[index])
  setEditingTask(tasks[index])
  setTaskEditIndex(index)
}

const handleDeleteClick = (index) => {
  setTasks(tasks.filter((_, i) => i !== index))
  if (taskEditIndex === index) {
    setEditingTask(null)
    setTaskEditIndex(null)
  }
}
useEffect(() => {
    const getUser = async () => {
      try {
          const response = await axios.get('http://localhost:8000/users/')
          setUser(response.data)
          console.log(user)
          setLoading(false)
      } catch (error) {
          console.error('Error fetching user data:', error)
          setLoading(false)
      }
  }
  getUser()
}, [])
  if (loading) {
      return <p>Loading...</p>;
  }

  if (!user) {
      return <p>No user data available.</p>;
  }

console.log(user[0])
return (
  <div className="Sidebar">
      {user ? (
        <div className='UserLink'>
          <h1 className="Greeting">Nice to have you back, {user[0].username}</h1>
          <div className="Logout">
            <Link to="/logout">Logout</Link>
          </div>
        </div>
      ) : (
        <div className='AuthLinks'>
          <Link to="/login">Login</Link>
          <Link to="/register">Create User</Link>
        </div>
      )}
    </div>
  )
}
      {/* <h1>Eateries</h1>
      <ul>
        {eateries.map(eatery => (
          <li key={eatery.id}>
            <h2>{eatery.name}</h2>
            <p>Rating: {eatery.avg_rating} Stars</p>
            <Link to={`/ratings/${eatery.id}?place_type=eatery`}>Rate This Eatery</Link>
            <hr />
          </li>
        ))}
      </ul>

      <h1>Hotspots</h1>
      <ul>
        {hotspots.map(hotspot => (
          <li key={hotspot.id}>
            <h2>{hotspot.name}</h2>
            <p>Rating: {hotspot.avg_rating} Stars</p>
            <Link to={`/ratings/${hotspot.id}?place_type=hotspot`}>Rate This Hotspot</Link>
            <hr />
          </li>
        ))}
      </ul>

      <h2>Wish List</h2>
      <form id="taskForm" onSubmit={handleTaskSubmit}>
        <input
          type="text"
          id="taskInput"
          value={taskInput}
          onChange={(e) => setTaskInput(e.target.value)}
          placeholder="Where to?"
          required
        />
        <button type="submit">
          {taskEditIndex !== null ? 'Update list' : 'Must See'}
        </button>
      </form>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task}
            <button onClick={() => handleEditClick(index)} className="edit">Edit</button>
            <button onClick={() => handleDeleteClick(index)} className="delete">Delete</button>
          </li>
        ))}
      </ul> */}
 