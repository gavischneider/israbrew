import { useEffect, useState } from "react";
import { AsyncBeersJSON } from "../types/AsyncBeersJSON";
import { Beer } from "./Beer";

export const AsyncBeerGrid = () => {
  const initialStateAsync = {
    beerbazaar: [],
  };

  const [asyncBeers, setAsyncBeers] = useState<AsyncBeersJSON>(
    initialStateAsync
  );

  // useEffect(() => {
  //   fetch("/api/asyncbeer")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       console.log("DATA!!!!!!!!");
  //       console.log(data);
  //       setAsyncBeers(data.beers);
  //     });
  // }, []);

  return (
    <div className="container mx-auto bg-gray-900 mt-5">
      <div className="object-center grid grid-cols-1 gap-12 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 mx-auto pb-6 pt-6">
        {asyncBeers.beerbazaar ? (
          asyncBeers.beerbazaar.map((beer: any) => {
            const b = JSON.parse(beer);
            return <Beer beer={b} key={b.name} />;
          })
        ) : (
          <div className="text-white">Loading...</div>
        )}
      </div>
    </div>
  );
};
