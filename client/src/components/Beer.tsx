export const Beer = (props: any) => {
  const beer = props.beer;
  const supplier = props.supplier;

  return (
    <div className="rounded shadow-xl transform transition border border-white border-opacity-10 hover:border-opacity-75 bg-gray-700 mx-auto">
      <div className="p-2">
        <a href={beer.url} target="_blank" rel="noreferrer">
          <div className="mx-auto h-44 w-44 bg-white rounded border border-black">
            {supplier === "Beer And Beyond" || supplier === "Biratenu" ? (
              <img
                alt={"Post header"}
                src={beer.image}
                className="mx-auto h-44 pt-0"
              />
            ) : (
              <img
                alt={"Post header"}
                src={beer.image}
                className="mx-auto h-40 pt-2"
              />
            )}
          </div>
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
