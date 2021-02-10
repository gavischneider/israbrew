import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
import { BeersJSON } from "../types/BeersJSON";
import { BeerGrid } from "./BeerGrid";

export const TabsBar = () => {
  const initialState = {
    beerandbeyond: [],
    biratenu: [],
    mendelsonheshin: [],
    beerz: [],
    beerbazaar: [],
    keshetteamim: [],
    tivtaam: [],
  };

  const [beers, setBeers] = useState<BeersJSON>(initialState);

  useEffect(() => {
    fetch("/api/beers")
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
        <Tab>Tiv Taam</Tab>
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
        <BeerGrid beers={beers.mendelsonheshin} supplier={"Mendelson Heshin"} />
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
      <TabPanel>
        <BeerGrid beers={beers.tivtaam} supplier={"Tiv Taam"} />
      </TabPanel>
    </Tabs>
  );
};
