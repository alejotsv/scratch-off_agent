import { useEffect, useState } from 'react';

const ChatBox = ({ onStop }: { onStop: () => void }) => {
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
  const [userInput, setUserInput] = useState('');
  const [apiResponse, setApiResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUserInput(e.target.value);
  };

  const handleSend = async () => {
    if (!userInput.trim()) return;

    const userQuestion = userInput;
    setUserInput('');
    setApiResponse('');
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'odds-debug': 'false' // Set to 'true' for debugging
        },
        body: JSON.stringify({ question: userQuestion })
      });

      const data = await res.json();

      if (data.response) {
        setApiResponse(data.response);
        // console.log('DEBUG info:', data.debug, data.games);
      } else if (data.error) {
        setApiResponse(`⚠️ Error: ${data.error}`);
      } else {
        setApiResponse('⚠️ Unexpected response.');
      }
    } catch (err) {
      console.error(err);
      setApiResponse('⚠️ Network error. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (apiResponse) {
      console.log('API response received');
      // console.log('Received API response:', apiResponse);
    }
  }, [apiResponse]);

  const isSendDisabled = userInput.trim() === '';

  return (
    <div className="flex flex-col justify-center items-center bg-white h-[100vh] text-zinc-900 px-4">
      <h2 className="text-lg font-medium text-center text-orange-600">
        Enter your lottery odds question
      </h2>
      <div className="w-full max-w-xl mt-10 flex items-center gap-2">
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="e.g. What are the best $10 tickets with prizes remaining?"
          className="flex-grow border border-orange-300 p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-400"
        />
        <button
          onClick={handleSend}
          disabled={isSendDisabled}
          className={`cursor-pointer font-semibold py-3 px-5 rounded-md transition ${
            isSendDisabled
              ? 'bg-gray-300 text-white cursor-not-allowed'
              : 'bg-orange-400 hover:bg-orange-300 text-white'
          }`}
        >
          Send
        </button>
      </div>

      <div className="w-full max-w-xl mt-6 border border-orange-200 bg-orange-50 text-orange-900 p-4 rounded-md h-[300px] overflow-y-auto text-base font-normal">

        {loading ? (
          <div className="flex items-center gap-2">
            <svg
              className="animate-spin h-5 w-5 text-orange-500"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
              ></path>
            </svg>
            <span>Checking for your best odds...</span>
          </div>
        ) : apiResponse ? (
          <pre className="whitespace-pre-wrap break-words">{apiResponse}</pre>
        ) : (
          <span className="text-gray-400 italic">Waiting...</span>
        )}
      </div>

      <p className="text-xs italic text-gray-500 mt-2">
        This is an AI-powered recommendation tool using public scratch-off ticket data. Lottery games are games of chance. Please play responsibly.
      </p>

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
