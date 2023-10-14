import './index.css'
import ProcessForm from './components/Form'
import Diagram from './components/Diagrama'

function App() {

  return (
    <main className=" bg-slate-900 h-full min-h-screen relative isolate pt-14FF">
      { 
      <div
        className="fixed inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        aria-hidden="true"
      >
        <div
          className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#cda427c7] to-[#e5de89] opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
          style={{
            clipPath:
              'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)',
          }}
        />
      </div> }

      <div className="flex flex-col mx-3  border-red-500">
        <h1 className='mx-auto text-center text-4xl text-white font-bold  my-14 m-5'>
          GESTIÓN DE PROCESOS
        </h1>
        <ProcessForm />


        
      </div>

    </main>

  )
}

export default App
