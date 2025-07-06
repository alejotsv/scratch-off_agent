type Props = {
  game: string;
  odds: string;
  ticket_price: string;
  summary: string;
};

const TicketCard = ({ game, odds, ticket_price, summary }: Props) => {
  return (
    <div className="bg-white p-4 rounded shadow-md">
      <h2 className="text-xl font-semibold">{game}</h2>
      <p className="text-sm text-gray-600 mb-1">Odds: {odds}</p>
      <p className="text-sm text-gray-600 mb-2">Price: {ticket_price}</p>
      <p className="text-gray-700">{summary}</p>
    </div>
  );
};

export default TicketCard;
