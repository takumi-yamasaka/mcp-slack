import './App.css'
import Chat from './components/chat/Chat'

function App() {
  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4 shadow-md">
        <div className="container mx-auto">
          <h1 className="text-2xl font-bold">Trast Project Assistant</h1>
          <p className="text-sm opacity-80">MCP Client for project knowledge</p>
        </div>
      </header>
      <main className="flex-1 container mx-auto p-4 overflow-hidden">
        <div className="bg-white rounded-lg shadow-lg h-full overflow-hidden">
          <Chat />
        </div>
      </main>
      <footer className="bg-gray-800 text-white p-2 text-center text-sm">
        <p>MCP Client - Powered by OpenAI</p>
      </footer>
    </div>
  )
}

export default App
