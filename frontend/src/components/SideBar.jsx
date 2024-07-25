import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { useParams } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

export default function SideBar() {
  const [profiles, setProfiles] = useState([])
  const {id} = useParams()

  useEffect(() => {
      const profilesData = async () => {
          try {
              const response = await axios.get('http://localhost:8000/user/')
              console.log('Profiles data:', response.data);
              if (response.status !== 200) {
                  throw new Error('Not working')
              }
              setProfiles(response.data)
          } catch (error) {
              console.error('Error grabbing profiles', error)
          }
      };
  profilesData ();
  }, [id]);

  if (!profiles) {
    return <div>Loading...</div>
}


  return (
    <div className="SideBar">
        <h1>SideBar</h1>
        <ul>
       {/* {profiles.map(profile => (
          <li key={profile.id}> */}
            <h2> Nice to see you again! {user.username}</h2>
           <div>
             <h3> Chronicles:</h3>
             <h3>Favorites: </h3> 
             <h4>{profiles.favorite_eateries}</h4>
             <h4>{profiles.favorite_hotspots}</h4>
             <h3>Bookmarked: </h3>
             <h4>{profiles.bookmarked_eateries}</h4> 
             <h4>{profiles.bookmarked_hotspots}</h4> 
            
           </div>
         {/* </li>
       ))} */}
     </ul>
    </div>
  )
}