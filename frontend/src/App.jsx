import './index.css'
import ProcessForm from './components/Form'

function App() {

  return (
    <div className="flex flex-col mx-3 border border-red-500">
      <h1 className='mx-auto text-center text-3xl text-red-600 border mb-7'>
        Gestion de Procesos
      </h1>
      
      <ProcessForm />
    </div>
  )
}

export default App
