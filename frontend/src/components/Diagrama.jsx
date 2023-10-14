import React, { useEffect, useState } from 'react';
const xd = {
    "0": {
        "0": ["A", 1.0],
        "1": ["B", 1.0],
        "2": ["C", 1.0],
        "3": ["X", 1.0],
        "4": ["A", 1.0],
        "5": ["B", 1.0],
        "6": ["C", 1.0],
        "7": ["X", 1.0],
        "8": ["A", 1.0],
        "9": ["B", 1.0],
        "10": ["C", 1.0],
        "11": ["X", 1.0],
        "12": ["A", 1.0],
        "13": ["B", 1.0],
        "14": ["C", 1.0],
        "15": ["X", 1.0],
        "16": ["A", 1.0],
        "17": ["B", 1.0],
        "18": ["C", 1.0],
        "19": ["X", 1.0],
        "20": ["A", 1.0],
        "21": ["B", 1.0],
        "22": ["C", 1.0],
        "23": ["X", 1.0],
        "24": ["A", 1.0],
        "25": ["B", 1.0],
        "26": ["C", 1.0],
        "27": ["X", 1.0],
        "28": ["A", 1.0],
        "29": ["B", 1.0],
        "30": ["C", 1.0],
        "31": ["X", 1.0],
        "32": ["A", 1.0],
        "33": ["B", 1.0],
        "34": ["C", 1.0],
        "35": ["X", 1.0],
        "36": ["A", 1.0],
        "37": ["B", 1.0],
        "38": ["C", 1.0],
        "39": ["X", 1.0],
        "40": ["A", 1.0],
        "41": ["B", 1.0],
        "42": ["C", 1.0],
        "43": ["X", 1.0],
        "44": ["A", 1.0],
        "45": ["B", 1.0],
        "46": ["C", 1.0],
        "47": ["X", 1.0],
    },
    "1": {
        "0": ["B", 1.0],
        "1": ["C", 1.0],
        "2": ["A", 1.0]
    },
    "2": {
        "0": ["Y", 2.0],
        "1": ["C", 1.0],
        "2": ["B", 1.0]
    },
    "3": {
        "0": ["B", 1.0],
        "1": ["C", 1.0],
        "2": ["A", 1.0]
    },
    "4": {
        "0": ["Y", 2.0],
        "1": ["C", 1.0],
        "2": ["B", 1.0]
    },
    "5": {
        "0": ["B", 1.0],
        "1": ["C", 1.0],
        "2": ["A", 1.0]
    },
    "6": {
        "0": ["Y", 2.0],
        "1": ["C", 1.0],
        "2": ["B", 1.0]
    },
};

const t = {

    "0": {
        "0": ["A", 1.0],
        "1": ["A", 1.0],
    },
    "1": {
        "0": ["B", 2.0],
        "1": ["B", 1.0],
    },
    "2": {
        "0": ["C", 1.0],
        "1": ["C", 1.0],
    },
    "3": {
        "0": ["D", 2.0],
        "1": ["D", 1.0],
    },

}
function Diagram(props) {
    const [data, setData] = useState(props.diagram)
    const [times, setTimes] = useState(props.times)

    useEffect(()=>{
        setData(props.diagram);
        setTimes(props.times)

    },[props.diagram,props.times])

    return (
        <div className='my-10'>
            <h1 className='mx-auto text-center text-4xl text-white font-bold border mb-7'>
                DIAGRAMA DE GANTT
            </h1>
            <div className="w-10/12 border rounded-lg shadow overflow-auto dark:border-gray-700 dark:shadow-gray-900 m-auto my-5">
                <table className="w-full text-sm text-center text-gray-500 dark:text-gray-400" >
                    <tbody className="font-medium text-lg divide-y divide-gray-200 dark:divide-gray-700">
                        {data && Object.keys(data).map((process) => (
                            process == 0 &&
                            <tr >
                                {Object.keys(data[process]).map((colunm) => (

                                    <td className="p-3">
                                        {data[process][colunm]&&<h4>
                                            {data[process][colunm][0]}
                                            <sub>{data[process][colunm][1]}</sub>
                                        </h4>}
                                    </td>

                                ))}
                            </tr>
                        ))}
                        {data && Object.keys(data).map((process) => (
                            process == 1 &&
                            <tr className=" bg-gray-50 dark:bg-gray-700">
                                {Object.keys(data[0]).map((index) => (

                                    <td className="p-2">
                                        {index}
                                    </td>

                                ))}
                            </tr>
                        ))}
                        {data && Object.keys(data).map((process) => (
                            process != 0 &&
                            <tr >
                                {Object.keys(data[process]).map((colunm) => (

                                    <td className="p-3">
                                        {data[process][colunm]&&<h4>
                                            {data[process][colunm][0]}
                                            <sub>{data[process][colunm][1]}</sub>
                                        </h4>}
                                    </td>

                                ))}
                            </tr>
                        ))}

                    </tbody>
                </table>
            </div>
            <h1 className='mx-auto text-center text-4xl text-white font-bold border mb-7'>
                TIEMPOS
            </h1>
            <div className="w-10/12 border rounded-lg shadow overflow-auto dark:border-gray-700 dark:shadow-gray-900 m-auto my-5">
                <table className="w-full text-sm text-center text-gray-500 dark:text-gray-400" >
                    <thead className="text-base bg-gray-50 dark:bg-gray-700">
                        <tr>
                            <th className="py-3">PROCESO</th>
                            <th>TIEMPO DE RETORNO</th>
                            <th>TIEMPO DE ESPERA</th>
                        </tr>
                    </thead>
                    <tbody className="font-medium text-base divide-y divide-gray-200 dark:divide-gray-700">
                        {times && Object.keys(times).map((process) => (

                            <tr >
                                <td className="p-3">
                                    <h4>
                                        {times[process][0][0]}
                                    </h4>
                                </td>
                                {Object.keys(times[process]).map((colunm) => (

                                    <td className="p-3">
                                        {times[process][colunm] && <h4>
                                            {times[process][colunm][1]}
                                        </h4>}
                                    </td>

                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Diagram;
