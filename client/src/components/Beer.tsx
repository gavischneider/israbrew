export const Beer = (props: any) => {
  const beer = props.beer;
  return (
    <div className="rounded shadow-xl transform transition border border-white border-opacity-10 hover:border-opacity-75 bg-gray-700 mx-auto">
      <div className="p-2">
        <a href={beer.url} target="_blank" rel="noreferrer">
          <img
            alt={"Post header"}
            src={beer.image}
            className="rounded border border-black"
          />

          <h1 className="text-white my-2">{beer.name}</h1>
          <h3 className="text-white mb-2 opacity-75">
            {beer.brewery ? beer.brewery : ""}
          </h3>
          <h4 className="text-white my-2">{beer.price}</h4>
        </a>
      </div>
    </div>
  );
};
