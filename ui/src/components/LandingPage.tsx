const LandingPage = ({ onStart }: { onStart: () => void }) => {
  return (
    <div className="relative overflow-hidden">
      {/* Gradients */}
      <div aria-hidden="true" className="flex absolute -top-96 start-1/2 transform -translate-x-1/2">
        <div className="bg-gradient-to-tl from-orange-200 via-orange-100 to-white blur-3xl w-[90rem] h-[50rem] rounded-full origin-top-left -rotate-12 -translate-x-[15rem]"></div>
        <div className="bg-gradient-to-tl from-orange-200 via-orange-100 to-white blur-3xl w-[90rem] h-[50rem] rounded-full origin-top-left -rotate-12 -translate-x-[15rem]"></div>
      </div>
      {/* End Gradients */}

      <div className="relative z-10">
        <div className="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 min-h-[80vh] flex items-center justify-center">
          <div className="max-w-2xl text-center mx-auto">
            <p className="inline-block text-sm font-medium bg-clip-text bg-gradient-to-l from-orange-600 to-orange-300 text-transparent">
              Get your lottery odds with...
            </p>

            {/* Title */}
            <div className="mt-5 max-w-2xl">
              <h1 className="block font-semibold text-4xl md:text-5xl lg:text-6xl bg-clip-text text-transparent bg-gradient-to-r from-orange-700 via-orange-400 to-white">
                Scratchy!
              </h1>
              <h2>
                <span className="text-gray-500 text-lg md:text-xl lg:text-2xl dark:text-gray-400">
                  Your AI-powered lottery assistant
                </span>
              </h2>
            </div>
            {/* End Title */}

            <div className="mt-5 max-w-3xl">
              <p className="text-lg text-gray-600 dark:text-gray-400">
                {/* Describe how Scratchy is a tool that uses a Flask API and an agentic system with Bedrock */}
                Scratchy is your AI-powered lottery companion, built with Amazon Bedrock and agentic AI patterns. Leveraging real-time odds and custom filters, it helps you make smarter, data-driven ticket selections.
              </p>
            </div>

            {/* Buttons */}
            <div className="mt-8 gap-3 flex justify-center">
              <button
                onClick={onStart}
                className="cursor-pointer py-3 px-4 inline-flex items-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-orange-400 text-white hover:bg-orange-300 disabled:opacity-50 disabled:pointer-events-none dark:focus:outline-none dark:focus:ring-1 dark:focus:ring-gray-600"
              >
                Get started
                <svg className="flex-shrink-0 w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor">
                  <path d="m9 18 6-6-6-6" />
                </svg>
              </button>              
            </div>
            {/* End Buttons */}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
