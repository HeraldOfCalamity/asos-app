import React, { useEffect, useState } from 'react';

function Diagram(props) {
    const [data, setData] = useState(props.diagram)
    const [times, setTimes] = useState(props.times)

    useEffect(() => {
        setData(props.diagram);
        setTimes(props.times)

    }, [props.diagram, props.times])

    return (
        <div className='my-10'>
            <h1 className='mx-auto text-center text-4xl text-white font-bold my-14'>
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
                                        {data[process][colunm] && data[process][colunm][0] != "0"
                                            ? <h4>
                                                {data[process][colunm][0]}
                                                <sub>{data[process][colunm][1]}</sub>
                                            </h4>
                                            : <h4>Ø</h4>}
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
                                        {data[process][colunm] && <h4>
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
            <h1 className='mx-auto text-center text-4xl text-white font-bold my-14'>
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
