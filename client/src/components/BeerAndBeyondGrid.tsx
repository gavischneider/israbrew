import { Beer } from "./Beer";

export const BeerAndBeyondGrid = (props: any) => {
  console.log(props.beers);
  const beers = props.beers;

  return (
    <div className="container mx-auto bg-gray-900 mt-5">
      <div className="object-center grid grid-cols-1 gap-12 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 mx-auto pb-6 pt-6">
        {beers.map((beer: any) => {
          const b = JSON.parse(beer);
          return <Beer beer={b} key={b.name} />;
        })}
      </div>
    </div>
  );
};
