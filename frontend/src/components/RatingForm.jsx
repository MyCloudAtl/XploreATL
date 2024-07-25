import React, { useState } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom'

export default function RatingForm ({placeType}) {
  const { id } = useParams()
  const [rating, setRating] = useState(1)

  const handleRatingChange = (e) => {
    setRating(parseInt(e.target.value))
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const ratingData = {
      rating: rating,
      place_id: id,
      place_type: placeType
    };

    axios.post('http://localhost:8000/ratings/', ratingData)
      .then(response => {
        console.log('Rating submitted successfully:', response.data);
        setRating(1);
        setComment('');
      })
      .catch(error => {
        console.error('Error submitting rating:', error);
      });
  };

  return (
    <div>
      <h2>Leave a Rating</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Rating:</label>
          <select value={rating} onChange={handleRatingChange}>
            {[1, 2, 3, 4, 5].map(num => (
              <option key={num} value={num}>{num} Stars</option>
            ))}
          </select>
        </div>
        <div>
          <label>Comment:</label>
          <textarea value={comment} onChange={handleCommentChange} />
        </div>
        <button type="submit">Submit Review</button>
      </form>
      <Link to={`/ratings/${id}/update`}>Update Rating</Link>
    </div>
  );
};


