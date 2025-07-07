import { useState } from 'react';
import LandingPage from './components/LandingPage';
import ChatBox from './components/ChatBox';

const App = () => {
  const [showChat, setShowChat] = useState(false);

  return (
    <main className="bg-white min-h-screen text-gray-900 font-sans">
      {showChat ? (
        <ChatBox onStop={() => setShowChat(false)} />
      ) : (
        <LandingPage onStart={() => setShowChat(true)} />
      )}
    </main>
  );
};

export default App;
