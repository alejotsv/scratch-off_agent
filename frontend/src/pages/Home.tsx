import Header from '../components/Header';
import TicketCard from '../components/TicketCard';

const tickets = [
  {
    game: "$15MM GOLD RUSH MULTIPLIER (#1574)",
    odds: "1:2.6",
    ticket_price: "$30",
    summary: "Best odds under $30 with strong value at lower prize tiers.",
  },
  {
    game: "GOLD RUSH LIMITED (#1501)",
    odds: "1:2.65",
    ticket_price: "$20",
    summary: "Close contender with good overall odds and lower price.",
  },
];

const Home = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <Header />
      <div className="grid gap-4 mt-4">
        {tickets.map((ticket, idx) => (
          <TicketCard key={idx} {...ticket} />
        ))}
      </div>
    </div>
  );
};

export default Home;
