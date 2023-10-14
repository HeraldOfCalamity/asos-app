// ProcessForm.js
import axios from 'axios'
import React, { useEffect, useState } from 'react';
import Diagram from './Diagrama';

function ProcessForm() {
    const [diagram, setDiagram] = useState(null);
    const [times, setTimes] = useState(null);
    const [method, setMethod] = useState('FCFS');
    const [cuantum, setCuantum] = useState(0);
    useEffect(()=>{
        console.log("USE EFFECT:",diagram);
    },[diagram])
    const getGantt = async () => {
        
        try{
            
            await axios.get('http://localhost:8000/api/process')
                .then(res => {
                    console.log('============ Response form GET ===============');
                    console.log(res.data);
                    setDiagram(JSON.parse(res.data[0]))
                    setTimes(JSON.parse(res.data[1]))
                    console.log(JSON.parse(res.data[1]));
                    console.log(res.data);
                })
                .catch(error => {
                    console.log(error);
                })
        } catch (error) {
            console.log('Error: ', error)
        }
        
    }
      

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
        ) {
            // if (formData.priority.trim() === '') setFormData({...formData, priority:''})
            console.error('Fields name, cpu_time and arrival cannot be blank');
            return;
        }

        // Add the current form data to the list of processes        
        setProcesses([...processes, formData]);
        // Clear the form
        setFormData({ name: '', cpu_time: '', arrival: '', priority: '' });
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
        let request = {"data":processes, "method":method};
        // Send the processes data to the API
        try {
            // const dataArray = [
            //     { name: "Process 1", cpu_time: 10, arrival: 5, priority: 2 },
            //     { name: "Process 2", cpu_time: 8, arrival: 3, priority: 1 },
            //     // Add more data objects as needed
            // ];
            await axios.post('http://localhost:8000/api/process', request, {
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
    const handleM = (event) => {
        setMethod(event.target.value);
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

                    />
                    <input
                        type="number"
                        min={0}
                        name="cpu_time"
                        placeholder="CPU"
                        value={formData.cpu_time}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'

                    />
                    <input
                        type="number"
                        min={0}
                        name="arrival"
                        placeholder="Arrival"
                        value={formData.arrival}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                    />
                    <input
                        type="number"
                        min={0}
                        name="priority"
                        placeholder="Priority"
                        value={formData.priority}
                        onChange={handleChange}
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5'
                    />
                </div>
                <div className="flex justify-center items-center h-full m-3">
                    <button className='p-2 bg-green-600 border border-green-800 hover:bg-green-700 text-white rounded me-2' type="button" onClick={addProcess}>Add Process</button>
                    <button className='p-2 bg-red-600 border border-red-800 hover:bg-red-700 text-white rounded me-2' type='button' onClick={deleteProcess}>Delete Process</button>
                </div>

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
                
                {processes.length != 0 && 
                <div className="flex justify-center items-center h-full m-3">
                    <select value={method} onChange={handleM} className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5' name="select">
                        <option value="FCFS">FCFS</option>
                        <option value="RR" >RR</option>
                        <option value="PRIO" >PRIO</option>
                        <option value="SJF" >SJF</option>
                        <option value="SRT" >SRT</option>
                    </select>
                    {method =="RR" &&<input
                        type="number"
                        min={0}
                        name="cuantum"
                        placeholder="cuantum"
                        className='border rounded border-indigo-400 bg-indigo-200 placeholder-indigo-400 p-1.5 mx-3 w-24'
                    />

}
                    <button className='bg-blue-600 border border-blue-600 hover:bg-blue-600 text-white rounded m-3 p-2' type="submit">Generar Diagrama</button>
                </div>}
            </form>
            {diagram && <Diagram diagram={diagram} times={times}/>}

        </div>
    );
}

export default ProcessForm;
