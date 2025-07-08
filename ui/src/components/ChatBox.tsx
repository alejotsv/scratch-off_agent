import { useEffect, useState } from 'react';

const ChatBox = ({ onStop }: { onStop: () => void }) => {
  const [userInput, setUserInput] = useState('');
  const [apiResponse, setApiResponse] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUserInput(e.target.value);
  };

  const handleSend = () => {
    console.log('Payload to API:', userInput);
    setApiResponse(''); // Reset response
    setTimeout(() => {
      setApiResponse(`Fake API response to: ${userInput}`);
    }, 1000);
  };

  useEffect(() => {
    if (apiResponse) {
      console.log('Received API response:', apiResponse);
    }
  }, [apiResponse]);

  return (
    <div className="flex flex-col justify-center items-center bg-white h-[100vh] text-zinc-900 px-4">      
      <div className="w-full max-w-xl mt-10 flex items-center gap-2">
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="Ask Scratchy..."
          className="flex-grow border border-orange-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-400"
        />
        <button
          onClick={handleSend}
          className="cursor-pointer bg-orange-400 hover:bg-orange-300 text-white font-semibold py-3 px-5 rounded-md transition"
        >
          Send
        </button>
      </div>
      
      <div className="w-full max-w-xl mt-6 border border-orange-200 bg-orange-50 text-orange-900 p-4 rounded-md min-h-[100px] text-base font-normal">
        {apiResponse ? apiResponse : <span className="text-gray-400 italic">Waiting...</span>}
      </div>

      <button
        className="mt-10 py-2 px-4 rounded bg-gray-200 hover:bg-gray-300 text-gray-800 cursor-pointer"
        onClick={onStop}
      >
        Finish Session
      </button>
    </div>
  );
};

export default ChatBox;
