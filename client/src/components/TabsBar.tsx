import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
import { BeersJSON } from "../types/BeersJSON";
import { BeerGrid } from "./BeerGrid";
import { AsyncBeerGrid } from "./AsyncBeerGrid";

export const TabsBar = () => {
  const initialState = {
    beerandbeyond: [],
    biratenu: [],
    mendelson: [],
    beerz: [],
    beerbazaar: [],
    keshetteamim: [],
  };

  const [beers, setBeers] = useState<BeersJSON>(initialState);

  useEffect(() => {
    fetch("/api/beer")
      .then((res) => res.json())
      .then((data) => {
        setBeers(data.beers);
      });
  }, []);

  return (
    <Tabs>
      <TabList>
        <Tab>Home</Tab>
        <Tab>Beer And Beyond</Tab>
        <Tab>Biratenu</Tab>
        <Tab>Mendelson Heshin</Tab>
        <Tab>BeerZ</Tab>
        <Tab>Beer Bazaar</Tab>
        <Tab>Keshet Teamim</Tab>
      </TabList>

      <TabPanel>
        <h1>Home</h1>
      </TabPanel>

      <TabPanel>
        <BeerGrid beers={beers.beerandbeyond} supplier={"Beer And Beyond"} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.biratenu} supplier={"Biratenu"} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.mendelson} supplier={"Mendelson Heshin"} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.beerz} supplier={"BeerZ"} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.beerbazaar} supplier={"Beer Bazaar"} />
      </TabPanel>
      <TabPanel>
        <BeerGrid beers={beers.keshetteamim} supplier={"Keshet Teamim"} />
      </TabPanel>
    </Tabs>
  );
};
