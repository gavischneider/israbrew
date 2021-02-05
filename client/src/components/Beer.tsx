export const Beer = (props: any) => {
  const beer = props.beer;

  return (
    <div className="rounded shadow-xl transform transition border border-white border-opacity-10 hover:border-opacity-75 bg-gray-700 mx-auto min-w-full">
      <div className="p-2">
        <a href={beer.url} target="_blank" rel="noreferrer">
          <img
            alt={"Post header"}
            src={beer.image}
            className="rounded border border-black mx-auto w-44 h-44"
          />

          <div className="">
            <div className="text-white my-2">{beer.name}</div>
            <div className="text-white mb-2">
              {beer.brewery ? beer.brewery : ""}
            </div>
            <div className="text-white my-2 opacity-75">{beer.price}</div>
          </div>
        </a>
      </div>
    </div>
  );
};
