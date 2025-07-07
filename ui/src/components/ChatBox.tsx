import React from 'react';

const ChatBox = ({ onStop }: { onStop: () => void }) => {
  return (
    <div className="flex flex-col justify-center items-center bg-white h-[100vh]">
      <div className="mx-auto flex w-full mt-20 flex-col justify-center px-5 pt-0 md:h-[unset] md:max-w-[80%] lg:h-[60vh] lg:max-w-[80%] lg:px-6 xl:pl-0 ">
        <div className="relative flex w-full flex-col pt-[20px] md:pt-0">
          <div className="mx-auto flex min-h-[25vh] w-full max-w-[1000px] flex-col xl:min-h-[35vh]">
            <div className="mx-auto flex w-full flex-col flex mb-auto">
              <div className="mb-2.5 flex w-full items-center text-center">
                <div className="mr-5 flex h-[40px] min-h-[40px] min-w-[40px] items-center justify-center rounded-full border border-zinc-200 bg-transparent dark:border-transparent dark:bg-white">
                  <svg className="h-4 w-4" viewBox="0 0 24 24" fill="currentColor">
                    <path fillRule="evenodd" clipRule="evenodd" d="M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0ZM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695Z" />
                  </svg>
                </div>
                <div className="flex w-full">
                  <div className="me-2.5 flex w-full rounded-lg border border-zinc-200 bg-white/10 p-5 backdrop-blur-xl dark:border-white/10 dark:bg-zinc-950">
                    <p className="text-sm font-medium leading-6 text-zinc-950 dark:text-white md:text-base md:leading-[26px]">
                    Ask Scratchy: What’s the best $10 ticket with top prizes left?
                    </p>
                  </div>
                  <button
                    onClick={onStop}
                    className="flex w-[70px] cursor-pointer items-center justify-center rounded-lg border border-zinc-200 bg-white/10 p-5 backdrop-blur-xl dark:border-white/10 dark:bg-zinc-950"
                  >
                    <svg className="h-[20px] w-[20px] text-zinc-950 dark:text-white" viewBox="0 0 20 20" fill="currentColor">
                      <path d="m5.433 13.917 1.262-3.155A4 4 0 0 1 7.58 9.42l6.92-6.918a2.121 2.121 0 0 1 3 3l-6.92 6.918c-.383.383-.84.685-1.343.886l-3.154 1.262a.5.5 0 0 1-.65-.65Z" />
                      <path d="M3.5 5.75c0-.69.56-1.25 1.25-1.25H10A.75.75 0 0 0 10 3H4.75A2.75 2.75 0 0 0 2 5.75v9.5A2.75 2.75 0 0 0 4.75 18h9.5A2.75 2.75 0 0 0 17 15.25V10a.75.75 0 0 0-1.5 0v5.25c0 .69-.56 1.25-1.25 1.25h-9.5c-.69 0-1.25-.56-1.25-1.25v-9.5Z" />
                    </svg>
                  </button>
                </div>
              </div>
              <div className="flex w-full">
                <div className="mr-5 flex h-10 min-h-[40px] min-w-[40px] items-center justify-center rounded-full bg-zinc-950 dark:border dark:border-zinc-800">
                  <svg className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="currentColor">
                    <path fillRule="evenodd" clipRule="evenodd" d="M9 4.5a.75.75 0 0 1 .721.544l.813 2.846a3.75 3.75 0 0 0 2.576 2.576l2.846.813a.75.75 0 0 1 0 1.442l-2.846.813a3.75 3.75 0 0 0-2.576 2.576l-.813 2.846a.75.75 0 0 1-1.442 0l-.813-2.846a3.75 3.75 0 0 0-2.576-2.576l-2.846-.813a.75.75 0 0 1 0-1.442l2.846-.813A3.75 3.75 0 0 0 7.466 7.89l.813-2.846A.75.75 0 0 1 9 4.5ZM18 1.5a.75.75 0 0 1 .728.568l.258 1.036c.236.94.97 1.674 1.91 1.91l1.036.258a.75.75 0 0 1 0 1.456l-1.036.258c-.94.236-1.674.97-1.91 1.91l-.258 1.036a.75.75 0 0 1-1.456 0l-.258-1.036a2.625 2.625 0 0 0-1.91-1.91l-1.036-.258a.75.75 0 0 1 0-1.456l1.036-.258a2.625 2.625 0 0 0 1.91-1.91l.258-1.036A.75.75 0 0 1 18 1.5ZM16.5 15a.75.75 0 0 1 .712.513l.394 1.183c.15.447.5.799.948.948l1.183.395a.75.75 0 0 1 0 1.422l-1.183.395c-.447.15-.799.5-.948.948l-.395 1.183a.75.75 0 0 1-1.422 0l-.395-1.183a1.5 1.5 0 0 0-.948-.948l-1.183-.395a.75.75 0 0 1 0-1.422l1.183-.395c.447-.15.799-.5.948-.948l.395-1.183A.75.75 0 0 1 16.5 15Z" />
                  </svg>
                </div>
                <div className="rounded-lg border shadow-sm flex !max-h-max bg-zinc-950 p-5 !px-[22px] !py-[22px] text-base font-normal leading-6 text-white backdrop-blur-xl dark:border-zinc-800 dark:!bg-white/5 dark:text-white md:text-base md:leading-[26px]">
                  <div className="text-base font-normal">
                  <p><strong>Best $10 Ticket to Play Right Now</strong></p>
                  <p>&nbsp;</p>
                  <p>
                    Based on the latest data, the <strong>"$10,000 Blowout"</strong> ticket offers the most favorable odds among all $10 scratch-offs.
                  </p>
                  <p>&nbsp;</p>
                  <p>
                    <strong>Top Prizes Remaining:</strong> 7 out of 8<br/>
                    <strong>Overall Odds:</strong> 1 in 3.65<br/>
                    <strong>Best Odds Tier:</strong> $500 and $1,000 prizes
                  </p>
                  <p>&nbsp;</p>
                  <p>
                    <strong>Recommendation:</strong> This ticket shows low claim velocity and high top-tier prize retention — ideal for maximizing ROI.
                  </p>
                  <p>&nbsp;</p>
                  <p><em>Note: Odds and availability vary by retailer and region. Check for updates before purchasing.</em></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div> 
    </div>
  );
};

export default ChatBox;
