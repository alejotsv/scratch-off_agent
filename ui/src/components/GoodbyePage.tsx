const GoodbyePage = ({
  onStart,
  backHome,
}: {
  onStart: () => void;
  backHome: () => void;
}) => {
  return (
    <div className="flex flex-col items-center justify-center h-[80vh] text-center space-y-6 px-4">
      <h1 className="text-4xl font-bold text-orange-400">Thanks for using Scratchy!</h1>
      <p className="text-lg text-gray-700 max-w-xl">
        We hope the odds are always in your favor. Come back anytime to check the best scratch-off tickets available.
      </p>
      <div className="flex flex-col sm:flex-row gap-4 mt-6">
        <button
          onClick={onStart}
          className="cursor-pointer py-3 px-5 inline-flex items-center justify-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-orange-400 text-white hover:bg-orange-300 transition"
        >
          🎯 Start Chat Again
        </button>
        <button
          onClick={backHome}
          className="cursor-pointer py-3 px-5 inline-flex items-center justify-center gap-x-2 text-sm font-semibold rounded-lg border border-transparent bg-gray-200 text-gray-800 hover:bg-gray-300 transition"
        >
          🏠 Home
        </button>
      </div>
    </div>
  );
};

export default GoodbyePage;
