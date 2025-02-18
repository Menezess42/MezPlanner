import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './style/index.css'
import App from './src/App.jsx'

createRoot(document.getElementById('root')).render(
    <App/>,
)
