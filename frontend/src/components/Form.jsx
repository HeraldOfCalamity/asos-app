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
                <div className="w-10/12 my-5 grid grid-cols-2  gap-4 md:grid-cols-4 m-auto">
                    <input
                        type="text"
                        name="name"
                        placeholder="Name"
                        value={formData.name}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                        required
                    />
                    <input
                        type="text"
                        name="cpu_time"
                        placeholder="CPU"
                        value={formData.cpu_time}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                        required
                    />
                    <input
                        type="text"
                        name="arrival"
                        placeholder="Arrival"
                        value={formData.arrival}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                    />
                    <input
                        type="text"
                        name="priority"
                        placeholder="Priority"
                        value={formData.priority}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                    />
                </div>

                <div className="flex justify-center items-center h-full m-3">
                    <button className='bg-blue-600 border border-blue-600 hover:bg-blue-600 text-white rounded mx-auto p-1' type="submit">Add Process</button>
                </div>


            </form>
            <div className="w-10/12 border rounded-lg shadow overflow-hidden dark:border-gray-700 dark:shadow-gray-900 m-auto">
                <table className="w-full text-sm text-center text-gray-500 dark:text-gray-400" >
                    <thead className="text-base bg-gray-50 dark:bg-gray-700">
                        <tr>
                            <th className="py-3">Name</th>
                            <th>CPU</th>
                            <th>Arrival</th>
                            <th>Priority</th>
                        </tr>
                    </thead>
                    <tbody className="font-medium text-base divide-y divide-gray-200 dark:divide-gray-700">
                        {processes.map((process, index) => (
                            <tr key={index}>
                                <td className="py-3">{process.name}</td>
                                <td>{process.cpu_time}</td>
                                <td>{process.arrival}</td>
                                <td>{process.priority}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            {processes.length != 0 && <div className="flex justify-center items-center h-full m-3">
                <button className='bg-blue-600 border border-blue-600 hover:bg-blue-600 text-white rounded mx-auto p-2' type="submit">Generar Diagrama</button>
            </div>}
        </div>
    );
}

export default ProcessForm;
