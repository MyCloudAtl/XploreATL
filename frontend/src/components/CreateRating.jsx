import React, { useState , useEffect} from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

export default function CreateRating () {
  const { id } = useParams()
  const navigate = useNavigate()
  const [rating, setRating] = useState({
    rating: '',
    eatery: '',
    hotspot: ''
  });
  const [updated, setUpdated] = useState(false)
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const ratingDetails = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/ratings/${id}`)
            setRating(response.data)
            setLoading(false)
        } catch (error) {
            console.error('Error fetching rating data:', error)
        }
    }
    ratingDetails()
}, [id])

const handleSubmit = async(e) => {
  e.preventDefault();
  try {
      const response = await axios.put(`http://localhost:8000/ratings/${id}`, rating)
      console.log('Rating updated successfully:', response.data)
      setUpdated(true);
  } catch (error) {
      console.error('Error updating rating:', error)
}}

const handleChange = (e) => {
    const { name, value } = e.target;
        setRating(prevRating => ({
            ...prevRating,
            [name]: value
        }));
};

useEffect(() => {
  if (updated) {
      navigate('/');
  }
}, [updated, navigate]);

if (loading) {
  return <div>Loading...</div>
}

return (
    <div>
      <h2>Leave a Rating</h2>
      <form onSubmit={handleSubmit}>
            <label>Rating:</label>
            <input type="number" name="rating" value={rating.rating} onChange={handleChange} required />
            {/* <label>Date Posted:</label>
            <input type="date" name="date" value={rating.date_posted} onChange={handleChange} /> */}
            <label>Eatery:</label>
            <input type="text" name="eatery" value={rating.eatery} onChange={handleChange} />
            <label>HotSpot:</label>
            <input type="text" name="hotspot" value={rating.hotspot} onChange={handleChange} />
            <button type="submit">Update</button>
        </form>
    </div>
  );
};