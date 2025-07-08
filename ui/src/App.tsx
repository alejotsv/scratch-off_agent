import { useState } from 'react';
import LandingPage from './components/LandingPage';
import ChatBox from './components/ChatBox';
import GoodbyePage from './components/GoodbyePage';

const App = () => {
  const [view, setView] = useState<'landing' | 'chat' | 'goodbye'>('landing'); 
  const onStart = () => {
    setView('chat');
  };
  const onStop = () => {
    setView('goodbye');
  };
  const backHome = () => {
    setView('landing');
  }

  return (
    <div>
        {view === 'landing' && (
          <LandingPage onStart={onStart} />
        )}
        {view === 'chat' && (
          <ChatBox onStop={onStop} />
        )}
        {view === 'goodbye' && (
          <GoodbyePage onStart={onStart} backHome={backHome} />
        )}
    </div>
  );
};

export default App;
