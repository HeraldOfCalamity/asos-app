// ProcessForm.js

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
    const handleSubmit = (e) => {
        e.preventDefault();
        // Add the current form data to the list of processes
        setProcesses([...processes, formData]);
        // Clear the form
        setFormData({ name: '', cpu_time: '', arrival: '', priority: '' });
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
                <button className='bg-green-600 border border-green-600 hover:bg-green-600 text-white rounded'  type="submit">Add Process</button>
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
