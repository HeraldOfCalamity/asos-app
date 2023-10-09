// ProcessForm.js
import axios from 'axios'
import React, { useState } from 'react';

function ProcessForm() {
    // State to store the list of processes
    const [processes, setProcesses] = useState([]);
    // State to store form input values
    const [formData, setFormData] = useState({
        name: '',
        cpu_time: '',
        arrival: '',
        priority: '',
    });

    // Function to handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        // Add the current form data to the list of processes
        setProcesses([...processes, formData]);
        // Clear the form
        setFormData({ name: '', cpu_time: '', arrival: '', priority: '' });
        // Send the processes data to the API
        try {
            // const dataArray = [
            //     { name: "Process 1", cpu_time: 10, arrival: 5, priority: 2 },
            //     { name: "Process 2", cpu_time: 8, arrival: 3, priority: 1 },
            //     // Add more data objects as needed
            // ];
            await axios.post('http://localhost:8000/api/process', processes, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(res => {
                    console.log(res.data);
                })
                .catch(error => {
                    console.log(error);
                })
            // Handle successful API response
        } catch (error) {
            // Handle API error
            console.error('Error:', error);
        }
    };

    // Function to handle input changes
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    return (
        <div className=''>
            <form onSubmit={handleSubmit}>
                <div className="mb-2">
                    <input
                        type="text"
                        name="name"
                        placeholder="Name"
                        value={formData.name}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400'
                    />
                    <input
                        type="text"
                        name="cpu_time"
                        placeholder="CPU"
                        value={formData.cpu_time}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400'
                    />
                    <input
                        type="text"
                        name="arrival"
                        placeholder="Arrival"
                        value={formData.arrival}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400'
                    />
                    <input
                        type="text"
                        name="priority"
                        placeholder="Priority"
                        value={formData.priority}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400'
                    />
                </div>
                <button className='p-2 bg-green-600 border border-green-600 hover:bg-green-700 text-white rounded me-2' type="submit">Add Process</button>
                {/* <button className='p-2 bg-green-600 border border-green-600 hover:bg-green-700 text-white rounded' type="submit">Add Process</button> */}
            </form>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>CPU</th>
                        <th>Arrival</th>
                        <th>Priority</th>
                    </tr>
                </thead>
                <tbody>
                    {processes.map((process, index) => (
                        <tr key={index}>
                            <td>{process.name}</td>
                            <td>{process.cpu_time}</td>
                            <td>{process.arrival}</td>
                            <td>{process.priority}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ProcessForm;
