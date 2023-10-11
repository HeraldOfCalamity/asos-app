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

    const addProcess = () => {
        if (
            formData.name.trim() === '' ||
            formData.cpu_time.trim() === '' ||
            formData.arrival.trim() === '' ||
            formData.priority.trim() === ''
        ){
            // if (formData.priority.trim() === '') setFormData({...formData, priority:''})
            console.error('Fields name, cpu_time and arrival cannot be blank');
            return;
        }

        // Add the current form data to the list of processes        
        setProcesses([...processes, formData]);
        // Clear the form
        setFormData({ name: '', cpu_time: '', arrival: '', priority: '' });
    }

    const getGantt = async () => {
        
        try{
            
            await axios.get('http://localhost:8000/api/process')
                .then(res => {
                    console.log('============ Response form GET ===============');
                    console.log(res.data);
                })
                .catch(error => {
                    console.log(error);
                })
        } catch (error) {
            console.log('Error: ', error)
        }
        
    }

    const deleteProcess = () => {
        const updatedProcesses = processes.slice(0, -1);
        setProcesses(updatedProcesses)
    }
    // Function to handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        // minimum one elemento must be entered
        if (processes.length == 0)
            {console.error('Why are you trying to send an empty form ? xd')
            return}
        
        // Send the processes data to the API
        let request = {"data":processes, "method":"FCFS"};
        console.log(request);
        try {
            // const dataArray = [
            //     { name: "Process 1", cpu_time: 10, arrival: 5, priority: 2 },
            //     { name: "Process 2", cpu_time: 8, arrival: 3, priority: 1 },
            //     // Add more data objects as needed
            // ];
            
            await axios.post('http://localhost:8000/api/process',request , {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(res => {
                    console.log(res.data);
                    console.log('Todo bien con el POST')
                    getGantt()
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
            <form className='mx-3' onSubmit={handleSubmit}>
                <div className="mb-4">
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
                <div className=''>
                    <button className='p-2 bg-green-600 border border-green-800 hover:bg-green-700 text-white rounded me-2' type="button" onClick={addProcess}>Add Process</button>
                    <button className='p-2 bg-red-600 border border-red-800 hover:bg-red-700 text-white rounded me-2' type='button' onClick={deleteProcess}>Delete Process</button>
                    <button className='p-2 bg-indigo-600 border border-indigo-800 hover:bg-indigo-700 text-white rounded' type='submit'>Begin processing</button>
                </div>              
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
