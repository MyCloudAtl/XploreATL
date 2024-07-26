import React, { useState } from 'react';
import axios from 'axios';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(username)
        if (password !== confirmPassword) {
            setMessage('Passwords do not match');
            return;
        }

        try {
            const response = await axios.post('http://localhost:8000/users/', {
                username,
                password
            });
            setMessage(response.data.message);
        } catch (error) {
            setMessage('Registration failed');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Register</h2>
            <div>
                <label>Username:</label>
                <input
                    type="text"
                    name={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Password:</label>
                <input
                    type="password"
                    name={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </div>
            <div>
                <label>Confirm Password:</label>
                <input
                    type="password"
                    name={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    required
                />
            </div>
            <button type="submit">Register</button>
            <p>{message}</p>
        </form>
    );
};

export default RegisterForm;