import './App.scss'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { TaskPage } from './pages/TaskPage'
import { TaskFormPage } from './pages/TaskFormPage'
import { Navigation } from './components/Navigation'

function App() {

  return (
    <div className='App'>
      <BrowserRouter>
        <Navigation/>
        <Routes>
          <Route path='/' element={<Navigate to='/tasks'/>}/>
          <Route path='/tasks' element={<TaskPage/>}/>
          <Route path='/tasks-create' element={<TaskFormPage/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
